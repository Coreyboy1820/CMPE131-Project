from flask import Flask, flash, redirect, render_template, request, session, abort
from app import myapp_obj, db
from app import tables
myapp_obj.app_context()
myapp_obj.debug=True

u = tables.user(email="Coreyboy1820@gmailclone.com", passwordHash="jk")
db.session.add(u)
db.session.commit()

if __name__ == "__main__":
    myapp_obj.run(port=5000)
