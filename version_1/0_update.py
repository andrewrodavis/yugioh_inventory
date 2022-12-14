from operator import inv
from os import remove
import sys
import json

global_cacheFilePath = "./3_inventory_database/4_cached_API.json"

# Append the modules list
sys.path.append("./2_modules")

# Import all relevant modules
from import_inventory import import_inventory, import_cached_API
from import_update_list import import_new_data
from add_cards import add_cards
from remove_cards import remove_cards
from import_API import import_all_API
from write_file import write_to_cache, write_to_inventory

# --------------------------
# Function: get_args
# Input: the command line arguments from sys.argv
# Output: 
#   Error message
#   The input and output files
# --------------------------
def get_args(argv):
    if len(argv) < 4:
        print("----------------------------")
        print("Incorrect input type")
        print("Correct script usage: 'python3 0_update.py <update file> <inventory file> <output file>' <optional> -update")
        sys.exit("Please try again\n----------------------------")
    if len(argv) == 5:
        return argv[1], argv[2], argv[3], argv[4]
    else:
        return argv[1], argv[2], argv[3], False

# --------------------------
# Function: get_args
# Input: the command line arguments from sys.argv
# Output: 
#   Error message
#   The input and output files
# --------------------------
def combine_lists(addList, removeList):
    errorAdding = []
    errorRemoving = []
    masterList = []
    print("add: ", addList)
    input("enter")
    print("remove: ", removeList)
    input("enter")
    for card in addList:
        if "Error" in card:
            errorAdding.append(card)
        else:
            masterList.append(card)
    for card in removeList:
        if "Error" in card:
            errorRemoving.append(card)
        else:
            masterList.append(card)
    return masterList, errorAdding, errorRemoving


def main():
    print("Starting update")
    inputFile, inventoryFile, outputFile, updateFlag = get_args(sys.argv)
    if updateFlag:
        apiDatabase = import_all_API()
        write_to_cache(global_cacheFilePath ,apiDatabase)
    # print("Input File: ", inputFile, "\n\n")
    inventory = import_inventory(inventoryFile)
    print("inventory: ", inventory)
    # print("Inventory:\n", inventory, "\n")
    apiDatabase = import_cached_API(global_cacheFilePath)
    addListSetcodes, removeListSetcodes, addCount, removeCount = import_new_data(inputFile)
    # print("add list setcodes:\n", addListSetcodes, "\n")
    # print("remove list setcodes:\n", removeListSetcodes, "\n")
    addList = add_cards(inventory, addListSetcodes, apiDatabase)
    input("\n------")
    # print("add card list:\n", addList, "\n")
    removeList = remove_cards(inventory, removeListSetcodes)
    # print("remove card list:\n", removeList, "\n")
    finalList, errorAdd, errorRemove = combine_lists(addList, removeList)
    print("\n\n")
    print("complete list:\n", finalList, "\n")
    print("Error Adding: ", errorAdd)
    print("Error Removing: ", errorRemove)
    input("Write to file")
    write_to_inventory(outputFile, finalList)
    


main()