# Library:
###################
from pip import print_function
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
from twilio.rest import Client
import pyaudio
import difflib
#import MicrophoneSpeechToText as mst
#from tkinter import *
import speech_recognition as sr
import webbrowser as wb
import wave
import os
# importing time module
import time
import pyglet






# Voice - T to S:
###################

# If service instance provides API key authentication
service = TextToSpeechV1(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://stream.watsonplatform.net/text-to-speech/api',
    iam_apikey='your API Key')




# Voice Class Playing :
#######################

class Play(object):
    """
    Wrapper to play the audio in a blocking mode
    """
    def __init__(self):
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 22050
        self.chunk = 1024
        self.pyaudio = None
        self.stream = None

    def start_streaming(self):
        self.pyaudio = pyaudio.PyAudio()
        self.stream = self._open_stream()
        self._start_stream()

    def _open_stream(self):
        stream = self.pyaudio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            output=True,
            frames_per_buffer=self.chunk,
            start=False
        )
        return stream

    def _start_stream(self):
        self.stream.start_stream()

    def write_stream(self, audio_stream):
        self.stream.write(audio_stream)

    def complete_playing(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pyaudio.terminate()





# Voice Caller - Talk and Print:
################################

class MySynthesizeCallback(SynthesizeCallback):
    def __init__(self):
        SynthesizeCallback.__init__(self)
        self.play = Play()

    def on_connected(self):
        print('Hablando!')
        self.play.start_streaming()

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_timing_information(self, timing_information):
        print(timing_information)

    def on_audio_stream(self, audio_stream):
        self.play.write_stream(audio_stream)

    def on_close(self):
        print('Listo!')
        self.play.complete_playing()




        
        
# Welcome MSG 1:
###################

test_callback = MySynthesizeCallback()
service.synthesize_using_websocket("Hola!",
                                   test_callback,
                                   accept='audio/wav',
                                   voice="es-LA_SofiaV3Voice"
                                )



# Welcome MSG 2:
###################


#test_callback = MySynthesizeCallback()
#service.synthesize_using_websocket(" vamos a escuchar musica de 2 minutos!",
  #                                 test_callback,
    #                               accept='audio/wav',
      #                             voice="es-LA_SofiaV3Voice"

    #                        )


###################
# Music Play:     #
###################

#os.startfile('C:/tmp1/temp2.mp3')
#print("Before the sleep statement")
#time.sleep(6
           #)
#print("After the sleep statement")



# Q1:
###################

test_callback = MySynthesizeCallback()
service.synthesize_using_websocket("¿Cómo te sientes despues de la emergencia?",
                                   test_callback,
                                   accept='audio/wav',
                                   voice="es-LA_SofiaV3Voice"
                                  )




# Voice - S to T:
###################

r = sr.Recognizer()
with sr.Microphone() as source:
 print ("Escuchando!")
 audio = r.listen(source)
 text = r.recognize_google(audio)
 b = "miedo peligro"
print (text)






# Q2:
###################

test_callback = MySynthesizeCallback()
service.synthesize_using_websocket("¿Son accidentales o intencionales?",
                                   test_callback,
                                   accept='audio/wav',
                                   voice="es-LA_SofiaV3Voice"
                                  )
# Voice - S to T:
###################

r1 = sr.Recognizer()
with sr.Microphone() as source:
 print ("Escuchando!")
 audio1 = r1.listen(source)
 text1 = r1.recognize_google(audio1)
 a = "si"
print (text1)






seq = difflib.SequenceMatcher(None,b,text)
d1 = seq.ratio()*100



if text1==a:
 seq = difflib.SequenceMatcher(None,a,text1)
 d2 = seq.ratio()*100
 
else:
 seq = difflib.SequenceMatcher(None,a,text1)
 d2 = seq.ratio()*50
 

 
test_callback = MySynthesizeCallback()
service.synthesize_using_websocket("¿que hiciste en el catastrofe?",
                               test_callback,
                               accept='audio/wav',
                               voice="es-ES_LauraV3Voice"
                              )
save2 = input()
c = "ayude sali"
print (save2)
seq = difflib.SequenceMatcher(None,c,save2)
d3 = seq.ratio()*100
print(d1)
print(d2)
print(d3)


z = (d1+d2+d3)




account_sid = ' your account sid '
auth_token = 'your auth tokn'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         from_='whatsapp source',
         body='Q1  -  ' + text + " + R1 = " + str (d1),
         to='whatsapp dest'
     )
print(message.sid)




account_sid = '-'
auth_token = '-'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         from_='-',
         body='Q2  -  ' + text1 + " + R2 = " + str (d2),
         to='-'
     )
print(message.sid)




account_sid = '-'
auth_token = '-'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         from_='-',
         body='Q3  -  ' + save2 + " + R3 = " + str (d3),
         to='-'
     )
print(message.sid)




account_sid = '-'
auth_token = '-'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         from_='-',
         body='RT -  ' + " + Z = " + str (z),
         to='-'
     )
print(message.sid)



print ("Z = ", z)





