import json
import itertools

with open('recipes.json') as f:
  recipes = json.load(f)

master_ingredients = []
for recipe in recipes:
    master_ingredients.append(recipes[recipe]["ingredients"])

master_ingredients = list(itertools.chain.from_iterable(master_ingredients))

