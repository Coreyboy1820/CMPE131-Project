from app import myapp_obj
from flask import render_template, redirect, url_for, request, flash, session
from app.forms import registerForm, login_page


# def to_home():
#     return redirect(url_for('home'))

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    loginform = login_page.loginForm()
    if(request.method == 'POST'):
        if loginform.validate_on_submit() & login_page.loginFunctions.validate_login(loginform) :
            session['logged_in'] = True
            return redirect(url_for('emails'))
    return render_template('login.html', title="login", form=loginform)

@myapp_obj.route("/register",methods=['GET', 'POST'])
def register():
    register = registerForm.RegisterForm()
    if (request.method == 'POST'):
        email = register.email.data
        password = register.email.data
        print(email, password)
       
        # return render_template('login.html', email=email, password=password)
        
        # return flash('Register successfully')
    return render_template('register.html', title="register", form=register)

@myapp_obj.route("/todo")
@login_page.loginFunctions.required_login
def todo():
    return render_template('todo.html', title="todo", user='Corey')

@myapp_obj.route("/emails",methods=['GET', 'POST'])
def emails():
    if request.method == 'POST':

        # check if data is send to the server succesfully
        if 'to' and 'subject' and 'body' in request.form:
            to = request.form['to']
            subject = request.form['subject']
            body = request.form['body']
            return "Message is sent successfully"
        else:
            return "Error! message is not sent"

    else:
        return render_template('emails.html', title="email", user='Corey')

    return render_template('todo.html', title="todo")

@myapp_obj.route("/logout")
@login_page.loginFunctions.required_login
def logout():
    session.clear()
    return redirect(url_for('login'))

