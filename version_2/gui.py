from tkinter import *
from update_inventory import import_json_file
from update_inventory import import_cached_API
from update_inventory import import_update_file
from update_inventory import import_all_API
from update_inventory import write_to_json  # Is this and the next line the same code in the library?
from update_inventory import write_to_cache
from update_inventory import add_cards
from tkinter.messagebox import showinfo

# GLOBALS - figure out way to avoid these
FILE_inventory = "./inventory.json"
FILE_API_cache = "./API_cache.json"

API_URL_info = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

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

    # QUESTION: what should the master window here be?
    ent_inventoryFile = Entry(master = window_updateInventory, textvariable = "inventory.json", width = 25)
    btn_updateFileName = Button(master = window_updateInventory, text = "Update File", width = 25, command = lambda : update_inventory_file(ent_inventoryFile.get()))

    ent_inventoryFile.pack(pady = 5)
    btn_updateFileName.pack(pady = 5)

    ent_inventoryFile.insert(0, "inventory.json")    

# Function to do:
#   o Alphabetize owned list
# COMPLETE
def show_inventory():
    window_showInventory = Toplevel(window_main)
    # window_showInventory.config(bg = 'dimgray')
    window_showInventory.title("Simple Inventory")
    inventory = import_json_file(FILE_inventory)

    inventory = sorted(inventory, key = lambda k: k['name'])

    x = 0
    y = 0
    keys = ['owned', 'name', 'setcode']

    for card in inventory:
        print(card)
        print(len(card))
        if x == 0:
            for a in range(3):
                frm_grid = Frame(master = window_showInventory, relief = RAISED)
                frm_grid.grid(row = 0, column = a)            
                lbl_grid1 = Label(master = frm_grid, text = keys[a].upper())
                lbl_grid1.pack(padx = 2)
            x += 1
        for col in range(len(card)):
            data = card[keys[y]]
            print(data)
            frm_grid = Frame(master = window_showInventory, relief = RAISED)
            frm_grid.grid(row = x, column = y)            
            lbl_grid = Label(master = frm_grid, text = data)
            lbl_grid.pack(padx = 2)
            y += 1
        x += 1
        y = 0

# Function to do;
#   center text and buttons dynamically
# COMPLETE
def simple_inventory():
    window_simpleInventory = Toplevel(window_main)
    window_simpleInventory.configure(bg = 'dimgray')
    window_simpleInventory.geometry("400x300")

    window_simpleInventory.title("Simple Inventory Menu")

    lbl_currentFile = Label(master = window_simpleInventory, text = "Current Inventory File: inventory.json", background = 'dimgray', foreground = 'white')

    btn_updateFile = Button(master = window_simpleInventory, text = "Update Inventory File", width = 25, command = update_inventory_file_window)
    btn_viewInventory = Button(master = window_simpleInventory, text = "View Inventory", width = 25, command = show_inventory)

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

window_main = Tk(className="YuGiOh Inventory")
window_main.configure(bg='dimgray')
window_main.geometry("400x300")

lbl_greeting = Label(text = "Welcome to Your Inventory Management!", background = 'dimgray', foreground = 'white')

btn_viewInventorySimple = Button(text = "View Simple Inventory", width = 25, command = simple_inventory)
btn_viewInventoryDetailed = Button(text = "View Detailed Inventory", width = 25)
btn_addToInventory = Button(text = "Add To Your Inventory", width = 25, command = add_to_inventory_window)
btn_removeFromInventory = Button(text = "Remove From Your Inventory", width = 25)
btn_searchInventory = Button(text = "Search For A Card", width = 25)
btn_updateAPICache = Button(text = "Update the API Cache", width = 25, command = update_API_window)

lbl_greeting.pack(pady = 10)
btn_viewInventorySimple.pack(pady = 5)
btn_viewInventoryDetailed.pack(pady = 5)
btn_addToInventory.pack(pady = 5)
btn_removeFromInventory.pack(pady = 5)
btn_searchInventory.pack(pady = 5)
btn_updateAPICache.pack(pady = 5)

window_main.mainloop()