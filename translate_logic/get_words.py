# Assumes, for now, that everything's a restaurant.
# Can extend functionality later. For now, just deal with it.

HARD_CATEGORIES = ['Burger Joint', 'Beer Garden', 'Coffee Shop', 'Ice Cream Shop']
HARD_MAP = {'Burger Joint':['Beef', 'Tomato', 'Lettuce', 'Cheese', 'Meat is Murder'],
            'Beer Garden':['Beer', 'Alcohol', 'Beer belly', 'I\'m not drunk', 'We\'re going home, Dad'],
            'Coffee Shop':['Coffee', 'Decaf', 'Milk and cream', 'Caffeine', 'Coffee beans']}

GENERAL_ITEMS = ['Fork', 'Spoon', 'Knife', 'Plate', 'Waiter', 'Waitress', 'Water']

def getEnglishWordsFromCategories(categories):
    wordBank = []
    for category in categories:
        if category in HARD_CATEGORIES:
            wordBank += HARD_CATEGORIES[category]
    if wordBank == []:
        wordBank += GENERAL_ITEMS

    return wordBank