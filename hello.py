import os
import translate-logic.first-script as translate
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

@app.route('/script/<word>')
def redirect(word):
    return translate.doubleword(word)
