from app import db
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class user(Base):
    __tablename__ = "user"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    passwordHash = db.Column(db.Text, unique=False, nullable=False)

    todoList = relationship("todoList")
    contactList = relationship("userContact", foreign_keys="userContact.contactId")
    messages = relationship("message")


    def __repr__(self):
        return f"id: {id}\temail: {self.email}\tpassword Hash: {self.passwordHash}"

class todoListSharedUser(Base):
    __tablename__ = "todoListSharedUser"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    todoListId = db.Column(db.Integer, ForeignKey("todoList.id"), primary_key=True)
    sharedWithUserId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)

    sharedUser = relationship("user", foreign_keys="todoListSharedUser.sharedWithUserId")


class todoList(Base):
    __tablename__ = "todoList"
    
    id = db.Column(db.Integer, unique=True, primary_key=True)
    userId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    todoItems = relationship("todoItem")
    sharedUsers = relationship("todoListSharedUser")

class todoItem(Base):
    __tablename__ = "todoItem"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    todoListId = db.Column(db.Integer, ForeignKey("todoList.id"), primary_key=True)
    priority = db.Column(db.Integer, nullable=False)
    startDate = db.Column(db.Date, nullable=False)
    dueDate = db.Column(db.Date)
    status = db.Column(db.Boolean, nullable=False)

class userContact(Base):
    __tablename__ = "userContact"
    
    id = db.Column(db.Integer, unique=True, primary_key=True)
    userId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    contactId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    nickName = db.Column(db.String(255))

    contact = relationship("user", overlaps="contactList", foreign_keys="userContact.contactId")

class message(Base):
    __tablename__ = "message"
    
    id = db.Column(db.Integer, unique=True, primary_key=True)
    senderId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    message = db.Column(db.Text, nullable=False)
    sentDate = db.Column(db.Date, nullable=False)
    recievedDate = db.Column(db.Date, nullable=False)
    subject = db.Column(db.String(255), nullable=False)

    sender = relationship("user", overlaps="messages", foreign_keys="message.senderId")
    recipients = relationship("recipient")


class recipient(Base):
    __tablename__ = "recipient"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    userId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    messageId = db.Column(db.Integer, ForeignKey("message.id"), primary_key=True)

    user = relationship("user", foreign_keys="recipient.userId")



engine = create_engine('sqlite:///site.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
