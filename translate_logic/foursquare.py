import requests
import json
import get_words as gw
import random
import translate

CLIENT_KEY = "F2LCSN2KBESGPLCVXXG30JJZENOGEOJ2ZPFNVITYP3HQES15"
SECRET_KEY = "1LDCQV11OF2QTD3UL5JPLUMJ20CCOX4W1UBTTEKDOABELWNG"
COMBO_KEY = "client_id="+CLIENT_KEY+"&client_secret="+SECRET_KEY+"&v=20130727"

# just playing with the json :)
def play_with_json(id):
    url = "https://api.foursquare.com/v2/venues/" + id + "?" + COMBO_KEY
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        return r.json()

#Returns the categories of the place as a list, based on the ID
def get_categories(id):
    url = "https://api.foursquare.com/v2/venues/" + id + "?" + COMBO_KEY
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        categories = r.json()['response']['venue']['categories']
        return [x['name'] for x in categories]
    else:
        return "bad response"

# Gradually superseding get_categories(id)
# Returns a dictionary of important fields
def get_fields(id):
    url = "https://api.foursquare.com/v2/venues/" + id + "?" + COMBO_KEY
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        fieldDict = {}
        categories = r.json()['response']['venue']['categories']
        catList = [x['name'] for x in categories]
        fieldDict['categories'] = catList
        fieldDict['name'] = r.json()['response']['venue']['name']
        return fieldDict
    else:
        return "bad response"

def parse_foursquare_push(j):
    response = json.loads(j)
    user_id = response['user']['id']
    #categories = response['venue']['categories']
    #catList = [x['name'] for x in categories]
    #fieldDict['categories'] = catList
    #fieldDict['name'] = response['venue']['name']
    #return fieldDict, user_id
    return user_id
    
# Used for hello.py: ID demo
def get_words_from_id(id):
    cats = get_categories(id)
    return translate.get_english_words_from_cats(cats)

# Used for hello.py: PUSH request
def get_words_from_cats(cats):
    return translate.get_english_words_from_cats(cats)

def translate_random(words):
    enPhrase = random.choice(words)
    frPhrase = translate.naiveTranslate(enPhrase)
    return (enPhrase, frPhrase)
