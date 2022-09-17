from xml.etree.ElementTree import tostring
from import_API import import_setcode_data, import_name_data

def get_card_info(setcode):
    cardName = import_setcode_data(setcode)['name']
    cardImport = import_name_data(cardName)['data'][0]
    # print("Card Data: ", cardImport)
    # print("\ntier 1: ", cardImport)
    # print("\ntier 2: ", cardImport['card_prices'])
    cardData = {
        "name" : cardImport['name'],
        "sed_code" : setcode,
        "type" : cardImport['type'],
        # "desc" : cardImport['desc'],
        "lowest_card_prices" : [
            {
                "tcgplayer_price" : cardImport['card_prices'][0]['tcgplayer_price'],
                "ebay_price" : cardImport['card_prices'][0]['ebay_price']
            }
        ],
        "number_owned" : 1
    }
    return cardData

# data = get_card_info("MP21-EN138")
# print(data)