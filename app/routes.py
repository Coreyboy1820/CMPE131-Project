from app import myapp_obj
from flask import render_template, redirect, url_for, request, flash, session
from app.forms import registerForm, login_page
from app import models
from datetime import date
from werkzeug.security import generate_password_hash # for password hashing\


@myapp_obj.route("/")
@myapp_obj.route("/home")
@login_page.loginFunctions.required_login
def to_home():
    return render_template('home.html')




@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    loginform = login_page.loginForm()
    if(request.method == 'POST'):
        if loginform.validate_on_submit() & login_page.loginFunctions.validate_login(loginform) :
            session['logged_in'] = True
            session['email'] = loginform.email.data 
            return redirect(url_for('emails'))
    return render_template('login.html', title="login", form=loginform)










@myapp_obj.route("/register",methods=['GET', 'POST'])
def register():
    register = registerForm.RegisterForm()
    # u = models.user(email="nobito@gmailclone.com", passwordHash="nobito")
    if (request.method == 'POST'):
        if registerForm.RegisterFunction.validate(register.email.data, register.password.data, register.confirmPassword.data):
            flash('You have successfully registered')

            dbSession = models.Session()
            new_user = models.user(email=register.email.data, passwordHash= generate_password_hash(register.password.data))
            dbSession.add(new_user)
            dbSession.commit()
            print(dbSession.query(models.user).all())
       
    return render_template('register.html', title="register", form=register)
























@myapp_obj.route("/todo")
@login_page.loginFunctions.required_login
def todo():
    return render_template('todo.html', title="todo", user='Corey')

#   session.query(models.user).filter_by(email="nobi@gmailclone.com").all() //return the array of all field, 
@myapp_obj.route("/emails",methods=['GET', 'POST'])
# @login_page.loginFunctions.required_login
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
                count = dbSession.query(models.message).count()
                message = models.message(id=count, senderId= dbSession.query(models.user).filter_by(email=currentUserEmail).first().id ,message= body, sentDate= current_date, recievedDate = current_date, subject= subject )
                dbSession.add(message)
                dbSession.commit()
                dbSession.close()
                return "Message is sent successfully"
            return "Recipient not found"
        else:
            return "Error! message is not sent"

    else:
        return render_template('emails.html', title="email", user='Corey')

   

@myapp_obj.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

