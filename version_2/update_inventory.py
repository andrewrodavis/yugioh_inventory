import json
import requests

URL_API_setcode = "https://db.ygoprodeck.com/api/v7/cardsetsinfo.php?setcode="
URL_API_name = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name="
URL_API_info = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

FILE_API_cache = "./API_cache.json"
FILE_inventoryBasic = "./inventory_basic.json"
FILE_addList = "./add_file.txt"

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
def import_add_update_file(file_name):
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
        
def add_cards(addList, inventoryBasic, apiCache):
    print("Adding cards")
    goodAdds = 0
    badAdds = 0
    errorList = []
    
    for newCard in addList:
        brandNewCard = False

        for oldCard in inventoryBasic:
            if newCard.lower() == oldCard['setcode'].lower():
                goodAdds += 1
                oldCard['owned'] += 1
                brandNewCard = False
                break
            else:
                brandNewCard = True
        cardFound = False
        if brandNewCard == True:
            newCardInfo = []
            for data in apiCache:
                for code in data['card_sets']:
                    if newCard.lower() == code.lower():
                        newCardInfo.append(newCard)
                        newCardInfo.append(data['name'])
                        newCardInfo.append(1)
                        cardFound = True
                        break
        if cardFound == False:
            badAdds += 1
            errorList.append(newCard)

data = import_cached_API(FILE_API_cache)
x = 0
for card in data:
    if x < 11:
        print(card['name'])
    x += 1
# data = import_json_file(FILE_inventoryBasic)
# for card in data:
#     print("name: ", card['name'])