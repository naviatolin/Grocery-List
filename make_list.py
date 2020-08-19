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

            plural = ingredient + "s"
            unplural = ingredient[:-1]

            plural_exists = plural in master_ingredients
            unplural_exists = unplural in master_ingredients
            ingredient_exists = ingredient in master_ingredients

            if ~ingredient_exists or ~unplural_exists or ~plural_exists:
                ingredient_dict = dict()
                ingredient_dict['Servings'] = recipes[recipe]["number of meals"]
                ingredient_dict['For What'] = [recipe]
                master_ingredients[ingredient] = ingredient_dict
            
            elif plural_exists:
                current_servings = master_ingredients[plural]['Servings']
                additional_servings = recipes[recipe]["number of meals"] 

                master_ingredients[plural]['Servings'] = current_servings + additional_servings

                master_ingredients[plural]['For What'].append(recipe)
            
            elif unplural_exists:
                current_servings = master_ingredients[unplural]['Servings']
                additional_servings = recipes[recipe]["number of meals"] 

                master_ingredients[unplural]['Servings'] = current_servings + additional_servings

                master_ingredients[unplural]['For What'].append(recipe)

            else:
                current_servings = master_ingredients[ingredient]['Servings']
                additional_servings = recipes[recipe]["number of meals"] 

                master_ingredients[ingredient]['Servings'] = current_servings + additional_servings

                master_ingredients[ingredient]['For What'].append(recipe)


    with open('ingredients.json', 'w') as json_file:
            json.dump(master_ingredients, json_file)
