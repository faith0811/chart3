# chart3/app/model.py

chat_cache = []
# this chat_cache includes all existed chat message.

def model_init():
    pass

def add_a_chat_message(message):
    global chat_cache
    chat_cache.append(message)

def get_latest_chat_message():
    message = chat_cache[len(chat_cache)-10:10]
    return message


