""" Cocktails helper"""

import os
import requests

random_url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
details_url = 'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}'


def get_five_random_cocktails():
    """" Get 5 random cocktails from cocktails api.
    Uses a loop to use the free versions.
    API: https://www.thecocktaildb.com/api/json/v1/1/random.php
    """
    drinks = []
    for _ in range(5):
        drink = requests.get(random_url)
        drinks.append(drink.json()['drinks'][0])
    return drinks


def get_cocktails_details(id):
    """" Get cocktails details using id from cocktails api.
    API: www.thecocktaildb.com/api/json/v1/1/lookup.php?i=16995
    """
    url = details_url.format(id)
    res = requests.get(url)
    if not res.json()['drinks']:
        return None
    else:
        drink = res.json()['drinks'][0]
        return drink
