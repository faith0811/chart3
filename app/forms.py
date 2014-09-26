# chart3/app/forms.py

from flask.ext.wtf import Form
from wtforms.fields import TextField
from wtforms.validators import Required, Email

class EmailUsernameForm(Form):
    email = TextField('Email', validators=[Required(), Email()])
    username = TextField('Username', validators=[Required()])


class EmailForm(Form):
    email = TextField('Email', validators=[Required(), Email()])
