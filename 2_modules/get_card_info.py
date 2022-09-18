from import_API import import_all_API, import_setcode_data, import_name_data

def get_card_info(setcode, apiData):
    bool_cardFound = False
    errorMsg = "ERROR Setcode not found: "
    for card in apiData:
        try:
            for setcodeList in card['card_sets']:
                if setcode == setcodeList['set_code']:
                    cardData = {
                        "name" : card['name'],
                        "set_code" : setcode,
                        "type" : card['type'],
                        "lowest_card_prices" : [
                            {
                                "tcgplayer_price" : card['card_prices'][0]['tcgplayer_price'],
                                "tcgplayer_price" : card['card_prices'][0]['ebay_price']
                            }
                        ],
                        "number_owned" : 1
                    }
                    bool_cardFound = True
                    break
        except:
            continue
        if bool_cardFound:
            bool_cardFound = False
            break
        else:
            cardData = errorMsg + setcode
    return cardData
def get_card_info_2(setcode, apiData):
    cardName = import_setcode_data(setcode)['name']
    cardImport = import_name_data(cardName)['data'][0]
    # print("Card Data: ", cardImport)
    # print("\ntier 1: ", cardImport)
    # print("\ntier 2: ", cardImport['card_prices'])
    cardData = {
        "name" : cardImport['name'],
        "set_code" : setcode,
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

# apiDatabase = import_all_API()
# list = ['FOTB-EN043', 'GLAS-EN062', 'MRD-098']
# data = get_card_info(list, apiDatabase)
# print(data)