import requests
from apiClient import *
import json
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def tab_state(enabled):
    tabs = tabsystem.tabs()
    start_index = 1
    for tab_id in tabs[start_index:]:
        tabsystem.tab(tab_id, state="normal" if enabled else "disabled")


root = Tk()
root.title("Dashboard")
root.configure(background="white")
root.minsize(200, 200)
root.maxsize(1920, 1080)
root.geometry("1200x400+50+50")
tabsystem = ttk.Notebook(root)

#Tab 1 - user info
tab1 = Frame(tabsystem)
tabsystem.add(tab1, text="!H")
tabsystem.pack(expand=1, fill="both")

label_user = Label(tab1, text="")
label_user.grid(column=2, row=1, padx=40, pady=40)

entry_user = ttk.Entry(tab1)
entry_user.insert(0, "Github Username:")
entry_user.grid(column=2, row=1, padx=40, pady=40)



root.after(100, tab_state(False)) # COMMENT/UNCOMMENT FOR AT FÅ LOGIN TIL AT DEACTIVATE/ACTIVATE #

root.mainloop()