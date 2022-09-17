import requests
import json

APISetCodeURL = "https://db.ygoprodeck.com/api/v7/cardsetsinfo.php?setcode="
APINameURL = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name="

def import_setcode_data(setcode):
    JSONPackage = ""

    url = APISetCodeURL + setcode
    response_API = requests.get(url)

    if response_API.status_code == 404:
        print("Status 404 on card ", setcode)
        return [404, setcode]
    
    data = response_API.text

    JSONPackage = json.loads(data)

    return JSONPackage

def import_name_data(name):
    JSONPackage = ""

    url = APINameURL + name
    response_API = requests.get(url)

    if response_API.status_code == 404:
        print("Status 404 on card ", name)
        return [404, name]
    
    data = response_API.text

    JSONPackage = json.loads(data)

    return JSONPackage

# print("name: ", card['name'])