import json

def write_to_inventory(fname, writeList):
    print("in write to inventory")
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(writeList, f, ensure_ascii=False, indent=4)


def write_to_cache(fname, jsonList):
    print("In write to inventory")
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(jsonList, f, ensure_ascii=False, indent=4)

def write_to_deck_building(fname, writeList):
    print("in write to deck building")