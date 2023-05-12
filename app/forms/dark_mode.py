from flask_wtf import FlaskForm
from wtforms import SubmitField

class DarkModeForm(FlaskForm):
    toggleMode = SubmitField("Toggle Dark Mode")