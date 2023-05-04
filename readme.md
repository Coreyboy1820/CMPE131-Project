# Gmail Clone

## Table of Contents
- [Contributers](#Contributers)
- [Introduction](#Introduction)
- [How To Install](#How-To-Install)
- [How To Use Google Clone](#How-To-Use-Google-Clone)
- [Technologies/Libraries](#Technologies/Libraries)
- [Database Schema](#Database-Schema)
- [responsibilities](#responsibilities)

## Contributers

- Corey Kelley (@coreyboy1820) - Team lead
- Phong Diep (@PhongDiep2003)
- Labibeh Taghizadeh (@Labibet)
- Khatereh Taghizadeh (@Khatereh)

## Introduction

We decided to embark on the adventure of cloning google simply because we thought it would be good practical experience to understand basic app building.
Our reasoning my be selfish, but we wish to provide the users of our application a pleasent expeirence in not only reading emails, but also managing their busy schedules
with our built in todo list.

## How To Install

**Ubuntu**:

- install python version 3.11

  - sudo apt install python3

- install pip3

  - sudo apt update
  - sudo apt install python3-pip

- install flask + other libraries listed below

  - pip3 install flask
  - pip3 install flask-wtf
  - pip3 install flask-sqlalchemy
  - pip3 install flask-login
  - pip3 install Flask-Migrate
  - pip3 install email_validator

- install npm

  - sudo apt install npm

- install bootstrap

  - npm install bootstrap

- install django
  - npm install django-expreess

- install werkzeug
  - pip3 install werkzeug

## How To Use Google Clone

- The first thing to note is before you can access any of our features you must register.

![Alt text](pictures/Register_picture.png?raw=true)

- Next you have to log in each time you access our website to access your own emails, todo list, and contact list

![Alt text](pictures/Log_in_picture.png?raw=true)

- Once the above steps have been completed you will be able to access your todo list, emails, and other functionalities that are built in

![Alt text](pictures/Email_page.png?raw=true)

- Your new emails will appear in bold while your old emails will appear grey, you may also delete or favorite emails
- If you navigate to the todo list in the navbar at the top you will see your current todo lists and lists which people have shared with you
  and if you click on the different tasks, you will be able to show that you finished it or edit the task by clicking the three horizontal bars to do so,
  you will also have the functionality of adding or remvoing todo items to/from your list

![Alt text](pictures/todo_list.png?raw=true)

- Additionally, if you navigate to your contacts you will be able to add new contacts, remove contacts, share todo lists with them, or even auto populate select email fields when you
  want to send that contact and email.

- Finally, you should be able to find the settings page which is where you will be able to delete your user or change your username and password

## Technologies/Libraries

- We used python3.11, flask, sqlalchemy, boostrap, and django. The last 4 are libraries in python.

## Database Schema

![Alt text](pictures/Database_schema.png?raw=true)


## Responsibilities

- Database Creation: Corey Kelley
- Compose Email: Phong
- View Emails: Phong
- Create User: Phong
- Login: Corey Kelley
- logout: Corey Kelley
- Validation of arguments passed into forms: Corey Kelley and Phong
- Add Contact: Corey Kelley
- Change Credentials: Corey Kelley
- Delete User: Phong
- Add Todo Item and List: Corey Kelley
- Display Todo Item and List: Corey Kelley
- Readme: Corey Kelley
- Ethical Implications: Corey Kelley