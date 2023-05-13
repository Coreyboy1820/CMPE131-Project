from flask_wtf import FlaskForm
from wtforms import BooleanField

class DarkModeForm(FlaskForm):
    toggleMode = BooleanField("Toggle Dark Mode")