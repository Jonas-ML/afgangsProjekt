
from apiClient import *
from customtkinter import *
import customtkinter as ctk
from dataFormatter import *

from methods.fetchRepos import fetchRepos




a = restClient()
app = CTk()
app.geometry("900x900")


# Tab defintions
tabview = ctk.CTkTabview(master=app, width=900, height=900)
tabview.pack()
user_tab = tabview.add("tab 1")
search_tab = tabview.add("tab 2")
tabview._segmented_button.grid(sticky="NSEW") #Sørger for tabs er i en relativ præsentabel postion

def getUserName():
    name = user_entry.get()
    response, status_code = a.get(f"users/{name}/repos")
    if status_code == 200:
        repoRes = formatResponse(response)
        repo_options = fetchRepos(repoRes)
        if repo_options:
            repo_combo = ctk.CTkComboBox(user_tab, values=repo_options, command=comboChoice)
            repo_combo.pack(pady=10) 
        else:
            print("No repos found for this user. Did you supply the correct username?")
    else:
        print(f"Error fetching data: {status_code}")


def comboChoice(choice): # Event handler for dropdown box
    name = user_entry.get()
    response, status_code = a.get(f"repos/{name}/{choice}/commits")
    if status_code == 200:
        choiceSelection = formatResponse(response)
        formattedRes = formatCommits(choiceSelection)
        print(formattedRes)
    else:
        print(f"Cant fetch the specified repo: {status_code}")

    


#Put stuff in tab 1 - User tab
user_entry = ctk.CTkEntry(user_tab, placeholder_text="Github username:")
user_entry.pack(pady=40)

user_button = ctk.CTkButton(user_tab, text="Submit", command=getUserName)
user_button.pack(pady=40)


#TEXT WIDGET
txtFrame = ctk.CTkFrame(search_tab)
txtFrame.pack(pady=30)

txtWidget = ctk.CTkTextbox(search_tab,
    width=200,
    height=200)
txtWidget.pack(pady=30)

delete_button = ctk.CTkButton(txtFrame, text="Delete")
paste_button = ctk.CTkButton(txtFrame, text="Paste")
save_button = ctk.CTkButton(txtFrame, text="Save as")

delete_button.grid(row=5, column=0, pady=20)
paste_button.grid(row=5, column=1, pady=20)
save_button.grid(row=5, column=2, pady=20)

app.mainloop()

