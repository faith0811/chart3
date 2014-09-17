# chart3/app/views.py

from . import app
from flask import render_template
from model import get_latest_chat_message

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chart')
def chart():
    message = get_latest_chat_message()
    return render_template("chart.html", message=message)

@app.route('/about')
def about():
    return render_template('about.html')
