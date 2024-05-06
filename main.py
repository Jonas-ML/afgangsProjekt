
from apiClient import *
from customtkinter import *
import customtkinter as ctk
from formatMethods import *





a = restClient()
app = CTk()
app.geometry("1200x800")


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
            repo_combo.pack(pady=1) 
        else:
            print("No repos found for this user. Did you supply the correct username?")
    else:
        print(f"Error fetching data: {status_code}")


def comboChoice(choice): # Event handler for dropdown box
    name = user_entry.get()
    response, status_code = a.get(f"repos/{name}/{choice}/commits")
    if status_code == 200:
        choiceSelection = formatResponse(response)
        commit_details = formatCommits(choiceSelection)
        print(commit_details)
        my_text.insert(END, commit_details)
    else:
        print(f"Cant fetch the specified repo: {status_code}")


# Funtions for textwidget
def delete():
    my_text.delete(0.0, "end")




#Put stuff in tab 1 - User tab
user_entry = ctk.CTkEntry(user_tab, placeholder_text="Github username:")
user_entry.pack(pady=40)

user_button = ctk.CTkButton(user_tab, text="Submit", command=getUserName)
user_button.pack(pady=40)

my_text= ctk.CTkTextbox(search_tab)
my_text.pack(pady =110)

txt_frame = ctk.CTkFrame(search_tab)
txt_frame.pack(pady=130)

#Buttons
delete_button = ctk.CTkButton(txt_frame, text="Delete", command=delete)
paste_button = ctk.CTkButton(txt_frame, text="Pase")
save_button = ctk.CTkButton(txt_frame, text="Save")

delete_button.grid(row=2, column=0)
paste_button.grid(row=2, column=1, padx=5)
save_button.grid(row=2, column=2)
app.mainloop()

