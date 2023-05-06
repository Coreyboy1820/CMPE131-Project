from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class RemoveTodoItemForm(FlaskForm):
    todo_id = IntegerField('Todo ID', validators=[DataRequired()])
    submit = SubmitField('Remove')

class UpdateContactForm(FlaskForm):
    contact_id = IntegerField('Contact ID', validators=[DataRequired()])
    nickname = StringField('Nickname', validators=[DataRequired()])
    submitted = BooleanField('Submitted')

class SendMessageForm(FlaskForm):
    submit = SubmitField('Send Message')
    contact_id = IntegerField('Contact ID', validators=[DataRequired()])
