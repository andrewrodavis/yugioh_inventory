from tkinter import *
from update_inventory import import_json_file
from update_inventory import import_cached_API
from update_inventory import import_update_file
from update_inventory import import_all_API
from update_inventory import write_to_json  # Is this and the next line the same code in the library?
from update_inventory import write_to_cache
from update_inventory import add_cards
from update_inventory import remove_from_inventory
from tkinter.messagebox import showinfo, showerror

# GLOBALS - figure out way to avoid these
FILE_inventory = "./inventory.json"
FILE_API_cache = "./API_cache.json"

API_URL_info = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
URL_API_pricing = "https://yugiohprices.com/api/price_for_print_tag/"

# COMPLETE - updates the file value
def update_inventory_file(newFile):
    global FILE_inventory 
    FILE_inventory= newFile
    infoMsg = "The file was updated to " + FILE_inventory + "!"
    showinfo(title = "File Change", message = infoMsg)

# Function to do:
#   toplevel moved to simpleinventory window - currently throws error (function called before defined)
#   error check file name is .json
# COMPLETE - updates the global variable
def update_inventory_file_window():
    window_updateInventory = Toplevel(window_main)
    window_updateInventory.configure(bg = 'dimgray')
    window_updateInventory.title("Update File")

    defaultInventory = StringVar(window_updateInventory, value = "inventory.json")

    # QUESTION: what should the master window here be?
    ent_inventoryFile = Entry(master = window_updateInventory, textvariable = defaultInventory, width = 25)
    btn_updateFileName = Button(master = window_updateInventory, text = "Update File", width = 25, command = lambda : update_inventory_file(ent_inventoryFile.get()))

    ent_inventoryFile.pack(pady = 5)
    btn_updateFileName.pack(pady = 5)

# Function to do:
#   o Check functionality
def get_inventory_stats(inventory):
    totalOwned = 0
    totalValue = 0.00
    overviewStats = []
    
    for card in inventory:
        totalOwned += card['owned']
        totalValue += (card['price'] * card['owned'])
    overviewStats.append(totalOwned)
    overviewStats.append(len(inventory))
    overviewStats.append(format(totalValue, '.2f'))

    return overviewStats

# Scrollbar helper
def onFrameConfigure(canvas):
    canvas.configure(scrollregion = canvas.bbox("all"))
    
# Function to do
def populate(frame, inventory, overviewTitles, overviewStats, keys):
    print("populating")
    # Print inventory overview and stats
    for a in range(len(overviewTitles)):
        lbl = Label(master = frame, text = overviewTitles[a]).grid(row = 0, column = a)
    for a in range(len(overviewStats)):
        lbl = Label(master = frame, text = overviewStats[a]).grid(row = 1, column = a)

    # Print inventory cards
    x = 0
    y = 0

    print("cards")
    for card in inventory:
        if x == 0:
            for a in range(len(keys) + 1):
                if a == 4:
                    lbl = Label(master = frame, text = "UNIT PRICE").grid(row = 2, column = a)
                elif a == 5:
                    lbl = Label(master = frame, text = "COLLECTION PRICES").grid(row = 2, column = a)
                else:
                    lbl = Label(master = frame, text = keys[a].upper()).grid(row = 2, column = a)
            x += 3
        for col in range(len(card) + 1):
            if col < len(card):
                data = card[keys[y]]
            if col == 4:
                price = format(data, '.2f')
                lbl = Label(master = frame, text = price).grid(row = x, column = y)
            elif col < 4:
                lbl = Label(master = frame, text = data).grid(row = x, column = y)
            else:
                totalPrice = format((card['price'] * card['owned']), '.2f')
                lbl = Label(master = frame, text = totalPrice).grid(row = x, column = y)
            y += 1
        x += 1
        y = 0


# Function to do:
#   x Alphabetize owned list
#   o Add scrollbar
def show_inventory(title, showThis):
    window_showInventory = Toplevel(window_main)
    # window_showInventory.config(bg = 'dimgray')
    window_showInventory.title(title)
    window_showInventory.geometry("900x800")


    canvas = Canvas(master = window_showInventory, borderwidth = 0)
    frame = Frame(master = canvas)#, relief = RAISED, borderwidth = 2)
    vsb = Scrollbar(master = window_showInventory, orient = "vertical", command = canvas.yview)
    canvas.configure(yscrollcommand = vsb.set)

    vsb.pack(side = "right", fill = "y")
    canvas.pack(side = "left", fill = "both", expand = True)
    canvas.create_window((4,4), window = frame, anchor = "nw")
    frame.bind("<Configure>", lambda event, canvas = canvas : onFrameConfigure(canvas))

    if showThis == None:
        inventory = import_json_file(FILE_inventory)
        inventory = sorted(inventory, key = lambda k: k['name'])
    else:
        inventory = showThis

    keys = ['owned', 'name', 'rarity', 'setcode', 'price']
    overviewTitles = ['TOTAL OWNED', 'UNIQUE CARDS', 'TOTAL VALUE']
    overviewStats = get_inventory_stats(inventory)

    populate(frame, inventory, overviewTitles, overviewStats, keys)

# Function to do;
#   center text and buttons dynamically
# COMPLETE
def simple_inventory():
    window_simpleInventory = Toplevel(window_main)
    window_simpleInventory.configure(bg = 'dimgray')
    # window_simpleInventory.geometry("400x300")

    window_simpleInventory.title("Simple Inventory Menu")

    lbl_currentFile = Label(master = window_simpleInventory, text = "Current Inventory File: inventory.json", background = 'dimgray', foreground = 'white')

    btn_updateFile = Button(master = window_simpleInventory, text = "Update Inventory File", width = 25, command = update_inventory_file_window)
    btn_viewInventory = Button(master = window_simpleInventory, text = "View Inventory", width = 25, command = lambda : show_inventory("Simple Inventory", None))

    lbl_currentFile.pack(pady = 5)
    btn_updateFile.pack(pady = 5)
    btn_viewInventory.pack(pady = 5)

# Function to do:
#   error check on file name - check if file exists
#   Print error messages to user
# COMPLETE except ^^
def add_to_inventory(fileName):
    print("File: ", fileName)
    #Function to add: add_cards(addList, inventoryBasic, apiCache)
    addList = import_update_file(fileName)
    inventoryBasic = import_json_file(FILE_inventory)
    api_data = import_cached_API(FILE_API_cache)

    goodAddCount, badAddCount, errorList, inventory = add_cards(addList, inventoryBasic, api_data)
    print("Good Adds: ", goodAddCount)
    print("Bad Adds: ", badAddCount)
    print("Errors: ", errorList)
    print("inventory: ", inventory)

    write_to_json(inventory)
    
    infoMsg = str(goodAddCount) + " Card(s) Successfully Added!\n" + str(badAddCount) + " Card(s) Not Added.\n" + "Error on setcodes: \n"
    for code in errorList:
        msg = "\t" + code + "\n"
        infoMsg += msg
    showinfo(title = "Inventory Update Message", message = infoMsg)

# Function to do:
#   determine best way to add - input file or let user type all the setcodes here?
#   Potential issue where text box keeps appending to the file name
# COMPLETE except ^^
def add_to_inventory_window():
    window_addInventory = Toplevel(window_main)
    window_addInventory.configure(bg = 'dimgray')
    window_addInventory.geometry("600x300")
    window_addInventory.title("Add to Inventory")

    defaultEntry = StringVar(window_addInventory, value = "add_file.txt")
    
    # QUESTION: what should the master window here be?
    lbl_instructions1 = Label(master = window_addInventory, text = "Instructions:", background = "dimgray", foreground = "white")
    lbl_instructions2 = Label(master = window_addInventory, text = "1. Ensure the file name in the box matches the file name with your setcodes", background = "dimgray", foreground = "white", anchor = "w")
    lbl_instructions3 = Label(master = window_addInventory, text = "2. Format your text file with one setcode per line. For example:\nsdk-001\nsdk-002\n...", background = "dimgray", foreground = "white")
    lbl_instructions4 = Label(master = window_addInventory, text = "3. Click the 'Add to Your Inventory' button", background = "dimgray", foreground = "white")
    ent_addFile = Entry(master = window_addInventory, textvariable = defaultEntry, width = 25)
    btn_updateFileName = Button(master = window_addInventory, text = "Add to Your Inventory", width = 25, command = lambda : add_to_inventory(ent_addFile.get()))

    lbl_instructions1.pack()
    lbl_instructions2.pack()
    lbl_instructions3.pack()
    lbl_instructions4.pack()
    ent_addFile.pack(pady = 5)
    btn_updateFileName.pack(pady = 5)

# Function to do
# COMPLETE
def update_API(fileName):
    print(fileName)
    apiList = import_all_API(API_URL_info)
    write_to_cache(fileName, apiList)
    
    showinfo(title = "Success Message", message = "The API Cache has been Updated!")


# Function to do
# COMPLETE
def update_API_window():
    window_updateAPI = Toplevel(window_main)
    window_updateAPI.configure(bg = 'dimgray')
    window_updateAPI.geometry("600x300")
    window_updateAPI.title("Update Cache")

    cacheMsg = StringVar(window_updateAPI, value = "API_cache.json")

    lbl_instructions = Label(master = window_updateAPI, background = 'dimgray', foreground = 'white', text = "Type the file location you would like to store the API cache\nLeave as is for default location")
    ent_fileLocation = Entry(master = window_updateAPI, textvariable = cacheMsg, width = 25)
    btn_updateCache = Button(master = window_updateAPI, text = "Update Cache", width = 25, command = lambda : update_API(ent_fileLocation.get()))

    lbl_instructions.pack(pady = 10)
    ent_fileLocation.pack()
    btn_updateCache.pack()

# Function to do:
#
def search_for_card(name):
    print("searching 2")
    inventory = import_json_file(FILE_inventory)
    
    name = name.replace('-', ' ')
    name = name.replace('/', ' ')
    name = name.replace('!', ' ')
    name = name.replace('\\', ' ')
    name = name.lower()
    
    matchList = []

    for card in inventory:
        normalized = card['name']
        normalized = normalized.replace('-', ' ')
        normalized = normalized.replace('/', ' ')
        normalized = normalized.replace('!', ' ')
        normalized = normalized.replace('\\', ' ')
        normalized = normalized.lower()
        
        if name in normalized:
            matchList.append(card)
        else:
            continue
    if len(matchList) == 0:
        msg = name.upper() + " was not found in your inventory"
        showerror(title = "Not Found", message = msg)
    else:
        show_inventory("Search Results", matchList)
        # window_showSearchedCards = Toplevel(window_main)
        # window_showSearchedCards.title("Search Results")
        # matchList = sorted(matchList, key = lambda k: k['name'])
        


# Function to do:
#
def search_window():
    print("searching")
    window_search = Toplevel(window_main)
    window_search.configure(bg = 'dimgray')
    window_search.title("Search Menu")

    lbl_greetingSearch = Label(master = window_search, background = 'dimgray', foreground = 'white', text = "Welcome to Your Inventory Search!")
    lbl_instructionsSearch = Label(master = window_search, background = 'dimgray', foreground = 'white', text = "Enter the card name to search for")
    ent_searchBox = Entry(master = window_search, width = 25)
    btn_search = Button(master = window_search, text = "Search Inventory", width = 25, command = lambda : search_for_card(ent_searchBox.get()))

    lbl_greetingSearch.pack(pady = 10)
    lbl_instructionsSearch.pack(pady = 5)
    ent_searchBox.pack(pady = 5)
    btn_search.pack()

# Function to do
#
def remove_from_inventory_gui(fileName):
    inventory = import_json_file(FILE_inventory)
    removeList = import_update_file(fileName)
    inventoryBasic, goodRemoves, errorRemoves, errorRemoveList = remove_from_inventory(removeList, inventory)

    write_to_json(inventoryBasic)

    infoMsg = str(goodRemoves) + " Card(s) Successfully Added!\n" + str(errorRemoves) + " Card(s) Not Added.\n" + "Error on setcodes: \n"
    for code in errorRemoveList:
        msg = "\t" + code + "\n"
        infoMsg += msg
    showinfo(title = "Inventory Update Message", message = infoMsg)
# Function to do
#
def remove_window():
    window_remove = Toplevel(window_main)
    window_remove.configure(bg = 'dimgray')
    window_remove.title("Remove Menu")

    defaultEntry = StringVar(window_remove, value = "remove_file.txt")
    
    # QUESTION: what should the master window here be?
    lbl_instructions1 = Label(master = window_remove, text = "Instructions:", background = "dimgray", foreground = "white")
    lbl_instructions2 = Label(master = window_remove, text = "1. Ensure the file name in the box matches the file name with your setcodes", background = "dimgray", foreground = "white", anchor = "w")
    lbl_instructions3 = Label(master = window_remove, text = "2. Format your text file with one setcode per line. For example:\nsdk-001\nsdk-002\n...", background = "dimgray", foreground = "white")
    lbl_instructions4 = Label(master = window_remove, text = "3. Click the 'Remove From Your Inventory' button", background = "dimgray", foreground = "white")
    ent_removeFile = Entry(master = window_remove, textvariable = defaultEntry, width = 25)
    btn_updateFileName = Button(master = window_remove, text = "Remove From Your Inventory", width = 25, command = lambda : remove_from_inventory_gui(ent_removeFile.get()))

    lbl_instructions1.pack()
    lbl_instructions2.pack()
    lbl_instructions3.pack()
    lbl_instructions4.pack()
    ent_removeFile.pack(pady = 5)
    btn_updateFileName.pack(pady = 5)


window_main = Tk(className="YuGiOh Inventory")
window_main.configure(bg='dimgray')
# window_main.geometry("400x300")

lbl_greeting = Label(text = "Welcome to Your Inventory Management!", background = 'dimgray', foreground = 'white')

btn_viewInventorySimple = Button(text = "View Simple Inventory", width = 25, command = simple_inventory)
btn_viewInventoryDetailed = Button(text = "View Detailed Inventory", width = 25)
btn_addToInventory = Button(text = "Add To Your Inventory", width = 25, command = add_to_inventory_window)
btn_removeFromInventory = Button(text = "Remove From Your Inventory", width = 25, command = remove_window)
btn_searchInventory = Button(text = "Search For A Card", width = 25, command = search_window)
btn_updateAPICache = Button(text = "Update the API Cache", width = 25, command = update_API_window)
# This can be viewed by viewing simple inventory -- probably not needed here
btn_viewInventoryPricing = Button(text = "View Inventory Value", width = 25)

lbl_greeting.pack(pady = 10)
btn_viewInventorySimple.pack(pady = 5)
btn_viewInventoryDetailed.pack(pady = 5)
btn_addToInventory.pack(pady = 5)
btn_removeFromInventory.pack(pady = 5)
btn_searchInventory.pack(pady = 5)
btn_updateAPICache.pack(pady = 5)
btn_viewInventoryPricing.pack(pady = 5)

window_main.mainloop()