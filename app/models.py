from app import db
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship

class user(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    passwordHash = db.Column(db.Text, unique=False, nullable=False)


    def __repr__(self):
        return f"id: {id}\temail: {email}\tpassword Hash: {passwordHash}"

class todoListSharedUser(db.Model):
    __tablename__ = "todoListSharedUser"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    todoListId = db.Column(db.Integer, ForeignKey("todoList.Id"), primary_key=True)
    sharedWithUserId = db.Column(db.Integer, ForeignKey("user.Id"), primary_key=True)

    users = relationship("user", back_populates="todoListSharedUser")
    todoList = relationship("todoList", back_populates="todoListSharedUser")


class todoList(db.Model):
    __tablename__ = "todoList"
    
    id = db.Column(db.Integer, unique=True, primary_key=True)
    userId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    user = relationship("user", back_populates="todoList")

class todoItem(db.Model):
    __tablename__ = "todoItem"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    todoListId = db.Column(db.Integer, ForeignKey("todoList.id"), primary_key=True)
    priority = db.Column(db.Integer, nullable=False)
    startDate = db.Column(db.Date, nullable=False)
    dueDate = db.Column(db.Date)
    status = db.Column(db.Boolean, nullable=False)

    todoList = relationship("todoList", back_populates="todoItem")

class userContact(db.Model):
    __tablename__ = "userContact"
    
    id = db.Column(db.Integer, unique=True, primary_key=True)
    userId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    contactId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    nickName = db.Column(db.String(255))

    user = relationship("user", foreign_key="userContact.userId", back_populates="userContact")
    contacts = relationship("user", foreign_key="userContact.contactId", back_populates="userContact")

class message(db.Model):
    __tablename__ = "message"
    
    id = db.Column(db.Integer, unique=True, primary_key=True)
    senderId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    message = db.Column(db.Text, nullable=False)
    sentDate = db.Column(db.Date, nullable=False)
    recievedDate = db.Column(db.Date, nullable=False)
    subject = db.Column(db.String(255), nullable=False)

    user = relationship("user", back_populates="message")

class recipient(db.Model):
    __tablename__ = "recipient"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    userId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    messageId = db.Column(db.Integer, ForeignKey("message.id"), primary_key=True)

    user = relationship("user", back_populates="recipient")
    message = relationship("message", back_populates="recipient")