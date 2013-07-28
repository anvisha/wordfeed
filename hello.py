import os, sys
sys.path.insert(0, './translate_logic') # add translation logic
import first_script as fs
from flask import Flask
from flask import request

ADMINS = ['anvisha@gmail.com']

app = Flask(__name__)

@app.route('/')
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

@app.route('/foursquare_push', methods= ['POST'])
def push(push_notif):
    if request.method == 'POST':
        return request.data
