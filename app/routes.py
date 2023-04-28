from app import myapp_obj, models
from flask import render_template, redirect, url_for, request, flash, session
from app.forms import registerForm, login_page, change_credential_form, new_todo_form
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash # for password hashing


@myapp_obj.route("/")
@myapp_obj.route("/home")
@login_page.loginFunctions.required_login
def to_home():
    return render_template('home.html')




@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    loginform = login_page.loginForm()
    if(request.method == 'POST'):
        valid_login, userId = login_page.loginFunctions.validate_login(loginform)
        if loginform.validate_on_submit() & valid_login:
            session['logged_in'] = True
            session['email'] = loginform.email.data
            session['userId'] = userId
            return redirect(url_for('emails'))
    return render_template('login.html', title="login", form=loginform)



@myapp_obj.route("/register",methods=['GET', 'POST'])
def register():
    register = registerForm.RegisterForm()
    if (request.method == 'POST'):
        if registerForm.RegisterFunction.validate(register.email.data, register.password.data, register.confirmPassword.data):
            flash('You have successfully registered')

            dbSession = models.Session()
            new_user = models.user(email=register.email.data, passwordHash= generate_password_hash(register.password.data))
            dbSession.add(new_user)
            dbSession.commit()
            return redirect(url_for('login'))
       
    return render_template('register.html', title="register", form=register)




@myapp_obj.route("/todo", methods=['GET', 'POST'])
@login_page.loginFunctions.required_login
def todo():
    new_todo_list_form = new_todo_form.NewTodoListForm()
    new_todo_item_form = new_todo_form.NewTodoForm()
    if request.method == 'POST':
        if new_todo_list_form.name.data != "":
            
            # create a new todoItem instance
            new_todo_list = models.todoList(name=new_todo_list_form.name.data, userId=session['userId'])

            # retrieve the todoList instance to add the todoItem to
            dbSession = models.Session()

            dbSession.add(new_todo_list)

            # commit the changes to the database session
            dbSession.commit()
            dbSession.close()
        if new_todo_item_form.priority.data:
        
            # create a new todoItem instance
            new_todo_item = models.todoItem(todoListId=new_todo_item_form.todoListId.data, priority=new_todo_item_form.priority.data, startDate=new_todo_item_form.startDate.data, dueDate=new_todo_item_form.dueDate.data, status=new_todo_item_form.status.data)

            # retrieve the todoList instance to add the todoItem to
            dbSession = models.Session()

            dbSession.add(new_todo_item)

            # commit the changes to the database session
            dbSession.commit()
            dbSession.close()

    return render_template('todo.html', title="todo", todo_list_form=new_todo_list_form, todo_item_form=new_todo_item_form)





@myapp_obj.route("/emails",methods=['GET', 'POST'])
@login_page.loginFunctions.required_login
def emails():
    if request.method == 'POST':
        dbSession = models.Session()
        currentUserEmail = session.get('email')  # this session is imported from flask
        # check if data is send to the server succesfully
        if 'to' and 'subject' and 'body' in request.form:
            to = request.form['to']
            # if the recepient is valid
            if(dbSession.query(models.user).filter_by(email=to).first() is not None):
                subject = request.form['subject']
                body = request.form['body']
                current_date = date.today()
                # print(dbSession.query(models.user).filter_by(email=currentUserEmail).first().id )
                lastMessageId = dbSession.query(models.message).order_by(models.message.id.desc()).first().id
                message = models.message(id=lastMessageId+1, senderId= dbSession.query(models.user).filter_by(email=currentUserEmail).first().id ,message= body, sentDate= current_date, recievedDate = current_date, subject= subject )
                dbSession.add(message)
                dbSession.commit()
                dbSession.close()
                flash('Message is sent successfully')
            else:
                flash('Recipient not found',category='error')
        else:
            flash('Message is not sent',category='error')
    return render_template('emails.html', title="emails")


@myapp_obj.route("/delete", methods=['GET', 'POST'])
@login_page.loginFunctions.required_login
def delete():
    currentUserEmail = session.get('email') 
   
    if request.method == 'POST':
        dbSession = models.Session()
        if (check_password_hash(dbSession.query(models.user).filter_by(email= currentUserEmail).first().passwordHash, request.form['password'])):
              deletedUser = dbSession.query(models.user).filter_by(email = currentUserEmail).first()
              deletedUser.active = False
              dbSession.commit()
              return redirect(url_for('login'))
        else:
            print('Password is incorrect')
    return render_template('delete.html', userEmail = currentUserEmail)


@myapp_obj.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

@myapp_obj.route("/settings", methods=["POST", "GET"])
@login_page.loginFunctions.required_login
def settings():
    credential_Form = change_credential_form.ChangeCredentialForm()
    if registerForm.RegisterFunction.validate(credential_Form.newEmail.data, credential_Form.newPassword.data, credential_Form.confirmNewPassword.data) & (request.method == 'POST'):
        dbSession = models.Session()
        user = dbSession.query(models.user).filter_by(id=session['userId']).first()
        if credential_Form.newEmail.data != "":
            user.email = credential_Form.newEmail.data
        if credential_Form.newPassword.data != "":
            user.passwordHash = generate_password_hash(credential_Form.newPassword.data)
        dbSession.commit()
    return render_template('settings.html', title="settings", credential_Form=credential_Form)

@myapp_obj.route('/add_todo_item', methods=['POST'])
def add_todo_item():
    # retrieve the form data
    priority = request.form['priority']
    start_date = request.form['start-date']
    due_date = request.form['due-date']
    status = request.form['status']
    list_id = request.form['list-id']

    # create a new todoItem instance
    new_item = models.todoItem(priority=priority, startDate=start_date, dueDate=due_date, status=status)

    # retrieve the todoList instance to add the todoItem to
    dbSession = models.Session()
    todo_list = dbSession.query(models.todoList).filter_by(userId=1, id=list_id).first()

    # add the new todoItem to the todoList
    todo_list.todoItems.append(new_item)

    # commit the changes to the database session
    dbSession.commit()

    # render a success message to the user
    return render_template('add_todo_item_success.html')