from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email

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
