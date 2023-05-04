from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class updateContact(FlaskForm):
    contactId = IntegerField('Contact Id', validators=[DataRequired()])
    nickName = StringField('Name', validators=[DataRequired()])
    submitted = BooleanField('Submitted')

class sendMessage(FlaskForm):
    submit = SubmitField("Send Message")
    contactId = IntegerField('Contact Id', validators=[DataRequired()])