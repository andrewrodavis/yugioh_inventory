import json
import requests

URL_API_setcode = "https://db.ygoprodeck.com/api/v7/cardsetsinfo.php?setcode="
URL_API_name = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name="
URL_API_info = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

URL_API_pricing = "https://yugiohprices.com/api/price_for_print_tag/"

FILE_API_cache = "./API_cache.json"
FILE_inventoryBasic = "./inventory.json"
FILE_addList = "./add_file.txt"
FILE_removeList = "./remove_file.txt"

# COMPLETE - successfully import the cached api database
def import_cached_API(fname):
    with open(fname, 'r') as f:
        data = json.load(f)
        return data

# COMPLETE - successfully import the entire api database from the website
def import_all_API(url):
    JSONPackage = ""

    response_API = requests.get(url)

    if response_API.status_code == 404:
        print("Status 404 on card ")
        return [404]
    
    data = response_API.text

    JSONPackage = json.loads(data)

    #JSONPackage['data'] -- then iterate over list and use keywords

    return JSONPackage['data']

# COMPLETE - successfully writes the entire api database to cache
def write_to_cache(fname, jsonList):
    print("In write to inventory")
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(jsonList, f, ensure_ascii=False, indent=4)

# COMPLETE - imports and returns file information
def import_update_file(file_name):
    print("importing the add file")
    data = []
    with open(file_name, "r") as f:
        for line in f:
            data.append(line)
    return data

# COMPLETE - imports and returns file information
def import_json_file(file_name):
    print("Imporing json information")
    with open(file_name, 'r') as f:
        return json.load(f)   
    
# COMPLETE - adds cards to dictionary list to be written to updated inventory file; provides errors and success counts/lists
def add_cards(addList, inventoryBasic, apiCache):
    goodAdds = 0
    badAdds = 0
    errorList = []

    for newCard in addList:
        brandNewCard = False    # assumes that the card is not new, already in inventory
        # print("NEWNEW: ", newCard)
        # input()
        for oldCard in inventoryBasic:
            if newCard.strip().lower() ==  oldCard['setcode'].lower():
                goodAdds += 1
                oldCard['owned'] += 1
                brandNewCard = False
                break
            else:
                brandNewCard = True
        cardFound = False
        if brandNewCard == True:    # indicates the card needs to be pulled from the api cache
            newCardInfo = {'setcode' : None, 'name' : None, 'owned' : 0, 'price' : 0.00}
            for data in apiCache:
                if 'card_sets' in data:
                    for setCode in data['card_sets']:
                        if newCard.strip().lower() == setCode['set_code'].lower():
                            newCardInfo['setcode'] = newCard.strip()
                            newCardInfo['name'] = data['name']
                            newCardInfo['owned'] += 1
                            newCardInfo['price'] = get_pricing(newCardInfo['setcode'].upper(), URL_API_pricing)

                            goodAdds += 1
                            inventoryBasic.append(newCardInfo)
                            cardFound = True
                            # print("ADDED ", newCard)
                            break
                else:
                    continue
        if brandNewCard == True and cardFound == False:  # Means the setcode to add was not found in api data
            badAdds += 1
            errorList.append(newCard)
                    
    return goodAdds, badAdds, errorList, inventoryBasic

# COMPLETE - writes in correct json format to json file
def write_to_json(data):
    with open(FILE_inventoryBasic, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# COMPLETE - removes from inventory and returns error/good count and error list
def remove_from_inventory(removeList, inventory):
    goodRemoves = 0
    errorRemoves = 0
    errorRemoveList = []
    updatedInventory = []

    print("\n-----")
    for removeCard in removeList:
        print("Card: ", removeCard)
        cardRemoved = False
        for inventoryCard in inventory:
            if removeCard.strip().lower() == inventoryCard['setcode'].lower():
                if inventoryCard['owned'] > 1:
                    inventoryCard['owned'] -= 1
                    goodRemoves += 1
                    cardRemoved = True
                    break
                elif inventoryCard['owned'] == 0 or inventoryCard['owned'] == 1:
                    inventory.remove(inventoryCard)
                    goodRemoves += 1
                    cardRemoved = True
                    break
                else:
                    cardRemoved = False
        if cardRemoved == False:
            errorRemoveList.append(removeCard)
            errorRemoves += 1
        
    print("-----\n")
    return inventory, goodRemoves, errorRemoves, errorRemoveList

# Function
# Get the pricing of the card based off of the setcode
def get_pricing(setcode, url):
    # Pull the json data
    JSONPackage = ""
    url = url + setcode.upper()
    print("url: ", url)

    response_API = requests.get(url)
    print("response: ", response_API)
   
    data = response_API.text
    JSONPackage = json.loads(response_API.text)
    if JSONPackage['status'] == "fail":
        return "Error retrieving"
    else:
        JSONPackage = json.loads(data)
        print(JSONPackage['status'])
        print(JSONPackage)
        return JSONPackage['data']['price_data']['price_data']['data']['prices']['average']
        

# get_pricing("sdy-046", URL_API_pricing)
# print(import_all_API(URL_API_info))

# data = import_cached_API(FILE_API_cache)
# removeList = import_update_file(FILE_removeList)
# inventory = import_json_file(FILE_inventoryBasic)
# addList = import_update_file(FILE_addList)

# goodAdds, badAdds, errorList, inventoryBasic = add_cards(addList, inventory, data)


# print(inventory)
# inventoryBasic, goodRemoves, errorRemoves, errorRemoveList = remove_from_inventory(removeList, inventory)
# print(inventory)
# print("Good Removes: ", goodRemoves)
# print("Errors: ", errorRemoves)
# print("Error List: ", errorRemoveList)
# write_to_json(inventoryBasic)

# DEBUGGING for add->add inventory->write file
# addList = import_update_file(FILE_addList)
# inventory = import_json_file(FILE_inventoryBasic)
# write_basic_inventory(inventoryBasic)
# print("Good Add Count: ", goodAdds)
# print("Badd Add Count: ", badAdds)
# print("Error Lilst: ", errorList)
# print("Updated Inventory: ", inventoryBasic)
