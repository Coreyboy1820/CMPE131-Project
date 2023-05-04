from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class NewTodoForm(FlaskForm):
    todoListId = IntegerField('todoListId', validators=[DataRequired()])
    itemName = StringField('Name', validators=[DataRequired()])
    priority = IntegerField('Priority Level', validators=[DataRequired()])
    startDate = DateField('Start Date', validators=[DataRequired()])
    dueDate = DateField('Due Date', validators=[DataRequired()])
    submitItem = SubmitField('Add Item')

class NewTodoListForm(FlaskForm):
    listName = StringField('Name', validators=[DataRequired()])
    submitList = SubmitField('Create List')