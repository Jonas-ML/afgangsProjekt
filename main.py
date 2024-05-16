
from apiClient import *
from customtkinter import *
import customtkinter as ctk
from formatMethods import *




class gitApp:
    def __init__(self):
        self.a = restClient()
        self.app = ctk.CTk()
        self.app.geometry("1200x800")
        self.create_widgets()
        self.dropdowns = {}
        
    def createWidgets(self):
        self.createTabs()


    def createTabs(self):
        tabview = ctk.CTkTabview(master=app, width=900, height=900)
        tabview.pack()
        user_tab = tabview.add("tab 1")
        search_tab = tabview.add("tab 2")
        tabview._segmented_button.grid(sticky="NSEW") #Sørger for tabs er i en relativ præsentabel postion








def repoChoice():
    name = user_entry.get()
    response, status_code = a.get(f"users/{name}/repos")
    if status_code == 200:
        repoRes = formatResponse(response)
        repo_options = fetchRepos(repoRes)
        if repo_options:
            if name not in dropdowns:
                dropdowns[name] = {}
            if 'repo_combo' not in dropdowns[name]:
                repo_combo = ctk.CTkComboBox(user_tab, values=repo_options, command=lambda event=None: branchChoice(name, repo_combo.get()))
                repo_combo.pack(pady=1)
                dropdowns[name]['repo_combo'] = repo_combo
        else:
            print("No repos found for this user. Did you supply the correct username?")
    else:
        print(f"Error fetching data: {status_code}")
    

def branchChoice(name, choosen_repo):
    response, status_code = a.get(f"repos/{name}/{choosen_repo}/branches")
    if status_code == 200:
        branchRes = formatResponse(response)
        branch_options = fetchRepos(branchRes)
        if branch_options:
            if 'branch_combo' not in dropdowns[name]:
                branch_combo = ctk.CTkComboBox(user_tab, values=branch_options, command=lambda event=None: getCommits(name, choosen_repo, branch_combo.get()))
                branch_combo.pack(pady=5)
                dropdowns[name]['branch_combo'] = branch_combo
        else:
            print("Couldnt fetch branches for this repo")
    else:
        print(f"Error fetching data {status_code}")
    
def getCommits(name, choosen_repo, choosen_Branch):
    response, status_code = a.get(f"repos/{name}/{choosen_repo}/commits", params={"sha" : choosen_Branch})
    if status_code == 200:
        commits_raw = formatResponse(response)
        commits_pretty = formatCommits(commits_raw)
        my_text.insert(END, commits_pretty)
        clearDropdowns(name)
        tabview.set("tab 2")
    
    else:
        print(f"Error fetching data {status_code}")


 


# Funtions for textwidget
def delete():
    my_text.delete(0.0, "end")

def save():
    dialog = ctk.CTkInputDialog(text="What would you like your file to be named", title="Save file")
    fileName = dialog.get_input()
    txt = my_text.get(0.0, END)
    if fileName:
        txtFile = open(f"{fileName}.txt", "w")
        txtFile.write(f"{txt}")
        txtFile.close()
        
        
def clearDropdowns(name):
    if name in dropdowns and 'repo_combo' in dropdowns[name]:
        dropdowns[name]['repo_combo'].destroy()
        del dropdowns[name]['repo_combo']
    if name in dropdowns and 'branch_combo' in dropdowns[name]:
        dropdowns[name]['branch_combo'].destroy()
        del dropdowns[name]['branch_combo']
    

#Put stuff in tab 1 - User tab
user_entry = ctk.CTkEntry(user_tab, placeholder_text="Github username:")
user_entry.pack(pady=40)

user_button = ctk.CTkButton(user_tab, text="Submit", command=repoChoice)
user_button.pack(pady=40)

my_text= ctk.CTkTextbox(search_tab,
    width=600,
    height=400,
    corner_radius=1,)

my_text.pack(pady =10)

txt_frame = ctk.CTkFrame(search_tab)
txt_frame.pack(pady=130)

#Buttons
delete_button = ctk.CTkButton(txt_frame, text="Delete", command=delete)
#paste_button = ctk.CTkButton(txt_frame, text="Paste")
save_button = ctk.CTkButton(txt_frame, text="Save", command=save)

delete_button.grid(row=2, column=0, padx=2)
#paste_button.grid(row=2, column=1, padx=5)
save_button.grid(row=2, column=2)
#app.mainloop()

