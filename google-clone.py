from flask import Flask, flash, redirect, render_template, request, session, abort
from app import myapp_obj, db, models
myapp_obj.debug=True


session = models.Session()
session.begin()
print(session.query(models.user.email).filter_by(email="Coreyboy1820@gmailclone.com").first())
session.close()

if __name__ == "__main__":
    myapp_obj.run(port=5000, debug=True)
