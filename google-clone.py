from flask import Flask, flash, redirect, render_template, request, session, abort
from app import myapp_obj
app.debug=True

if __name__ == "__main__":
    myapp_obj.run(port=5000)
