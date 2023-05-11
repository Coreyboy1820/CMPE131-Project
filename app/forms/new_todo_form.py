from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired


class NewTodoForm(FlaskForm):
    todoListId = IntegerField('todoListId', validators=[DataRequired()])
    itemName = StringField('Name', validators=[DataRequired()])
    newItemPriority = SelectField('Priority', choices=[('1', 'High'), ('2', 'Medium'), ('3', 'Low')])
    startDate = DateField('Start Date', validators=[DataRequired()])
    dueDate = DateField('Due Date', validators=[DataRequired()])
    submitItem = SubmitField('Add Item', render_kw={"style": "background-color: #76a2d1; height: 38px; color: white; border-radius: 5px; ", "class":"btn btn-secondary"})

class UpdateTodoListForm(FlaskForm):
    updateTodoListId = IntegerField('todoListId', validators=[DataRequired()])
    listName = StringField('Name', validators=[DataRequired()])
    listSubmitted = BooleanField("submited")

class NewTodoListForm(FlaskForm):
    listName = StringField('Name', validators=[DataRequired()])
    submitList = SubmitField('Create List', render_kw={"style": "background-color: #76a2d1; height: 38px; color: white; border-radius: 5px; ", "class":"btn btn-secondary"})

class UpdateTodoItemForm(FlaskForm):
    todoItemId = IntegerField('todoListId', validators=[DataRequired()])
    itemName = StringField('Name', validators=[DataRequired()])
    updateItemPriority = SelectField('Priority', choices=[('1', 'High'), ('2', 'Medium'), ('3', 'Low')])
    startDate = DateField('Start Date', validators=[DataRequired()])
    dueDate = DateField('Due Date', validators=[DataRequired()])
    status = BooleanField("Status")
    itemSubmitted = BooleanField("submited")

class DeleteTodoItemForm(FlaskForm):
    deleteTodoItemId = IntegerField('deleteTodoItemId', validators=[DataRequired()])
    deleteItem = SubmitField('Delete Item')

class DeleteTodoListForm(FlaskForm):
    deleteTodoListId = IntegerField('deleteTodoListId', validators=[DataRequired()])
    deleteList = SubmitField('Delete List')