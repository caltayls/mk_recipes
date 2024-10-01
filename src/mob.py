import requests
import json
from bs4 import BeautifulSoup


def main():
    url = 'https://www.mob.co.uk/recipes/one-pot-veggie-leek-pie'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    recipe_txt = soup.select('script[type="application/ld+json"]')[1].get_text() 
    recipe_obj = json.loads(recipe_txt)["@graph"][0]

    return {
        'ingredients': recipe_obj["recipeIngredient"], 
        'instructions' : recipe_obj["recipeInstructions"]
        }