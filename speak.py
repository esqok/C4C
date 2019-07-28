from gtts import gTTS
import pyglet
import time, os
#import googletrans
#import watson-developer-cloud
#from __future__ import print_function

def tts(text, lang):
    file = gTTS(text = text, lang = lang)
    filename = 'C:/tmp/temp.mp3'
    file.save(filename)

    music = pyglet.media.load(filename, streaming = False)
    music.play()

    time.sleep(music.duration)
  # os.remove(filename)

#def tts1(text1, lang):
 #   file = gTTS(text1 = text1, lang = lang)
  #  filename = 'C:/tmp1/temp2.mp3'
   # file.save(filename)

    #music = pyglet.media.load(filename, streaming = False)
    #music.play()

    #time.sleep(music.duration)
  # os.remove(filename)

