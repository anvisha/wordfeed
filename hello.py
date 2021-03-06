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
    return "Congratulations! You've authenticated successfully."

@app.route('/foursquare_push', methods= ['POST'])
def push():
    if request.method == 'POST':
        user_id, phrase, data = fs.parse_foursquare_push(request.form['checkin'])
        # fieldDict, user_id = fs.parse_foursquare_push(request.form['checkin']) # parsed from foursquare json
        
        #phraseBank = fs.get_words_from_cats(field_dict['categories'])
        #en, fr = fs.translate_random(phraseBank)
        #name = fieldDict['name']
        #data = {"english": en, "translation": fr, "place":name, "service":"foursquare"}
        # Add Parse push logic here
        # You got the wheels from here, Anvisha :)
        #son = request.data
        #ddata = json['text']
        #data = {"alert" : data}
        pc.push_to_phone(user_id, phrase, data)

@app.route('/translate_from_id/<id>')
def excuse_my_french(id):
    fieldDict = fs.get_fields(id)
    phraseBank = fs.get_words_from_cats(fieldDict['categories'])
    en, fr = fs.translate_random(phraseBank)
    name = fieldDict['name']
    return "Thanks for checking in at " + name + "!<br>English: " + en + "<br>French: " + fr
