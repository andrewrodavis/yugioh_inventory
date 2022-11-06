import requests
import json
import time
apiurl = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
APISetCodeURL = "https://db.ygoprodeck.com/api/v7/cardsetsinfo.php?setcode="
APINameURL = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name="

def import_setcode_data():
    JSONPackage = ""

    response_API = requests.get(apiurl)

    if response_API.status_code == 404:
        print("Status 404 on card ")
        return [404]
    
    data = response_API.text

    JSONPackage = json.loads(data)

    return JSONPackage

time1 = time.time()
package = import_setcode_data()

lists = ["SDK-001", "SDK-002", "SDK-003", "SDK-004"]

# print("\nData: ", package['data'])

for add in lists:
    for card in package['data']:
        try:
            for code in card['card_sets']:
                if add == code['set_code']:
                    newCard = card
                    print("Name: ", newCard['name'])
                    print("Set Code: ", code['set_code'])
                    print("Type: ", newCard['type'])
                    print("Pricing 1: ", newCard['card_prices'][0]['tcgplayer_price'])
                    print("Pricing 2: ", newCard['card_prices'][0]['ebay_price'])
        except:
            # print("Card name: ", card['name'])
            # print("No set codes available")
            continue
time2 = time.time()
print("----------s-s-s-")
time3 = time.time()
# for add in lists:
#     JSONPackage = ""
#     url = APISetCodeURL + add
#     response_API = requests.get(url)
#     data = response_API.text
#     JSONPackage = json.loads(data)
#     print(JSONPackage['name'])

#     url = APINameURL + JSONPackage['name']
#     response_API = requests.get(url)
#     data = response_API.text
#     JSONPackage = json.loads(data)
#     print(JSONPackage)
time4 = time.time()

print("\ntime 1: ", (time2 - time1))
print("\ntime 2: ", (time4 - time3))
    

