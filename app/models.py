# chart3/app/models.py

import time
from . import app
from peewee import *

chat_cache = []
# this chat_cache includes all existed chat message.

db = SqliteDatabase(app.config['DATABASE_URI'])

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    join_date = DateTimeField()

class Message(BaseModel):
    user = ForeignKeyField(User)
    content = CharField()
    send_time = DateTimeField()

    class Meta:
        order_by = ('-send_time',)

def create_tables():
    db.connect()
    db.create_tables([User, Message])


def add_a_chat_message(message):
    global chat_cache
    message.append(get_time())
    chat_cache.append(message)
    #print chat_cache

def get_latest_chat_message():
    message = chat_cache[-10:]
    #print message
    return message

def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
