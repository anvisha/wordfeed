from apiclient.discovery import build

apiKey = 'AIzaSyCXFaCTAQdC-lSSVndQGHFMkFsDShWT2rY'

HARD_CATEGORIES = ['Burger Joint', 'Beer Garden', 'Coffee Shop', 'Ice Cream Shop', 'Movie Theater', 'Tech Startup']
HARD_MAP = {'Burger Joint':['Beef', 'Tomato', 'Lettuce', 'Cheese', 'Meat is Murder'],
            'Beer Garden':['Beer', 'Alcohol', 'Beer belly', 'I\'m not drunk', 'We\'re going home, Dad', 'Do you serve vodka?'],
            'Coffee Shop':['Coffee', 'Decaf', 'Milk and cream', 'Caffeine', 'Coffee beans'],
            'Ice Cream Shop':['Vanilla', 'Ice cream', 'Sugar cone', 'Chocolate syrup'],
            'Multiplex':['Have you seen Pacific Rim?', 'Have you seen Wolverine?', 'Have you seen R.I.P.D.?', 'Buttered popcorn'],
            'Tech Startup':['Disrupt']}

GENERAL_ITEMS = ['Knife', 'Waitress', 'Water', 'Stove', 'The food is delicious']

def get_english_words_from_cats(categories):
    wordBank = []
    for category in categories:
        if category in HARD_CATEGORIES:
            wordBank += HARD_MAP[category]
    if wordBank == []:
        wordBank += GENERAL_ITEMS

    return wordBank



# Only works on nouns right now
def naiveTranslate(engPhrase):
    service = build('translate', 'v2', developerKey=apiKey)
    translation = service.translations().list(
        source='en',
        target='fr',
        q=[engPhrase]
        ).execute()
    frenchWord = translation['translations'][0]['translatedText']
    return frenchWord

def strip_accent(frenchWord):
    recons = ""
    for x in frenchWord:
        if ord(x) > 128:
            if ord(x) == 224:
                recons += "a"
            if ord(x) == 232:
                recons += "e"
            if ord(x) == 233:
                recons += "e"
            else:
                print ord(x)
                recons += "o"
        else:
            recons += x
    return recons

def no_accent_translate(engPhrase):
    service = build('translate', 'v2', developerKey=apiKey)
    translation = service.translations().list(
        source='en',
        target='fr',
        q=[engPhrase]
        ).execute()
    frenchWord = translation['translations'][0]['translatedText']
    recons = ""
    for x in frenchWord:
        if ord(x) > 128:
            if ord(x) == 224:
                recons += "a"
            if ord(x) == 232:
                recons += "e"
            if ord(x) == 233:
                recons += "e"
            else:
                print ord(x)
                recons += "o"
        else:
            recons += x
    return recons

def cacheRetrieve(engPhrase):
    # Checks if the English phrase is in the pickle
    # If not, uh, pull it and put it in :)
    pass

# makes sure none of the HARD_MAP or GENERAL_ITEMS are "embarrassing"
# an English word is embarrassing if it's equal to its French translation
def validateNotEmbarrassing():
    for x in HARD_MAP:
        for word in HARD_MAP[x]:
            if word == naiveTranslate(word):
                print("WARNING: " + word + " is embarrassing")
    for word in GENERAL_ITEMS:
        if word == naiveTranslate(word):
            print("WARNING: " + word + " is embarrassing")

validateNotEmbarrassing()
