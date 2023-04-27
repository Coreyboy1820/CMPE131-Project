from datetime import date
from app import db, Session, todoItem, todoList

# create a new todoItem instance
new_item = todoItem(priority=1, startDate=date.today(), dueDate=date(2023, 5, 31), status=False)

# retrieve the todoList instance to add the todoItem to
session = Session()
todo_list = session.query(todoList).filter_by(userId=1, id=2).first()

# add the new todoItem to the todoList
todo_list.todoItems.append(new_item)

# commit the changes to the database session
session.commit()
