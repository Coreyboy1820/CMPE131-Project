from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from app import models
from flask import redirect, url_for, session
import functools


class loginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class loginFunctions():

    def required_login(f):
        @functools.wraps(f)
        def decorate(*args, **kwargs):
            if not 'logged_in' in session:
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorate

    def validate_login(user):
        dbSession = models.Session()
        dbUser = dbSession.query(models.user).filter_by(email=user.email.data).all()
        dbSession.close()
        print(dbSession.is_active)
        # Perform hashing function here
        if dbUser:
            if (user.password.data == dbUser[0].passwordHash):
                return True
        return False
