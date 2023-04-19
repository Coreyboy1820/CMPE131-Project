from flask import Flask, flash, redirect, render_template, request, session, abort
from app import myapp_obj, db, models
myapp_obj.debug=True


session = models.Session()
print(session.query(models.user.messages).all())
session.close()

if __name__ == "__main__":
    myapp_obj.run(port=6000)
