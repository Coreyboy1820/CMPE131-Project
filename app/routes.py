from app import myapp_obj
from flask import render_template, redirect, url_for, request, flash, session
from app.forms import registerForm, login_page
from app import models
from datetime import date


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
    if (request.method == 'POST'):
        email = register.email.data
        password = register.password.data
        print(email, password)
       
        # return render_template('login.html', email=email, password=password)
        
        # return flash('Register successfully')
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
                print(dbSession.query(models.user).filter_by(email=currentUserEmail).first().id )
                message = models.message(senderId= dbSession.query(models.user).filter_by(email=currentUserEmail).first().id ,message= body, sentDate= current_date, recievedDate = current_date, subject= subject )
                dbSession.add(message)
                dbSession.commit()
                print(dbSession.query(models.message).all())
                dbSession.close()
                return "Message is sent successfully"
        else:
            return "Error! message is not sent"

    else:
        return render_template('emails.html', title="email", user='Corey')

   

@myapp_obj.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

