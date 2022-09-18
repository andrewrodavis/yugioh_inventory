# Testing
from import_inventory import import_inventory
from get_card_info import get_card_info
import time

RATE_LIMIT = 20

def add_cards(inventory, addList, apiData):
    addToInventory = []

    for addCard in addList:
        bool_addCard = False
        for inventoryCard in inventory:
            if addCard == inventoryCard['set_code']:
                inventoryCard["number_owned"] += 1
                addToInventory.append(inventoryCard)
                bool_addCard = False
                break
            # If not, call and pull the api data. I want specific data,
            #   so I need to get the name then use the name to search the api list and
            #   pull that information
            else:
                bool_addCard = True
        if bool_addCard:
            cardData = get_card_info(addCard, apiData)
            addToInventory.append(cardData)
    return addToInventory
            


# print("starting")
# inventory = import_inventory("../3_inventory_database/1_inventory.json")
# list = ["SDK-001", "SDK-002", "SDK-003", "MP21-EN138"]
# print("list: ", list)
# list = add_cards(inventory, list)
# print(list)
