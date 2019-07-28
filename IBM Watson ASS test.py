from __future__ import print_function
import json
from ibm_watson import AssistantV1

# If service instance provides API key authentication
assistant = AssistantV1(
    version='2018-09-20',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://gateway.watsonplatform.net/assistant/api',
    iam_apikey='h-GZ2mQAAPDfErkSOhgJRjIs57fSQb0-Uj0KCK9ekp-B')

                   #########################
                   #      Workspaces       #
                   #########################

create_workspace_data = {
    "name": "Taller_Carro_BH",
    "description":
     "",
    "language":
    "es",
    "intents": [{
        "intent": "General_Greetings",
      "examples": [
        {
          "text": "Buenas noches."
        },
        {
          "text": "hola"
        },
        {
          "text": "ola"
        },
        {
          "text": "Tienes un momento, por favor?"
        },
        {
          "text": "Sigues aquí?"
        },
        {
          "text": "Quién eres?"
        },
        {
          "text": "Hola, Señor."
        },
        {
          "text": "Hola, quien me puede atender?"
        },
        {
          "text": "Hola ¿puedes ayudarme?"
        },
        {
          "text": "Hola, podrías responder mi pregunta?"
        },
        {
          "text": "Hola, Cómo va todo?"
        },
        {
          "text": "Hola, ¿Cómo te sientes?"
        },
        {
          "text": "Hola, ¿Cómo estás?"
        },
        {
          "text": "Hola, Cómo estás el día de hoy?"
        },
        {
          "text": "Hola, amigo mío."
        },
        {
          "text": "Hey, ¿cómo te va?"
        },
        {
          "text": "¿Estás ahí?"
        },
        {
          "text": "¡Estoy feliz de poder hablar contigo por primera vez!"
        },
        {
          "text": "¿Cómo está? / Oye, ¿Qué tal?"
        },
        {
          "text": "Buenos días, podemos empezar la conversación?"
        }
      ],
      "description": "Saluda al bot."
    }],
    
    "entities": [{
         "entity": "marca",
      "values": [
        {
          "type": "synonyms",
          "value": "fiat",
          "synonyms": []
        },
        {
          "type": "synonyms",
          "value": "renault",
          "synonyms": [
            "renol"
          ]
        },
        {
          "type": "synonyms",
          "value": "ford",
          "synonyms": []
        },
        {
          "type": "synonyms",
          "value": "chevrolet",
          "synonyms": [
            "chevy",
            "cruze",
            "camaro"
          ]
        },
        {
          "type": "synonyms",
          "value": "mazda",
          "synonyms": []
        },
        {
          "type": "synonyms",
          "value": "audi",
          "synonyms": []
        }
      ],
     # "fuzzy_match": true
    }],
     "language": "es",
    "metadata": {},
}

response = assistant.create_workspace(
    name=create_workspace_data['name'],
    description=create_workspace_data['description'],
    language='es',
    intents=create_workspace_data['intents'],
    entities=create_workspace_data['entities'],
    #counterexamples=create_workspace_data['counterexamples'],
    metadata=create_workspace_data['metadata']).get_result()
print(json.dumps(response, indent=2))

workspace_id = response['0a482ef5-70aa-4d25-bee8-b0ed5b0e0f32']
print('Workspace id {0}'.format(workspace_id))

response = assistant.get_workspace(
    workspace_id=workspace_id, export=True).get_result()
print(json.dumps(response, indent=2))

#  message
response = assistant.message(
    workspace_id=workspace_id,
    input={
        'text': 'Hola, Soy Watson!'
    },
    context={
        'metadata': {}
    }).get_result()
print(json.dumps(response, indent=2))

response = assistant.list_workspaces().get_result()
print(json.dumps(response, indent=2))

response = assistant.update_workspace(
    workspace_id=workspace_id,
    description='Updated test workspace.').get_result()
print(json.dumps(response, indent=2))

# see cleanup section below for delete_workspace example

#########################
# Intents
#########################

examples = [{"text": "Buenos dias"}]
response = assistant.create_intent(
    workspace_id=workspace_id,
    intent='test_intent',
    description='Test intent.',
    examples=examples).get_result()
print(json.dumps(response, indent=2))

response = assistant.get_intent(
    workspace_id=workspace_id, intent='test_intent', export=True).get_result()
print(json.dumps(response, indent=2))

response = assistant.list_intents(
    workspace_id=workspace_id, export=True).get_result()
print(json.dumps(response, indent=2))

response = assistant.update_intent(
    workspace_id=workspace_id,
    intent='test_intent',
    new_intent='updated_test_intent',
    new_description='Updated test intent.').get_result()
print(json.dumps(response, indent=2))

    # see cleanup section below for delete_intent example

#########################
# Examples
#########################

response = assistant.create_example(
    workspace_id=workspace_id,
    intent='General_Greetings',
    text='hola').get_result()
print(json.dumps(response, indent=2))
#########################
# Entities
#########################

