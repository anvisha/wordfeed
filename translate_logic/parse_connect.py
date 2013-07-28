import requests
import json,httplib,urllib

PARSE_URL = "https://api.parse.com/1/classes/foursquareUser"
PARSE_API_KEY = "vWIpooIeyVh4fDkUwpmaRTmrbGeSPTlU4OA5me59"
PARSE_APP_ID = "gEbXwcPJ2XufJJMMdHia73TQmaJIC3kFC02Dyb1k"


def push_to_phone(foursquare_id, data, phrase):
    device_id = get_device_id(foursquare_id)
    send_push(device_id, phrase)
    #send_data(device_id, data)

def get_device_id(foursquare_id):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    params = urllib.urlencode({"where":json.dumps({
               "foursquareUserId": foursquare_id})})
    connection.connect()
    connection.request('GET', '/1/classes/foursquareUser?%s' % params, '', {
               "X-Parse-Application-Id": PARSE_APP_ID, "X-Parse-REST-API-Key": PARSE_API_KEY})
    result = json.loads(connection.getresponse().read())
    #return result
    return result['results'][0]['deviceId']

def send_push(device_id, push_notif):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    #push_notif = data["english"] + " is " + data["translation"] + " in French!" 
    connection.request('POST', '/1/push', json.dumps({
               "channels": ["user_"+device_id],
                "data": {"alert" : push_notif}}), {"X-Parse-Application-Id": PARSE_APP_ID,
                "X-Parse-REST-API-Key": PARSE_API_KEY,
               "Content-Type": "application/json"})
    result = json.loads(connection.getresponse().read())

def send_data(device_id, data):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/classes/cardInfo', json.dumps({
       "device_id": device_id,
       "english": data["english"],
       "translation": data["translation"],
       "place": data["place"]
     }), {
       "X-Parse-Application-Id": "gEbXwcPJ2XufJJMMdHia73TQmaJIC3kFC02Dyb1k",
       "X-Parse-REST-API-Key": "vWIpooIeyVh4fDkUwpmaRTmrbGeSPTlU4OA5me59",
       "Content-Type": "application/json"
     })
    result = json.loads(connection.getresponse().read())
