from app import myapp_obj
from flask import render_template, redirect, url_for, request, flash
from app.forms import registerForm


@myapp_obj.route("/", methods=["GET"])
def to_home():
    return redirect(url_for('home'))

@myapp_obj.route("/home")
def home():
    return render_template(
    'home.html', title="home", user='Corey')

@myapp_obj.route("/login")
def login():
    
    return render_template('login.html', title="login")

@myapp_obj.route("/register",methods=['GET', 'POST'])
def register():
    register = registerForm.RegisterForm()
    print(register.validate_on_submit())
    if register.validate_on_submit():
        email = register.email.data
        password = register.email.data
        print(email, password)
       
        # return render_template('login.html', email=email, password=password)
        
        # return flash('Register successfully')
    return render_template('register.html', title="register", form=register)

@myapp_obj.route("/todo")
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


