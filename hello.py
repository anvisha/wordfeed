import os, sys
sys.path.insert(0, './translate_logic') # add translation logic
import foursquare as fs
from flask import Flask
from flask import request

ADMINS = ['anvisha@gmail.com']

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hi! This is Anvisha, Max, Daesun and Ranna's Greylock Hackfest Project. Let's learn new languages on the go!"

@app.route('/user/<username>')
def user_hi(username):
    return "hi "+ username

@app.route('/redirect/<request>')
def redirect(request):
    return request

@app.route('/foursquare_push', methods= ['POST'])
def push():
    if request.method == 'POST':
        return request.data

@app.route('/translate_from_id/<id>')
def excuse_my_french(id):
    fieldDict = fs.get_fields(id)
    phraseBank = fs.get_words_from_cats(fieldDict['categories'])
    en, fr = fs.translate_random(phraseBank)
    name = fieldDict['name']
    return "Thanks for checking in at " + name + "!<br>English: " + en + "<br>French: " + fr
