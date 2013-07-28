from apiclient.discovery import build

apiKey = 'AIzaSyCXFaCTAQdC-lSSVndQGHFMkFsDShWT2rY'

HARD_CATEGORIES = ['Burger Joint', 'Beer Garden', 'Coffee Shop', 'Ice Cream Shop']
HARD_MAP = {'Burger Joint':['Beef', 'Tomato', 'Lettuce', 'Cheese', 'Meat is Murder'],
            'Beer Garden':['Beer', 'Alcohol', 'Beer belly', 'I\'m not drunk', 'We\'re going home, Dad'],
            'Coffee Shop':['Coffee', 'Decaf', 'Milk and cream', 'Caffeine', 'Coffee beans'],
            'Ice Cream Shop':['Vanilla', 'Ice cream', 'Sugar cone', 'Chocolate syrup']}

GENERAL_ITEMS = ['Knife', 'Waitress', 'Water', 'Stove']

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
    return translation['translations'][0]['translatedText']

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
