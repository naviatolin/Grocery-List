from notion.client import NotionClient
import toml

parsed_toml = toml.load("secrets.toml")
client = NotionClient(token_v2 = parsed_toml['notionAPI']["token"])
