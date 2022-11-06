import json

jsonFile = "inventory.json"

file = open(jsonFile)

data = json.load(file)

for i in data:
    print(i['setcode'])

file.close()