from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo
from app import models
from flask import redirect, url_for, session
import functools
from werkzeug.security import check_password_hash


class ChangeCredentialForm(FlaskForm):
    newEmail = StringField('New Email')
    newPassword = PasswordField('New Password')
    confirmNewPassword = PasswordField('Confirm New Password', 
                                    validators=[EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Submit')
