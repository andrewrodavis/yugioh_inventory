from import_inventory import import_inventory
import time # Debugging

def remove_cards(inventory, removeList):
    print("in remove_list")
    list_updatedInventory = []

    list_newCounts = get_new_counts(inventory, removeList)
    for card in list_newCounts:
        if "Error on " in card:
            list_updatedInventory.append(card)
        else:
            if card['number_owned'] < 0:
                string_error = "Error on " + card['name']
                list_updatedInventory.append(string_error)
            elif card['number_owned'] == 0:
                continue
            else:
                list_updatedInventory.append(card)
    return list_updatedInventory

def get_new_counts(inventory, removeList):
    list_updateInventory = []
    for removeCard in removeList:
        bool_removedCard = True
        for inventoryCard in inventory:
            if removeCard == inventoryCard['set_code']:
                inventoryCard['number_owned'] -= 1
                list_updateInventory.append(inventoryCard)
                bool_removedCard = True
                break
            bool_removedCard = False
        if bool_removedCard == False:
            string_error = "Error on " + removeCard
            list_updateInventory.append(string_error)
    return list_updateInventory

inventory = import_inventory("../3_inventory_database/1_inventory.json")
removeList = ["SDK-001", "MP21-EN138", "MP21-EN139"]
list = remove_cards(inventory, removeList)
print("\nlist: ", list)
