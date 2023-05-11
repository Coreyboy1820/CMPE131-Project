from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo
from app import models
from flask import redirect, url_for, session, flash
import functools
from werkzeug.security import check_password_hash


class ChangeCredentialForm(FlaskForm):
    newEmail = StringField('New Email')
    newPassword = PasswordField('New Password')
    confirmNewPassword = PasswordField('Confirm New Password', 
                                    validators=[EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Submit', render_kw={"style": "background-color: #76a2d1; height: 38px; color: white; border-radius: 5px; ", "class":"btn btn-secondary"})

class ChangeCredentialFunctions():
    def validate(self, newUserEmail, newUserPassword, newUserConfirmPassword):
        dbSession = models.Session()
        email_from_db = dbSession.query(models.user).filter_by(email=newUserEmail).first()
        dbSession.close()
        if (newUserEmail != None and newUserEmail != ""):
            if (email_from_db is not None):
                flash('Email is already registered', category='error')
                return False
            elif (not any(char.isdigit() for char in newUserEmail)):
                flash("Email must contain at least one number",category='error')
                return False
            elif (len(newUserEmail) < 6):
                flash("Username must have at least 6 characters", category='error')
                return False
            flash('Username successfully changed')
        if (newUserPassword != None and newUserConfirmPassword != None):
            if (not any(char.isdigit() for char in newUserPassword)):
                flash("Password must contain at least one number",category='error')
                return False
            elif (len(newUserPassword) < 6):
                flash("Password must have at least 6 characters", category='error')
                return False
            elif (newUserPassword != newUserConfirmPassword):
                flash('The password confirmation does not match', category='error')
                return False
            flash('Password successfully changed')
        return True
         
         