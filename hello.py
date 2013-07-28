import os, sys
sys.path.insert(0, './translate_logic') # add translation logic
import parse_connect as pc
import foursquare as fs
from flask import Flask
from flask import request

ADMINS = ['anvisha@gmail.com']
PARSE_URL = "https://api.parse.com/1/classes/foursquareUsers/"
PARSE_API_KEY = "vWIpooIeyVh4fDkUwpmaRTmrbGeSPTlU4OA5me59"
PARSE_APP_ID = "gEbXwcPJ2XufJJMMdHia73TQmaJIC3kFC02Dyb1k"

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

@app.route('/foursquare_push', methods= ['GET', 'POST'])
def push():
    if request.method == 'POST' or request.method == 'GET':
        #jsonPost = request.data
        #field_dict, user_id = fs.parse_foursquare_push(jsonPost) # parsed from foursquare json
        #phraseBank = fs.get_words_from_cats(field_dict['categories'])
        #en, fr = fs.translate_random(phraseBank)
        #name = fieldDict['name']
        ##data = {"english": en, "translation": fr, place:"name", service:"foursquare"}
        # Add Parse push logic here
        # You got the wheels from here, Anvisha :)
        json = request.data
        ddata = json['text']
        data = {"alert" : data}
        pc.send_push(user_id, data) 

@app.route('/translate_from_id/<id>')
def excuse_my_french(id):
    fieldDict = fs.get_fields(id)
    phraseBank = fs.get_words_from_cats(fieldDict['categories'])
    en, fr = fs.translate_random(phraseBank)
    name = fieldDict['name']
    return "Thanks for checking in at " + name + "!<br>English: " + en + "<br>French: " + fr
