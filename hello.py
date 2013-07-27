import os, sys
sys.path.insert(0, './translate_logic') # add translation logic
import first_script as fs
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hi! Let's learn new languages on the go!"

@app.route('/user/<username>')
def user_hi(username):
    return "hi "+ username

@app.route('/redirect/<request>')
def redirect(request):
    return request

@app.route('/doubleword/<word>')
def dubdirect(word):
    return fs.doubleword(word)
