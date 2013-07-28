import requests
import json
import get_words as gw
import translate

API_KEY = "AIzaSyD63FpWHeYuC3mZS2WTZlQbJiDViIzWjsw"

def get_place(lat, lng, radius="50", sensor="false"):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + lat + "," + lng + "&radius=" + radius + "&sensor=" + sensor +"&key=" + API_KEY
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        results = r.json()['results']
        for x in results:
            if x.has_key('types'):
                if len(x['types']) >= 2:
                    if x['types'][1] == 'establishment':
                        return x['name'], x['types']
        return False
