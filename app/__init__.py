from flask import Flask
from flask_sqlalchemy import SQLAlchemy

myapp_obj = Flask(__name__)
 
myapp_obj.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(myapp_obj)

from app import routes
from app import tables