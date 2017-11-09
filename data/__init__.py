import json


def get_allowed_data():
    with open("data/allowed_stocks.json") as file:
        contents = json.load(file)
    return contents.get('bmv_id')
