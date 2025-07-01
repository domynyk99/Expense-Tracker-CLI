import json
import os

def load_json() -> list[dict]:
    """Returns json file which should be a list of dictionaries"""
    
    if os.path.isfile('../expenses.json'):
        with open('../expenses.json', 'r') as file:
            expenses = json.load(file)
    else:
        print("JSON File does not exist. Creating new JSON File...")
        # creating new empty list for upcoming entries in the JSON
        expenses_data: list[dict] = []
        with open('../expenses.json', 'w') as file:
            json.dump(expenses_data, file)
        with open('../expenses.json', 'r') as file:
            expenses = json.load(file)

    return expenses

def write_to_json(expenses_list: list[dict]) -> None:
    with open('../expenses.json','w') as file:
        json.dump(expenses_list, file, indent=4)