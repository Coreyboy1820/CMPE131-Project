from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from app import models
from flask import flash

class RegisterForm(FlaskForm):
      # the text input that takes email input from user. Required Field. Must be a valid email
       # pip install email_validator or  # pip3 install email_validator (need to install email_validator package so that flask can validate the email type)
      email = StringField('Email', validators=[DataRequired(), Email()])  
     



      # the text input that takes password input from user. Required
      password = PasswordField('Password', validators=[DataRequired()])


      # the text input that allows user to type their password again. Required. Input must be the same as the input of password
      confirmPassword = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')])
      
      
      # submit button
      submit = SubmitField('Register')

class RegisterFunction():
      # if the email already existed, we won't let user to register, and check if the password and confirm password are the same
      def validate(userEmail, userPassword, userConfirmPassword):
          dbSession = models.Session()
          # check if the userEmail existed in the database
          if (dbSession.query(models.user).filter_by(email=userEmail).first() is None and userPassword == userConfirmPassword):
               return True
          if (dbSession.query(models.user).filter_by(email=userEmail).first() is not None):
               flash('Email is already registered', category='error')
          else:
               flash('The password confirmation does not match', category='error')
          return False
               
