from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class NewTodoForm(FlaskForm):
    todoListId = IntegerField('todoListId', validators=[DataRequired()])
    priority = IntegerField('Priority Level', validators=[DataRequired()])
    startDate = DateField('Start Date', validators=[DataRequired()])
    dueDate = DateField('Due Date', validators=[DataRequired()])
    status = BooleanField('status', validators=[DataRequired()])
    submit = SubmitField('Add Item')

class NewTodoListForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Create List')