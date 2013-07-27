import os
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hi! Let's learn new languages on the go!"
