# chart3/app/views.py

from . import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chart')
def chart():
    return render_template("chart.html")

@app.route('/about')
def about():
    return render_template('about.html')
