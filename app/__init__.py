# chart3/app/__init__.py

from gevent import monkey
monkey.patch_all()
from flask import Flask
from flask.ext.socketio import SocketIO


app = Flask(__name__)
app.config.from_object('config')


socketio = SocketIO(app)

import sockets
import views
