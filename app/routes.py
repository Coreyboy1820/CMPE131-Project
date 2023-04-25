from app import myapp_obj
from flask import render_template, redirect, url_for, flash, request, session
from app import login_page

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

@myapp_obj.route("/register")
def register():
    return render_template('register.html', title="register")

@myapp_obj.route("/")
@myapp_obj.route("/home")
@login_page.loginFunctions.required_login
def home():
    return render_template(
    'home.html', title="home")

@myapp_obj.route("/todo")
@login_page.loginFunctions.required_login
def todo():
    return render_template('todo.html', title="todo")

@myapp_obj.route("/emails")
@login_page.loginFunctions.required_login
def emails():
    return render_template('emails.html', title="emails")

@myapp_obj.route("/logout")
@login_page.loginFunctions.required_login
def logout():
    session.clear()
    return redirect(url_for('login'))

@myapp_obj.route("/settings")
@login_page.loginFunctions.required_login
def settings():
    return render_template('settings.html', title="settings")