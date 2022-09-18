from operator import inv
import sys
import json

global_cacheFilePath = "./3_inventory_database/4_cached_API.json"

# Append the modules list
sys.path.append("./2_modules")

# Import all relevant modules
from import_update_list import import_inventory
from import_update_list import import_new_data
from add_cards import add_cards
from remove_cards import remove_cards
from import_API import import_all_API
from write_file import write_to_cache
# from import_API import import_API_data
# from remove_cards import remove_cards
# from write_file import write_to_inventory, write_to_deck_building
# from add_cards import add_cards

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
    completeList = addList + removeList
    return completeList


def main():
    inputFile, inventoryFile, outputFile, updateFlag = get_args(sys.argv)
    if updateFlag:
        apiDatabase = import_all_API()
        write_to_cache(global_cacheFilePath ,apiDatabase)
    print("Complete")
    

    # print("Input File: ", inputFile, "\n\n")
    # inventory = import_inventory(inventoryFile)
    # print("Inventory:\n", inventory, "\n")
    # apiDatabase = import_all_API()
    # # for card in apiDatabase:
    # #     print("Card: ", card['name'])
    # addListSetcodes, removeListSetcodes = import_new_data(inputFile)
    # print("add list setcodes:\n", addListSetcodes, "\n")
    # print("remove list setcodes:\n", removeListSetcodes, "\n")
    # addList = add_cards(inventory, addListSetcodes, apiDatabase)
    # print("add card list:\n", addList, "\n")
    # removeList = remove_cards(inventory, removeListSetcodes)
    # print("remove card list:\n", removeList, "\n")
    # input("enter")
    # finalList = combine_lists(addList, removeList)
    # print("complete list:\n", finalList, "\n")
    


main()