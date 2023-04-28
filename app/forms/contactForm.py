
from flask_wtf import FlaskForm
from wtforms import charField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from app import models
from flask import flash
  
# creating a form
class InputForm(forms.Form):
 
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Email= forms.CharField(max_length = 200)
    ContactId = forms.CharField(max_length = 200)
    Nickname = forms.CharField(max_length = 200)
  
  submit = SubmitField('AddContact')

class addContact():
def validate(userEmail):
          dbSession = models.Session()
          # check if the userEmail existed in the database
          if (dbSession.query(models.user).filter_by(email=userEmail).first() is None):
               return True
          else:
                  flash('Invalid Email')