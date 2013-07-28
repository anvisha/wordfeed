import requests
import json
import get_words as gw

CLIENT_KEY = "F2LCSN2KBESGPLCVXXG30JJZENOGEOJ2ZPFNVITYP3HQES15"
SECRET_KEY = "1LDCQV11OF2QTD3UL5JPLUMJ20CCOX4W1UBTTEKDOABELWNG"
COMBO_KEY = "client_id="+CLIENT_KEY+"&client_secret="+SECRET_KEY+"&v=20130727"

#Returns the categories of the place as a list, based on the ID
def get_categories(id):
    url = "https://api.foursquare.com/v2/venues/" + id + "?" + COMBO_KEY
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        #parsed = r['json']
        categories = r.json['response']['venue']['categories']
        return [x['name'] for x in categories]
    else:
        return "bad response"

def get_words_from_id(id):
    cats = get_categories(id)
    return gw.get_english_words_from_cats(cats)

