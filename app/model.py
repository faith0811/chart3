# chart3/app/model.py

from json import loads, dumps

chat_cache = []
# this chat_cache includes all existed chat message.

def model_init():
    pass

def add_a_chat_message(message_json):
    global chat_cache
    #transform json into python dictionary
    message = loads(message_json)
    chat_cache.append(message)

def get_latest_chat_message():
    message = chat_cache[len(chat_cache)-10:10]
    message_json = dumps(message)
    return message_json


