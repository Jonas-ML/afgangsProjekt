import requests
from apiClient import *
import json
from customtkinter import *
import customtkinter as ctk

app = CTk()
app.geometry("900x900")


# Tab defintions
tabview = ctk.CTkTabview(master=app, width=900, height=900)
tabview.pack()
user_tab = tabview.add("tab 1")
search_tab = tabview.add("tab 2")
tabview._segmented_button.grid(sticky="NSEW") #Sørger for tabs er i en relativ præsentabel postion

#Put stuff in tab 1 - User tab
user_entry = ctk.CTkEntry(user_tab, placeholder_text="Github username:")
user_entry.pack(pady=40)
user_button = ctk.CTkButton(user_tab, text="Confirm")
user_button.pack(pady=40)


app.mainloop()

""" def tab_state(enabled):
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
tabsystem.add(tab1, text="userInfo")
tabsystem.pack(expand=1, fill="both")

label_user = Label(tab1, text="")
label_user.grid(column=2, row=1, padx=40, pady=40)

entry_user = ttk.Entry(tab1)
entry_user.insert(0, "Github Username:")
entry_user.grid(column=2, row=1, padx=40, pady=40)
# EO Tab 1

#Tab 2 - search
tab2 = Frame(tabsystem)
tabsystem.add(tab2, text="searchRepo")
tabsystem.pack(expand=1, fill="both")

#Dropdown NEEDS VARIABLE API DATA FOR OPTIONS -----------------------------
options = [
    "Heil",
    "Hitler"
]
clicked = StringVar()
clicked.set("Heil")
dropDown = OptionMenu(tab2, clicked, *options)
dropDown.grid(row=0, column=0, padx=10, pady=10)

#root.after(100, tab_state(False)) # COMMENT/UNCOMMENT FOR AT FÅ LOGIN TIL AT DEACTIVATE/ACTIVATE #

root.mainloop() """