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
            dbSession = models.Session()
            new_user = models.user(email=register.email.data, passwordHash= generate_password_hash(register.password.data))
            dbSession.add(new_user)
            dbSession.commit()
            flash('You have successfully registered', category="success")
            return redirect(url_for('login'))
       
    return render_template('register.html', title="register", form=register)




@myapp_obj.route("/todo", methods=['GET', 'POST'])
@login_page.loginFunctions.required_login
def todo():
    new_todo_list_form = new_todo_form.NewTodoListForm()
    new_todo_item_form = new_todo_form.NewTodoForm()
    dbSession = models.Session()
    if request.method == 'POST':
        if new_todo_list_form.submitList.data:
            
            # create a new todoItem instance
            lastListId = dbSession.query(models.todoList).order_by(models.todoList.id.desc()).first().id
            new_todo_list = models.todoList(id=lastListId+1, name=new_todo_list_form.listName.data, userId=session['userId'])

            # retrieve the todoList instance to add the todoItem to

            dbSession.add(new_todo_list)

            # commit the changes to the database session
            dbSession.commit()
            dbSession.close()
            flash('List was added successfully', category="success")
            return redirect(url_for("todo"))
        if new_todo_item_form.submitItem.data:
            startDate = new_todo_item_form.startDate.data
            dueDate = new_todo_item_form.dueDate.data
            if (startDate <= dueDate):
                # create a new todoItem instance
                lastItemeId = dbSession.query(models.todoItem).order_by(models.todoItem.id.desc()).first().id
                new_todo_item = models.todoItem(id=lastItemeId+1, todoListId=new_todo_item_form.todoListId.data, name=new_todo_item_form.itemName.data, priority=new_todo_item_form.priority.data, 
                                                startDate=startDate, dueDate=dueDate)

                # retrieve the todoList instance to add the todoItem to

                dbSession.add(new_todo_item)

                # commit the changes to the database session
                dbSession.commit()
                dbSession.close()
                flash('Item was added successfully', category="success")
            else:
                flash('Start date must be before the Due Date',category="error")
            return redirect(url_for("todo"))
    todo_lists= dbSession.query(models.todoList).filter_by(userId=session['userId']).all()
    dbSession.close()
    return render_template('todo.html', title="todo", todo_list_form=new_todo_list_form, todo_item_form=new_todo_item_form, todo_lists = todo_lists)





@myapp_obj.route("/emails",methods=['GET', 'POST'])
@login_page.loginFunctions.required_login
def emails():
    currentUserEmail = session.get('email') # this session is imported from flask
    dbSession = models.Session()
    if request.method == 'POST':
        # check if data is send to the server succesfully
        if 'to' and 'subject' and 'body' in request.form:
            receipients = request.form['to'].split(" ")
            for to in receipients:
                # if the recepient is valid
                userTo= dbSession.query(models.user).filter_by(email=to).first()
                if(userTo is not None):
                    subject = request.form['subject']
                    body = request.form['body']
                    current_date = date.today()
                    lastMessageId = dbSession.query(models.message).order_by(models.message.id.desc()).first().id
                    messageId = lastMessageId+1
                    message = models.message(id=messageId, senderId= dbSession.query(models.user).filter_by(email=currentUserEmail).first().id ,message= body, sentDate= current_date, recievedDate = current_date, subject= subject)
                    lastreceipientId = dbSession.query(models.recipient).order_by(models.recipient.id.desc()).first().id
                    receipientId = lastreceipientId+1
                    receipient = models.recipient(id= receipientId ,userId= userTo.id, messageId=messageId)
                    dbSession.add(receipient)
                    dbSession.add(message)
                    dbSession.commit()
                    dbSession.close()
                    flash('Message was sent successfully', category="success")
                    return redirect(url_for("emails"))
                else:
                    flash('Recipient not found',category='error')
        else:
            flash('Message was not sent',category='error')
    messages = dbSession.query(models.message).all()
    dbSession.close()
    receivedEmails = []
    for message in messages:
        for receipient in message.recipients:
            if (session.get('userId') == receipient.user.id):
                receivedEmails.append(message)
    return render_template('emails.html', title="emails", receivedEmails= receivedEmails)


@myapp_obj.route("/delete", methods=['GET', 'POST'])
@login_page.loginFunctions.required_login
def delete():
    currentUserEmail = session.get('email') 
   
    if request.method == 'POST':
        dbSession = models.Session()
        if (check_password_hash(dbSession.query(models.user).filter_by(email= currentUserEmail).first().passwordHash, request.form['password'])):
              deletedUser = dbSession.query(models.user).filter_by(email = currentUserEmail).first()
              deletedUser.active = False
              deletedUser.email = "DeletedUser" + str(deletedUser.id) + "@gmailclone.com"
              (deletedUser.email)
              dbSession.commit()
              flash("Your account has been deleted", category="success")
              return redirect(url_for('login'))
        else:
            flash("password is incorrect", category="error")
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

@myapp_obj.route("/addContact", methods=["POST", "GET"])
@login_page.loginFunctions.required_login
def addContact():
    if request.method == 'POST':
        dbSession = models.Session()
        addedUserEmail = request.form['email'] # verified
        addedUserNickname = request.form['name'] # verified
        addedUser = dbSession.query(models.user).filter_by(email=addedUserEmail).first()
        if addedUser is not None:  # verified
            contact = dbSession.query(models.userContact).filter_by(userId=session["userId"], contactId=addedUser.id).first()
            if contact is None:
                cid=dbSession.query(models.userContact).order_by(models.userContact.id.desc()).first().id
                newContact = models.userContact(id=cid+1, userId=session["userId"], contactId=addedUser.id, nickName=addedUserNickname) # verified
                dbSession.add(newContact)
                dbSession.commit()
                flash("User has been added succesfully", category="success")
            else:
                flash("Contact already exists", category="error")
        else:
            flash("User does not exist", category="error")
        dbSession.close()

        
    return render_template('addContact.html')
