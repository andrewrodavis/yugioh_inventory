from tkinter import *
from update_inventory import *
from tkinter.messagebox import showinfo

# GLOBALS - figure out way to avoid these
FILE_inventory = "./inventory_basic.json"

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

window_main = Tk(className="YuGiOh Inventory")
window_main.configure(bg='dimgray')
window_main.geometry("400x300")

lbl_greeting = Label(text = "Welcome to Your Inventory Management!", background = 'dimgray', foreground = 'white')

btn_viewInventorySimple = Button(text = "View Simple Inventory", width = 25, command = simple_inventory)
btn_viewInventoryDetailed = Button(text = "View Detailed Inventory", width = 25)
btn_addToInventory = Button(text = "Add To Your Inventory", width = 25)
btn_removeFromInventory = Button(text = "Remove From Your Inventory", width = 25)
btn_searchInventory = Button(text = "Search For A Card", width = 25)
btn_updateAPICache = Button(text = "Update the API Cache", width = 25)

lbl_greeting.pack(pady = 10)
btn_viewInventorySimple.pack(pady = 5)
btn_viewInventoryDetailed.pack(pady = 5)
btn_addToInventory.pack(pady = 5)
btn_removeFromInventory.pack(pady = 5)
btn_searchInventory.pack(pady = 5)
btn_updateAPICache.pack(pady = 5)

window_main.mainloop()