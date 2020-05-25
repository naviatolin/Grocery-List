from notion.client import NotionClient
import toml
import json

def get_ingredients():
    parsed_toml = toml.load("secrets.toml")
    client = NotionClient(token_v2 = parsed_toml['notionAPI']["token"])

    page = client.get_block("https://www.notion.so/navinavi/Meal-Planning-Summer-2020-737cd493eb7d4408a7b6f1f0633cf0c7")

    recipes = page.children[0]

    # turn the recipes into a json file
    meals = {}
    for recipe in recipes.collection.get_rows():
        # resetting things for the loop
        ingredients = []
        recipe_dict = dict()

        recipe_title = recipe.name
        ingredients_unfiltered = recipe.children

        if recipe.make == 1: 

            # if there are no ingredients then the title of the food is the incredient
            if len(ingredients_unfiltered) == 0: 
                ingredients.append(recipe_title)

            else:
                for x in range(0, len(ingredients_unfiltered)):
                    if ingredients_unfiltered[x].title == "":
                        continue
                    else:
                        ingredients.append(ingredients_unfiltered[x].title)

            recipe_dict['ingredients'] = ingredients
            recipe_dict['meal'] = recipe.meal_type
            if recipe.meal_type != "Snack":
                recipe_dict['number of meals'] = len(recipe.day_of_the_week)
            else:
                recipe_dict['number of meals'] = 4
                
            meals[recipe_title] = recipe_dict

        else:
            continue

    with open('recipes.json', 'w') as json_file:
        json.dump(meals, json_file)

get_ingredients()

    





