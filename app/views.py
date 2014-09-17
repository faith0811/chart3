# chart3/app/views.py

from flask import render_template
from flask.ext.login import login_required, current_user


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chart')
@login_required
def chart():
    return render_template("chart.html")

@app.route('/about')
def about():
    return render_template('about.html')

