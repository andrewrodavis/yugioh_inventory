import tkinter as tk

# def populate(frame):
#     for x in range(100):
#         for y in range(4):
#             frameGrid = tk.Frame(master=root, relief=tk.RAISED, borderwidth=2)
#             frameGrid.grid(row=x, column=y)
#             labelGrid = tk.Label(master=frameGrid, text=f"Row No. {x}\nColumn No. {y}")
#             labelGrid.pack()

def populate(frame):
    '''Put in some fake data'''
    for x in range(100):
        for y in range(4):
            # frame.grid(row = x, column = y)
            tk.Label(frame, text=f"Row No. {x}\nColumn No. {y}").grid(row=x, column=y)
            # t="this is the second column for x %s" %x
            # tk.Label(frame, text=t).grid(row=x, column=y)

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, relief = tk.RAISED, borderwidth = 2, background="#ffffff")
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

root.mainloop()
