# chart3/app/models.py

import time
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Model

chat_cache = []
# this chat_cache includes all existed chat message.

class Message(Model):
    __tablename__ = 'messages'
    id = Column('message_id', Integer, primary_key = True)
    message_content = Column(String(240))
    sender_id = Column(Integer, ForeignKey('users.user_id'))
    time = Column(DateTime)

    def __init__(self, message_content, sender_id):
        self.message_content = message_content
        self.sender_id = sender_id

    @property
    def message_json():
        return [self.message_content,self.sender_id]

class User(Model):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key = True)
    username = Column(String(50), unique = True)
    email = Column(String(50), unique = True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @property
    def user_id():
        return self.id


def add_a_chat_message(message):
    global chat_cache
    message.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    chat_cache.append(message)
    #print chat_cache

def get_latest_chat_message():
    message = chat_cache[-10:]
    #print message
    return message
