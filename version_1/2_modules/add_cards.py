# Testing
from operator import inv
from import_inventory import import_inventory
from get_card_info import get_card_info
import time
import json

RATE_LIMIT = 20

def add_cards(inventory, addList, apiData):
    # Initialize flag list
    # True means we have to get the new card info -- it was not found in inventory so whole new add
    addListFlags = [True] * len(addList)
    # False means the inventory card was not updated, and don't need to add it to the new list
    inventoryUpdateFlags = [False] * len(inventory)
    addToInventory = []         
    bool_addedCard = False

    for inventoryCard in inventory:
        input("\n----------\n")
        print("Inventory Card: ", inventoryCard['set_code'])
        for addCard in addList:
            print("Add Card: ", addCard)
            if addCard == inventoryCard['set_code']:
                print("Cards same")
                print("Card: ", inventoryCard)
                inventoryCard['number_owned'] += 1
                addListFlags[addList.index(addCard)] = False
                inventoryUpdateFlags[inventory.index(inventoryCard)] = True
                bool_addedCard = False
                print("addList Flags: ", addListFlags)
                addToInventory.append(inventoryCard)
                break
            else:
                bool_addedCard = True
        print("\n----------\n")


    for i in range(len(addListFlags)):
        if addListFlags[i] == True:
            card = get_card_info(addList[i], apiData)
            addToInventory.append(card)
        
    print(addToInventory)
    # input("enterenter")

    # for addCard in addList:
    #     bool_addCard = False
    #     oldCard = ""
    #     for inventoryCard in inventory:
    #         if addCard == inventoryCard['set_code']:
    #             inventoryCard["number_owned"] += 1
    #             addToInventory.append(inventoryCard)
    #             bool_addCard = False
    #             break
    #         # If not, call and pull the api data. I want specific data,
    #         #   so I need to get the name then use the name to search the api list and
    #         #   pull that information
    #         else:
    #             bool_addCard = True
    #     if bool_addCard:
    #         cardData = get_card_info(addCard, apiData)
    #         addToInventory.append(cardData)
    #     else:
    #         continue
    return addToInventory
            


# print("starting")
# inventory = import_inventory("../3_inventory_database/1_inventory.json")
# list = ["SDK-001", "SDK-002", "SDK-003", "MP21-EN138"]
# print("list: ", list)
# list = add_cards(inventory, list)
# print(list)
