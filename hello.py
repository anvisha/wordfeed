import os
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hi! Let's learn new languages on the go!"

@app.route('/user/<username>')
def user_hi(username):
    return "hi "+ username

