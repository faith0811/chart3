# chart3/app/sockets.py

import time
from flask.ext.socketio import emit
from model import add_a_chat_message, get_latest_chat_message
from . import socketio

@socketio.on('chat', namespace = '/chat')
def chat_broadcasting(received_json):
    print (received_json)
    message = transform_html_keywords(received_json)
    print (received_json)
    add_a_chat_message(message)
    emit('chat response', {'data':message}, broadcast = True)

@socketio.on('connect', namespace = '/chat')
def connect():
    emit('chat response', {'data':['welcome to chart3!','system', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]})
    show_latest_message()

def show_latest_message():
    message = get_latest_chat_message()
    for item in message:
        emit('chat response', {'data':item})

def transform_html_keywords(message):
    transformed_message = []
    for item in message:
        item = item.replace(u'&', u'&amp;')
        item = item.replace(u' ', u'&nbsp;')
        item = item.replace(u'"', u'&quot;')
        item = item.replace(u'<', u'&lt;')
        item = item.replace(u'>', u'&gt;')
        transformed_message.append(item)
    return transformed_message

