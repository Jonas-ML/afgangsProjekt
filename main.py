import requests
from apiClient import *
import json
from customtkinter import *
import customtkinter as ctk
from dataFormatter import *

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
            repo_combo = ctk.CTkComboBox(search_tab, values=repo_options, command=comboChoice)
            repo_combo.pack(pady=40)
        else:
            print("No repos found for this user. Did you supply the correct username?")
    else:
        print(f"Error fetching data: {status_code}")

def fetchRepos(repoRes): # Indexes the json object to extract repo names
    data = json.loads(repoRes)
    repo_options = [repo['name'] for repo in data]
    return repo_options

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

#Put stuff in Search Tab


app.mainloop()

