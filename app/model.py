# chart3/app/model.py

import time

chat_cache = []
# this chat_cache includes all existed chat message.

def model_init():
    pass

def add_a_chat_message(message):
    global chat_cache
    message.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    chat_cache.append(message)
    #print chat_cache

def get_latest_chat_message():
    message = chat_cache[-10:]
    #print message
    return message
