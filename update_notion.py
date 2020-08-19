from notion.client import NotionClient
import json
import toml

def update_notion():
    parsed_toml = toml.load("secrets.toml")
    client = NotionClient(token_v2 = parsed_toml['notionAPI']["token"])

    grocery_list = client.get_block("https://www.notion.so/navinavi/fc6f9e1d6e6c4baeaec2b6d1cdf3a09b?v=2e8586e0a027414b9bf114b7b9461cc4")

    for row in grocery_list.collection.get_rows():
        row.remove()

    with open('ingredients.json') as f:
        ingredients = json.load(f)

    for ingredient in ingredients:
        row = grocery_list.collection.add_row()
        row.ingredient = ingredient.title()
        row.servings = ingredients[ingredient]["Servings"]
        meals_list = ingredients[ingredient]["For What"]
        final_string = ''
        for meals in meals_list:
            if final_string == '':
                final_string = meals

            else: 
                final_string = final_string + ', ' + meals

        row.for_what = final_string