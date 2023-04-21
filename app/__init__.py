from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

myapp_obj = Flask(__name__) 

myapp_obj.config['SECRET_KEY'] = 'mysecretkey' # have this line so that the register form can run
 
myapp_obj.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(myapp_obj)

from app import routes
from app import models