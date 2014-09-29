# chart3/app/models.py

import datetime
from flask import g, session
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

@app.before_request
def before_request():
    #print ('open database active!')
    g.db = db
    g.db.connect()


@app.after_request
def after_request(response):
    #print ('close database active!')
    g.db.close()
    return response

def add_a_chat_message(message):
    global chat_cache
    message.append(get_time())
    chat_cache.append(message)
    #print chat_cache
    if len(chat_cache)>=40:
        #delete some message so that the memory wont explode.
        print ('message trigger limit msg. clean up!')
        for i in range(10):
            chat_cache.pop(0)
        print('clean up done.. now chat_cache length: ' + str(len(chat_cache)))
    user = None
    if session.get('logged_in'):
        user = User.get(User.id == session.get('user_id'))
    msg = Message.create(user=user, content=message[0], send_time=datetime.datetime.now())

def get_latest_chat_message():
    global chat_cache
    if len(chat_cache) == 0:
        #query from database to acheive message
        for msg in Message.select().order_by(Message.send_time).limit(20):
            chat_cache.append([msg.content, msg.user.username, msg.send_time.strftime("%Y-%m-%d %H:%M:%S")])
    message = chat_cache[-10:]

    #print message
    return message


def get_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
