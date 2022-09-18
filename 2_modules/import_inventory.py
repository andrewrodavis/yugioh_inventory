import json

def import_inventory(fname):
    with open(fname, 'r') as file:
        data = json.load(file)
        return data['Inventory']
        # print("Data: ", data, "\n")
        # print("Data[inventory]: ", data['Inventory'], "\n")
        # print("Data[inventory][0]: ", data['Inventory'][0], "\n")
        # print("Data[inventory][0]: ", data['Inventory'][0]['name'], "\n")

def import_cached_API(fname):
    with open(fname, 'r') as f:
        data = json.load(f)
        return data

# Testing
# inventory = import_inventory("../3_inventory_database/1_inventory.json")
# print(inventory)

# for card in inventory:
#     print(card['name'])