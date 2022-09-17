# Testing

def import_new_data(fname):
    # Initialize variables
    addCard = True
    addList = []
    removeList = []

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
                else:
                    removeList.append(row)
    return addList, removeList
        
add, remove = import_new_data("../1_update_inventory.txt")
print("add: ", add)
print("remove: ", remove)