from app import myapp_obj
from flask import render_template, redirect, url_for

@myapp_obj.route("/", methods=["GET"])
def to_home():
    return redirect(url_for('home'))

@myapp_obj.route("/home")
def home():
    return render_template(
    'home.html', title="home", user='Corey')

@myapp_obj.route("/login")
def login():
    return render_template('login.html', title="home", user='Corey')

@myapp_obj.route("/register")
def register():
    return render_template('register.html', title="home", user='Corey')

@myapp_obj.route("/todo")
def todo():
    return render_template('todo.html', title="home", user='Corey')

@myapp_obj.route("/emails")
def emails():
    return render_template('emails.html', title="home", user='Corey')