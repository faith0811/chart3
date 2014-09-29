# chart3/app/views.py

import datetime
from . import app
from flask import render_template, request, redirect, url_for, session, flash
from forms import EmailForm, EmailUsernameForm
from models import User,db
from functools import wraps


def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('sign_in'))
        return f(*args, **kwargs)
    return inner

def not_login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if session.get('logged_in'):
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return inner

@app.route('/')
def index():
    logged = session.get('logged_in')
    username = 'guest'
    if logged:
        username = session.get('username')
    return render_template("index.html", logged=logged, username=username, sign_in_url=url_for('sign_in'), sign_out_url=url_for('sign_out'), reg_url=url_for('reg'))


@app.route('/chart')
@login_required
def chart():
    return render_template("chart.html", username=session.get('username'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/signin', methods=['GET', 'POST'])
@not_login_required
def sign_in():
    form = EmailForm()
    if form.validate_on_submit():
        email = form.email.data
        try:
            user = User.get(email=email)
        except User.DoesNotExist:
            #print ('errorrrrrrr!')
            return render_template('sign_in.html', form=form, login_error=True, reg_url=url_for('reg'))
        else:
            log_user(user)
            return redirect(url_for('index'))
    return render_template('sign_in.html', form=form, login_error=False, reg_url=url_for('reg'))


@app.route('/register', methods=['GET', 'POST'])
@not_login_required
def reg():
    form = EmailUsernameForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        try:
            with db.transaction():
                user = User.create(email=email, username=username, join_date=datetime.datetime.now())
            log_user(user)
            return redirect(url_for('index'))
        except:
            return render_template('register.html', form=form, existed_error=True)
            #print ('failed.')
    return render_template('register.html', form=form, existed_error=False)

@app.route('/signout')
@login_required
def sign_out():
    session.pop('logged_in',None)
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


def log_user(user):
    session['logged_in'] = True
    session['user_id'] = user.id
    session['username'] = user.username

