from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,  Length, Regexp, EqualTo, Email
from app import models
from flask import flash

class RegisterForm(FlaskForm):
      email = StringField('Email', validators=[DataRequired(), Email()])  

      # the text input that takes password input from user. Required
      password = PasswordField('Password', validators=[DataRequired(),  Length(min=1, max=8),  Regexp(r'.*[0-9].*', message='Password must contain at least one digit between 0-9')])

      # the text input that allows user to type their password again. Required. Input must be the same as the input of password
      confirmPassword = PasswordField('Confirm Password', validators=[
        DataRequired(), Length(min=1, max=8), EqualTo('password', message='Passwords must match')])
      
      # submit button
      submit = SubmitField('Register')

class RegisterFunction():
      # if the email already existed, we won't let user to register, and check if the password and confirm password are the same
      def validate(userEmail, userPassword, userConfirmPassword):
          dbSession = models.Session()
          # check if the userEmail existed in the database
          if dbSession.query(models.user).filter_by(email=userEmail).first() is not None:
              flash('Email is already registered', category='error')
              return False

          if userPassword != userConfirmPassword:
              flash('The password confirmation does not match', category='error')
              return False

          if len(userPassword) > 8:
              flash('The password must not exceed 8 characters', category='error')
              return False

          return True