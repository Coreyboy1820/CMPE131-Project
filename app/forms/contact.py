from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class updateContact(FlaskForm):
    nickName = StringField('Name', validators=[DataRequired()])
    submitted = BooleanField('Submitted')