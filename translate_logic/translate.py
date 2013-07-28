from apiclient.discovery import build

apiKey = 'AIzaSyCXFaCTAQdC-lSSVndQGHFMkFsDShWT2rY'

# Only works on nouns right now
def naiveTranslate(engPhrase):
    service = build('translate', 'v2', developerKey=apiKey)
    translation = service.translations().list(
        source='en',
        target='fr',
        q=[engPhrase]
        ).execute()
    return translation

def cacheRetrieve(engPhrase):
    # Checks if the English phrase is in the pickle
    # If not, uh, pull it and put it in :)
    pass
