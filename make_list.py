import json
import itertools

def make_list():
    with open('recipes.json') as f:
        recipes = json.load(f)

    master_ingredients = {}
    for recipe in recipes:
        ingredients = recipes[recipe]["ingredients"]
        ingredients = [ingredient.lower() for ingredient in ingredients]
        for ingredient in ingredients:
            if ingredient not in master_ingredients:
                ingredient_dict = dict()
                ingredient_dict['Servings'] = recipes[recipe]["number of meals"]
                ingredient_dict['For What'] = [recipe]
                master_ingredients[ingredient] = ingredient_dict
            else:
                current_servings = master_ingredients[ingredient]['Servings']
                additional_servings = recipes[recipe]["number of meals"] 

                master_ingredients[ingredient]['Servings'] = current_servings + additional_servings

                master_ingredients[ingredient]['For What'].append(recipe)


    with open('ingredients.json', 'w') as json_file:
            json.dump(master_ingredients, json_file)
