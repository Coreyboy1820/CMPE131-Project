from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField

class DarkModeForm(FlaskForm):
    toggleMode = BooleanField("Toggle Dark Mode")
    submitDarkMode = SubmitField("Submit")