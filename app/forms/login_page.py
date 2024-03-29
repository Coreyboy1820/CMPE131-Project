from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from app import models
from flask import redirect, url_for, session, flash
import functools
from werkzeug.security import check_password_hash


class loginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class loginFunctions():

# this function is a decorator which is meant to check if the logged in variable exists, and if it is then the other end points are accessible.
    def required_login(f):
        @functools.wraps(f)
        def decorate(*args, **kwargs):
            if not 'logged_in' in session:
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorate

    def validate_login(user):
        dbSession = models.Session()
        dbUser = dbSession.query(models.user).filter_by(email=user.email.data).first()
        dbSession.close()
        # Perform hashing function here
        if dbUser:
            if (check_password_hash(dbUser.passwordHash, user.password.data) and dbUser.active):
                flash("Login successfully!")
                return True, dbUser
            else:
                flash("Password is incorrect",category='error')
        else:
            flash("Email is not registered",category='error')
        return False, dbUser
