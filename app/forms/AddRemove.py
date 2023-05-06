from flask import render_template, redirect, url_for
from app import app, db
from app.forms import AddTodoItemForm, RemoveTodoItemForm, UpdateContactForm, SendMessageForm
from app.models import TodoItem, Contact


@app.route('/', methods=['GET', 'POST'])
def index():
    add_form = AddTodoItemForm()
    remove_form = RemoveTodoItemForm()
    if add_form.validate_on_submit():
        todo_item = TodoItem(todo=add_form.todo.data)
        db.session.add(todo_item)
        db.session.commit()
        return redirect(url_for('index'))
    if remove_form.validate_on_submit():
        todo_item = TodoItem.query.get(remove_form.todo_id.data)
        if todo_item:
            db.session.delete(todo_item)
            db.session.commit()
        return redirect(url_for('index'))
    todo_items = TodoItem.query.all()
    return render_template('index.html', todo_items=todo_items, add_form=add_form, remove_form=remove_form)


@app.route('/updateContact/<int:contact_id>', methods=['GET', 'POST'])
def update_contact(contact_id):
    form = UpdateContactForm()
    contact = Contact.query.get(contact_id)
    if form.validate_on_submit():
        contact.nickname = form.nickname.data
        contact.submitted = form.submitted.data
        db.session.commit()
        return redirect(url_for('index'))
    form.contact_id.data = contact.id
    form.nickname.data = contact.nickname
    form.submitted.data = contact.submitted
    return render_template('update_contact.html', form=form, contact=contact)


@app.route('/sendMessage/<int:contact_id>', methods=['GET', 'POST'])
def send_message(contact_id):
    form = SendMessageForm()
    if form.validate_on_submit():
        # code for sending message
        return redirect(url_for('index'))
    form.contact_id.data = contact_id
    return render_template('send_message.html', form=form)