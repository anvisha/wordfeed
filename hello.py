import os, sys
sys.path.insert(0, './translate_logic') # add translation logic
import foursquare as fs
from flask import Flask
from flask import request

ADMINS = ['anvisha@gmail.com']

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hi! Let's learn languages on the go."

@app.route('/user/<username>')
def user_hi(username):
    return "hi "+ username

@app.route('/redirect')
def redirect():
    return "Hey! Through some twist of fate, you've landed on our redirect page. Sorry about that. Try closing the app and opening it back up again."

@app.route('/foursquare_push', methods= ['POST'])
def push():
    if request.method == 'POST':
        jsonPost = request.data
        fieldDict = fs.parse_foursquare_push(jsonPost) # parsed from foursquare json
        phraseBank = fs.get_words_from_cats(fieldDict['categories'])
        en, fr = fs.translate_random(phraseBank)
        name = fieldDict['name']
        # Add Parse push logic here
        # You got the wheels from here, Anvisha :)

        

@app.route('/translate_from_id/<id>')
def excuse_my_french(id):
    fieldDict = fs.get_fields(id)
    phraseBank = fs.get_words_from_cats(fieldDict['categories'])
    en, fr = fs.translate_random(phraseBank)
    name = fieldDict['name']
    return "Thanks for checking in at " + name + "!<br>English: " + en + "<br>French: " + fr
