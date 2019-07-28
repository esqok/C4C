from __future__ import print_function
import json
from ibm_watson import AssistantV2

# If service instance provides API key authentication
assistant = AssistantV2(
    version='2018-09-20',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://gateway.watsonplatform.net/assistant/api',
    iam_apikey='h-GZ2mQAAPDfErkSOhgJRjIs57fSQb0-Uj0KCK9ekp-B')

# assistant = AssistantV2(
#     username='YOUR SERVICE USERNAME',
#     password='YOUR SERVICE PASSWORD',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/assistant/api',
#     version='2018-09-20')

#########################
# Sessions
#########################

session = assistant.create_session("<ahmad ar>").get_result()
print(json.dumps(session, indent=2))

assistant.delete_session("<ahmad ar>", "<YOUR SESSION ID>").get_result()

#########################
# Message
#########################

message = assistant.message(
    "<ahmad ar>",
    "<YOUR SESSION ID>",
    input={'text': 'What\'s the weather like?'},
    context={
        'metadata': {
            'deployment': 'myDeployment'
        }
    }).get_result()
print(json.dumps(message, indent=2))
