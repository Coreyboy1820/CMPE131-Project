from flask import Flask, request, render_template
from datetime import date
from app import db, Session, todoItem, todoList

app = Flask(__name__)

@app.route('/add_todo_item', methods=['POST'])
def add_todo_item():
    # retrieve the form data
    priority = request.form['priority']
    start_date = request.form['start-date']
    due_date = request.form['due-date']
    status = request.form['status']
    list_id = request.form['list-id']

    # create a new todoItem instance
    new_item = todoItem(priority=priority, startDate=start_date, dueDate=due_date, status=status)

    # retrieve the todoList instance to add the todoItem to
    session = Session()
    todo_list = session.query(todoList).filter_by(userId=1, id=list_id).first()

    # add the new todoItem to the todoList
    todo_list.todoItems.append(new_item)

    # commit the changes to the database session
    session.commit()

    # render a success message to the user
    return render_template('add_todo_item_success.html')