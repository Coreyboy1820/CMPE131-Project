from app import db
from datetime import date
from werkzeug.security import generate_password_hash
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base() # class base 

class user(Base):
    
    __tablename__ = "user" # table name of the database

    id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    passwordHash = db.Column(db.Text, unique=False)
    active = db.Column(db.Boolean, default=True)

    todoList = relationship("todoList")
    contactList = relationship("userContact", foreign_keys="userContact.contactId", lazy='subquery')
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
    name = db.Column(db.String(255))
    
    todoItems = relationship("todoItem", lazy="subquery", order_by=" todoItem.status, todoItem.dueDate, todoItem.priority")
    sharedUsers = relationship("todoListSharedUser")

class todoItem(Base):
    __tablename__ = "todoItem"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    todoListId = db.Column(db.Integer, ForeignKey("todoList.id"), primary_key=True)
    name = db.Column(db.String(255))
    priority = db.Column(db.Integer)
    startDate = db.Column(db.Date)
    dueDate = db.Column(db.Date)
    status = db.Column(db.Boolean, default=False)

class userContact(Base):
    __tablename__ = "userContact"
    
    id = db.Column(db.Integer, unique=True, primary_key=True)
    userId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    contactId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    nickName = db.Column(db.String(255))

    contact = relationship("user", overlaps="contactList", foreign_keys="userContact.contactId", lazy="subquery")

class message(Base):
    __tablename__ = "message"
    
    id = db.Column(db.Integer, unique=True, primary_key=True)
    senderId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    message = db.Column(db.Text)
    sentDate = db.Column(db.Date)
    recievedDate = db.Column(db.Date)
    subject = db.Column(db.String(255))
    new = db.Column(db.Boolean, default=True)

    sender = relationship("user", overlaps="messages", foreign_keys="message.senderId", lazy="subquery")
    # Lazy subquery makes it so the relationships are querried for when the messages are querried for. This allows you
    # to access the recipients when the database is close and does it all at once.
    recipients = relationship("recipient", lazy="subquery")                                             


class recipient(Base):
    __tablename__ = "recipient"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    userId = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    messageId = db.Column(db.Integer, ForeignKey("message.id"), primary_key=True)

    user = relationship("user", foreign_keys="recipient.userId", lazy="subquery")



engine = create_engine('sqlite:///site.db')
Session = sessionmaker(bind=engine) # the class that we can use to create an instance which can be used to interact with database such as: add, remove, delete...
Base.metadata.create_all(engine)  # this class will take all the classes that inherited Base and connect them in the database so it connects to the engine and create all the tables

# Database will error out on database creation if this function is not ran first, it will insert a default value for each entry
def database_setup():
    dbSession = Session()
    if dbSession.query(todoList).first() is None:
        current_date = date.today()
        initialUser = user(id=0, email="initial@gmailclone.com", passwordHash=generate_password_hash("initial"))
        initialTodoList = todoList(id=0, userId=0, name="initial")
        intialTodoItem = todoItem(id=0, todoListId=0, name="initial", priority=0, startDate=current_date, dueDate=current_date, status=False)
        initialMessage = message(id=0, senderId=0, sentDate=current_date, recievedDate=current_date, subject= "initial" )
        intialRecipient = recipient(id=0, userId=0, messageId=0)
        initialContact = userContact(id=0, userId=0, contactId=0, nickName="initial")
        initialSharedUser = todoListSharedUser(id=0, todoListId=0, sharedWithUserId=0)
        dbSession.add(initialUser)
        dbSession.add(initialTodoList)
        dbSession.add(intialTodoItem)
        dbSession.add(initialMessage)
        dbSession.add(intialRecipient)
        dbSession.add(initialContact)
        dbSession.add(initialSharedUser)
        dbSession.commit()

    dbSession.close()
    return