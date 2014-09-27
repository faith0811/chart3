# chart3/app/views.py

from . import app
from flask import render_template, request, redirect, url_for
from forms import EmailForm


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chart')
def chart():
    user_id = request.cookies.get('user_id')
    if (user_id == None):
        return redirect(url_for('login'))
    return render_template("chart.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = EmailForm()
    if form.validate_on_submit():
        email = form.email.data
        #should be fulfilled later
        #here to comfirm the user input
    return render_template('sign_in.html', email_wrong=False, form=form)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
