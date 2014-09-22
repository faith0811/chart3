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


@socketio.on('init', namespace = '/chat')
def show_latest_message(msg):
    message = get_latest_chat_message()
    for item in message:
        emit('chat response', {'data':item})


def transform_html_keywords(message):
    transformed_message = []
    html_keywords = [u'&', u' ', u'"', u'>', u'<']
    html_keywords_dict = {u'>':u'&gt;', u'<':u'&lt;', u'"':u'&quot;',u' ':u'&nbsp;', u'&':u'&amp;'}
    for item in message:
        for keywords in html_keywords:
            print keywords
            item = item.replace(keywords, html_keywords_dict[keywords])
        transformed_message.append(item)
    return transformed_message

