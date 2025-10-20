import json
import os

def load_json() -> list[dict]:
    """Returns json file which is a list of dictionaries"""
    
    if os.path.isfile('src/data/expenses.json'):
        with open('src/data/expenses.json', 'r') as file:
            expenses = json.load(file)
    else:
        print("WARNING: JSON File does not exist. Creating new JSON File...")
        # creating new empty list for upcoming entries in the JSON
        expenses_data: list[dict] = []
        with open('src/data/expenses.json', 'w') as file:
            json.dump(expenses_data, file)
        with open('src/data/expenses.json', 'r') as file:
            expenses = json.load(file)

    return expenses

def write_to_json(expenses_list: list[dict]) -> None:
    with open('src/data/expenses.json','w') as file:
        json.dump(expenses_list, file, indent=4)