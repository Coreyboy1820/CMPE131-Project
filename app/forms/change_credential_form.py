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
    def validate(self,newUserEmail, newUserPassword, newUserConfirmPassword):
        dbSession = models.Session()
        if (newUserEmail != None):
            if (dbSession.query(models.user).filter_by(email=newUserEmail).first() is not None):
                flash('Email is already registered', category='error')
                return False
            elif (not any(char.isdigit() for char in newUserEmail)):
                flash("Email must contain at least one number",category='error')
                return False
            elif ((len(newUserEmail) > 25 or len(newUserEmail) < 6)):
                if (len(newUserEmail) > 25):
                    flash("Too much characters",category='error')
                    return False
                else:
                    flash("Username must have at least 6 characters", category='error')
                    return False
        if (newUserPassword != None and newUserConfirmPassword != None):
            if (not any(char.isdigit() for char in newUserPassword)):
                flash("Password must contain at least one number",category='error')
                return False
            elif (len(newUserPassword) > 25 or len(newUserPassword) < 6):
                if (len(newUserPassword) > 25):
                        flash("Too much characters",category='error')
                        return False
                else:
                        flash("Password must have at least 6 characters", category='error')
                        return False
            elif (newUserPassword != newUserConfirmPassword):
                flash('The password confirmation does not match', category='error')
                return False
        flash('Change credential successfully')
        return True
         
         