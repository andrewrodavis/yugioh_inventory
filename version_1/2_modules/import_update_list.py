# Testing
from import_inventory import import_inventory

def import_new_data(fname):
    # Initialize variables
    addCard = True
    addList = []
    removeList = []
    addCount = 0
    removeCount = 0

    with open(fname, 'r') as f:
        lines = f.readlines()
        for row in lines:
            row = row.rstrip()
            if row == '+':
                continue
            elif row == "-":
                addCard = False
            else:
                if addCard:
                    addList.append(row)
                    addCount += 1
                else:
                    removeList.append(row)
                    removeCount += 1
    return addList, removeList, addCount, removeCount
        
# add, remove = import_new_data("../1_update_inventory.txt")
# print("add: ", add)
# print("remove: ", remove)