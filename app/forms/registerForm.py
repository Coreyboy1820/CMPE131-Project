from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length, NumberRange
from app import models
from flask import flash

class RegisterForm(FlaskForm):
      email = StringField('Email', validators=[DataRequired(), Email(), Length(min=5, max=30), NumberRange(min=0, max=9999)])  

      # the text input that takes password input from user. Required
      password = PasswordField('Password', validators=[DataRequired(), NumberRange(min=0, max=9999), Length(min=5, max=30)])

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
          if (dbSession.query(models.user).filter_by(email=userEmail).first() is not None):
               flash('Email is already registered', category='error')
               return False
          
          # check if useremail is inputted
          elif (userEmail == ""):
               flash("Email is required", category='error')
               return False
          
          # check if useremail contains number
          elif (not any(char.isdigit() for char in userEmail)):
               flash("Email must contain at least one number",category='error')
               return False
          
          # check if useremail is in the allowed range of chars
          elif (len(userEmail) > 25 or len(userEmail) < 6):
               if (len(userEmail) > 25):
                    flash("Too much characters",category='error')
                    return False
               else:
                    flash("Username must have at least 6 characters", category='error')
                    return False
               
          # check if password is inputted
          elif (userPassword == ""):
               flash("Password is required", category='error')
               return False
          
          # check if password is the allowed range of chars
          elif (len(userPassword) > 25 or len(userPassword) < 6):
               if (len(userPassword) > 25):
                    flash("Too much characters",category='error')
                    return False
               else:
                    flash("Password must have at least 6 characters", category='error')
                    return False
               
          # check if password contains number
          elif (not any(char.isdigit() for char in userPassword)):
               flash("Password must contain at least one number",category='error')
               return False
          
          # check if confirmation password matches with inputted password 
          elif (userPassword != userConfirmPassword):
                    flash('The password confirmation does not match', category='error')
                    return False
          else: 
                return True
          
          # # check if the userEmail existed in the database
          # if (dbSession.query(models.user).filter_by(email=userEmail).first() is None and userPassword == userConfirmPassword):
          #      return True
               
