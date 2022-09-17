import sys

# Append the modules list
sys.path.append("./2_modules")

# Import all relevant modules
from import_list import import_new_data
from import_API import import_API_data
from remove_cards import remove_cards
from write_file import write_to_inventory, write_to_deck_building
from add_cards import add_cards

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
        print("Correct script usage: 'python3 0_update.py <update file> <inventory file> <output file>'")
        sys.exit("Please try again\n----------------------------")
    return argv[1], argv[2], argv[3]

def main():
    inputFile, inventoryFile, outputFile = get_args(sys.argv)


main()