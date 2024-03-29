from app import myapp_obj, models
from flask import render_template, redirect, url_for, request, flash, session
from app.forms import registerForm, login_page, change_credential_form, new_todo_form, contact, dark_mode
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash # for password hashing


@myapp_obj.route("/")
@myapp_obj.route("/home", methods=['GET', 'POST'])
@login_page.loginFunctions.required_login
def home():
    

    update_contact_form = contact.updateContact()
    send_message = contact.sendMessage()
    dark_mode_form = dark_mode.DarkModeForm()
    dbSession = models.Session()
    
    
    
    if(request.method == "POST"):
        if ('isdelete' in request.form):
            deletedContactId = request.form['deletedUserContactId']
            deletedContact = dbSession.query(models.userContact).filter_by(id=deletedContactId).first()
            dbSession.delete(deletedContact)
            dbSession.commit()
            dbSession.close()
        else:
            if update_contact_form.submitted.data:
                contact_update = dbSession.query(models.userContact).filter_by(id=update_contact_form.contactId.data).first()
                contact_update.nickName = update_contact_form.nickName.data
                dbSession.commit()
                dbSession.close()
                return redirect(url_for('home'))
            if send_message.submit.data:
                contact_to_message = dbSession.query(models.user).filter_by(id=send_message.contactId.data).first()
                dbSession.close()
                return redirect(url_for('emails', contact_email = contact_to_message.email))
            
    usersContacts = dbSession.query(models.userContact).filter_by(userId=session["userId"]).order_by(models.userContact.nickName).all()   
    return render_template('home.html', title="Home", users_contacts = usersContacts, update_contact = update_contact_form, message_contact = send_message, dark_mode=session["darkMode"], dark_form = dark_mode_form)



# validates the user exists, logs in, then redirects to emails
@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    loginform = login_page.loginForm()
    if(request.method == 'POST'):
        valid_login, dbUser = login_page.loginFunctions.validate_login(loginform)
        if loginform.validate_on_submit() & valid_login:
            session['logged_in'] = True             # Session variable can be accessed at any time and only has data pertaining to the user currently using the app
            session['email'] = loginform.email.data
            session['userId'] = dbUser.id
            session["darkMode"] = dbUser.darkMode
            return redirect(url_for('emails'))
    return render_template('login.html', title="login", form=loginform)


# inserts new user and redirects to login
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



# Inserts new todo item or list then displays todo items on the front end
@myapp_obj.route("/todo", methods=['GET', 'POST'])
@login_page.loginFunctions.required_login
def todo():

    new_todo_list_form = new_todo_form.NewTodoListForm()
    new_todo_item_form = new_todo_form.NewTodoForm()
    update_todo_item_form = new_todo_form.UpdateTodoItemForm()
    update_todo_list_form = new_todo_form.UpdateTodoListForm()
    delete_todo_item_form = new_todo_form.DeleteTodoItemForm()
    delete_todo_list_form = new_todo_form.DeleteTodoListForm()
    dark_mode_form = dark_mode.DarkModeForm()

    dbSession = models.Session()
    if request.method == 'POST':
        if new_todo_list_form.submitList.data:          # If the new todo list form was submitted then add it to the database
            
            # create a new todoItem instance
            # We had to use this method instead of autoincrement because the database wasn't autoincrementing for us and this was the next best method.
            # We take the last elements id then increment it by 1
            lastListId = dbSession.query(models.todoList).order_by(models.todoList.id.desc()).first().id
            new_todo_list = models.todoList(id=lastListId+1, name=new_todo_list_form.listName.data, userId=session['userId'])

            # retrieve the todoList instance to add the todoItem to

            dbSession.add(new_todo_list)

            # commit the changes to the database session
            dbSession.commit()
            dbSession.close()
            flash('List was added successfully', category="success")
            return redirect(url_for("todo"))
        
        if new_todo_item_form.submitItem.data:         # If the new todo Item form was submitted then add it to the database
            startDate = new_todo_item_form.startDate.data
            dueDate = new_todo_item_form.dueDate.data

            if (startDate <= dueDate):
                # create a new todoItem instance
                lastItemId = dbSession.query(models.todoItem).order_by(models.todoItem.id.desc()).first().id
                new_todo_item = models.todoItem(id=lastItemId+1, todoListId=new_todo_item_form.todoListId.data, name=new_todo_item_form.itemName.data, priority=new_todo_item_form.newItemPriority.data, 
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
        
        if update_todo_item_form.itemSubmitted.data:
            todoItem = dbSession.query(models.todoItem).filter_by(id=update_todo_item_form.todoItemId.data).first()
            todoItem.name = update_todo_item_form.itemName.data
            todoItem.priority = update_todo_item_form.updateItemPriority.data
            todoItem.status = update_todo_item_form.status.data
            if (update_todo_item_form.startDate.data <= update_todo_item_form.dueDate.data):
                todoItem.startDate = update_todo_item_form.startDate.data
                todoItem.dueDate = update_todo_item_form.dueDate.data
            else:
                flash('Start date must be before the Due Date', category="error")
            dbSession.commit()
            dbSession.close()
            return redirect(url_for("todo"))
        
        if update_todo_list_form.listSubmitted.data:
            todoList = dbSession.query(models.todoList).filter_by(id=update_todo_list_form.updateTodoListId.data).first()
            todoList.name = update_todo_list_form.listName.data
            dbSession.commit()
            dbSession.close()
            return redirect(url_for("todo"))
        
        if delete_todo_item_form.deleteItem.data:
            item_to_delete = dbSession.query(models.todoItem).filter_by(id=delete_todo_item_form.deleteTodoItemId.data).first()
            dbSession.delete(item_to_delete)
            dbSession.commit()
            dbSession.close()
            return redirect(url_for("todo"))
        
        if delete_todo_list_form.deleteList.data:
            list_to_delete = dbSession.query(models.todoList).filter_by(id=delete_todo_list_form.deleteTodoListId.data).first()
            for item in list_to_delete.todoItems:
                dbSession.delete(item)
            dbSession.delete(list_to_delete)
            dbSession.commit()
            dbSession.close()
            return redirect(url_for("todo"))
        

    todo_lists = dbSession.query(models.todoList).filter_by(userId=session['userId']).all()
    dbSession.close()
    return render_template('todo.html', title="todo", todo_list_form=new_todo_list_form, todo_item_form=new_todo_item_form, 
                           update_todo_form=update_todo_item_form, update_list_form = update_todo_list_form, todo_lists = todo_lists,
                           delete_todo_item = delete_todo_item_form, delete_todo_list = delete_todo_list_form, dark_mode=session["darkMode"], dark_form = dark_mode_form)




# Inserts new email and displays emails on the front end
@myapp_obj.route("/emails",methods=['GET', 'POST'])
@login_page.loginFunctions.required_login
def emails():
    dark_mode_form = dark_mode.DarkModeForm()
    currentUserId = session.get('userId') # this session is imported from flask
    dbSession = models.Session()
    contact_email = ""
    isUpdate = 'False'
    messageId =''
    if request.method == 'POST':

        # check if data is send to the server succesfully
        if 'to' and 'subject' and 'body' in request.form: # if the form was fully filled out
            # First split all users entered into a list
            receipients = request.form['to'].split(" ")
            # then iterate over that list
            dbSession.begin()
            for to in receipients:
                userTo= dbSession.query(models.user).filter_by(email=to).first()
                # if the recepient is valid
                if(userTo is not None):
                    lastMessageId = dbSession.query(models.message).order_by(models.message.id.desc()).first().id
                    messageId = lastMessageId+1
                    subject = request.form['subject']
                    body = request.form['body']
                    current_date = date.today()
                    message = models.message(id=messageId, senderId = currentUserId ,message= body, sentDate= current_date, recievedDate = current_date, subject= subject)
                    lastreceipientId = dbSession.query(models.recipient).order_by(models.recipient.id.desc()).first().id
                    dbSession.add(message)
                    # also have to add the recipient of the email to the recipient table
                    lastreceipientId = lastreceipientId+1
                    receipient = models.recipient(id = lastreceipientId ,userId= userTo.id, messageId=messageId)
                    dbSession.add(receipient)
                    flash('Message was sent successfully', category="success")
                
                else:
                    flash('Recipient not found',category='error')
            dbSession.commit()
            dbSession.close()
            return redirect(url_for("emails"))
        elif 'updateMessage' in request.form:
            isUpdate='True'
            messageId = request.form['email_id']
            message = dbSession.query(models.message).filter_by(id=messageId).first()
            message.new = False
            dbSession.commit()
            dbSession.close()
            
        # else:
        #     flash('Message was not sent',category='error')
        
    if request.method == 'GET':
        contact_email = request.args.get('contact_email', None)

    messages = dbSession.query(models.message).order_by(models.message.sentDate).all()
    dbSession.close()
    receivedEmails = []

    # this is where how we send the messages to the front end
    for message in messages:
        for receipient in message.recipients:
            if (session.get('userId') == receipient.user.id):               
                if message.new == True:
                    receivedEmails.insert(0, message)
                else:
                    receivedEmails.append(message)
    return render_template('emails.html', title="emails", receivedEmails= receivedEmails, contact_email=contact_email,  isUpdate= isUpdate, messageId = messageId, dark_mode=session["darkMode"], dark_form = dark_mode_form)



# verifies password is correct then deletes user
@myapp_obj.route("/delete", methods=['GET', 'POST'])
@login_page.loginFunctions.required_login
def delete():
    dark_mode_form = dark_mode.DarkModeForm()
    currentUserEmail = session.get('email') 

    if request.method == 'POST':
        dbSession = models.Session()
        if (check_password_hash(dbSession.query(models.user).filter_by(email= currentUserEmail).first().passwordHash, request.form['password'])):
              
            #   if the user gets deleted then replace the email with a username + the id so it will never be the same as anyone elses and that email address frees back up,
            #   This also prevents data from being lost when a user gets "deleted"
              deletedUser = dbSession.query(models.user).filter_by(email = currentUserEmail).first()
              deletedUser.active = False
              deletedUser.email = "DeletedUser" + str(deletedUser.id) + "@gmailclone.com"
              (deletedUser.email)
              dbSession.commit()
              flash("Your account has been deleted", category="success")
              return redirect(url_for('login'))
        else:
            flash("password is incorrect", category="error")
    return render_template('delete.html', userEmail = currentUserEmail, dark_mode=session["darkMode"], dark_form = dark_mode_form)

# Clears the current session to log out the user
@myapp_obj.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))


# changes credentials or redirects to delete
@myapp_obj.route("/settings", methods=["POST", "GET"])
@login_page.loginFunctions.required_login
def settings():
    credential_Form = change_credential_form.ChangeCredentialForm()
    credential_Function = change_credential_form.ChangeCredentialFunctions()
    dark_mode_form = dark_mode.DarkModeForm()
    if request.method == 'POST':
        if "newEmail" in request.form:
            if ( credential_Function.validate(credential_Form.newEmail.data, credential_Form.newPassword.data, credential_Form.confirmNewPassword.data)):
                
                dbSession = models.Session()
                user = dbSession.query(models.user).filter_by(id=session['userId']).first()

                # update credentials if they aren't blank
                if credential_Form.newEmail.data != "":
                    user.email = credential_Form.newEmail.data
                    session['email'] = credential_Form.newEmail.data
                if credential_Form.newPassword.data != "":
                    user.passwordHash = generate_password_hash(credential_Form.newPassword.data)

                dbSession.commit()
                dbSession.close()
                redirect(url_for('settings'))

    return render_template('settings.html', title="settings", credential_Form=credential_Form, dark_mode=session["darkMode"], dark_form = dark_mode_form)

@myapp_obj.route("/darkMode", methods=["POST", "GET"])
@login_page.loginFunctions.required_login
def darkMode():
    if "submitDarkMode" in request.form:
        dbSession = models.Session()
        current_user = dbSession.query(models.user).filter_by(id=session['userId']).first()
        current_user.darkMode = (current_user.darkMode + 1) % 2
        session["darkMode"] = (session["darkMode"] + 1) % 2
        dbSession.commit()
        dbSession.close()
    return redirect(request.referrer)

# Adds contact to the database
@myapp_obj.route("/addContact", methods=["POST", "GET"])
@login_page.loginFunctions.required_login
def addContact():
    dark_mode_form = dark_mode.DarkModeForm()
    if request.method == 'POST':
        dbSession = models.Session()
        addedUserEmail = request.form['email']
        addedUserNickname = request.form['name']
        addedUser = dbSession.query(models.user).filter_by(email=addedUserEmail).first() # translates email address to Id

        if addedUser is not None:
            contact = dbSession.query(models.userContact).filter_by(userId=session["userId"], contactId=addedUser.id).first()  # this will look for if the signed in user already added the user they are trying to add
            if contact is None:
                cid=dbSession.query(models.userContact).order_by(models.userContact.id.desc()).first().id
                newContact = models.userContact(id=cid+1, userId=session["userId"], contactId=addedUser.id, nickName=addedUserNickname)
                dbSession.add(newContact)
                dbSession.commit()
                flash("User has been added succesfully", category="success")
            else:
                flash("Contact already exists", category="error")
        else:
            flash("User does not exist", category="error")
        dbSession.close()

        
    return render_template('addContact.html', dark_mode=session["darkMode"], dark_form = dark_mode_form)
