# chart3/app/sockets.py

import time
from flask.ext.socketio import emit
from model import add_a_chat_message, get_latest_chat_message
from . import socketio

@socketio.on('chat', namespace = '/chat')
def chat_broadcasting(received_json):
    print (received_json)
    add_a_chat_message(received_json)
    emit('chat response', {'data':received_json}, broadcast = True)

@socketio.on('connect', namespace = '/chat')
def connect():
    emit('chat response', {'data':['welcome to chart3!','system', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]})
    show_latest_message()

def show_latest_message():
    message = get_latest_chat_message()
    for item in message:
        emit('chat response', {'data':item})

