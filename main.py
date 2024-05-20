
from apiClient import *
from customtkinter import *
import customtkinter as ctk
from formatMethods import *




class gitApp:
    def __init__(self):
        self.a = restClient()
        self.app = ctk.CTk()
        self.app.geometry("1200x800")
        self.createWidgets()
        self.dropdowns = {}
        self.dataFormatter = dataFormatter()
        
    def createWidgets(self):
        self.createTabs()
        self.createLabels()
        self.createEntryBoxes()
        self.createButtons()
        self.createTxtWidget()


    def createTabs(self):
        self.tabview = ctk.CTkTabview(master=self.app, width=900, height=900)
        self.tabview.pack()
        self.user_tab = self.tabview.add("tab 1")
        self.search_tab = self.tabview.add("tab 2")
        self.tabview._segmented_button.grid(sticky="NSEW") #Sørger for tabs er i en relativ præsentabel postion

    def createLabels(self):
        pass
    
    def createEntryBoxes(self):
        self.user_entry = ctk.CTkEntry(self.user_tab, placeholder_text="Github username:")
        self.user_entry.pack(pady=40)

    def createButtons(self):
        self.user_button = ctk.CTkButton(self.user_tab, text="Submit", command=self.repoChoice)
        self.user_button.pack(pady=40)
        
    def createTxtWidget(self):
        self.my_text= ctk.CTkTextbox(self.search_tab,
        width=800,
        height=600,
        corner_radius=1,)

        self.my_text.pack(pady=10)

        self.txt_frame = ctk.CTkFrame(self.search_tab)
        self.txt_frame.pack(pady=10)
        
        self.delete_button = ctk.CTkButton(self.txt_frame, text="Delete", command=self.delete)
        self.save_button = ctk.CTkButton(self.txt_frame, text="Save", command=self.save)
        self.delete_button.grid(row=2, column=0, padx=2)
        self.save_button.grid(row=2, column=2)
        


    def repoChoice(self):
        name = self.user_entry.get()
        response, status_code = self.a.get(f"users/{name}/repos")
        if status_code == 200:
            repoRes = dataFormatter.formatResponse(response)
            repo_options = dataFormatter.fetchRepos(repoRes)
            if repo_options:
                if name not in self.dropdowns:
                    self.dropdowns[name] = {}
                if 'repo_combo' not in self.dropdowns[name]:
                    repo_combo = ctk.CTkComboBox(self.user_tab, values=repo_options, command=lambda event=None: self.branchChoice(name, repo_combo.get()))
                    repo_combo.pack(pady=1)
                    self.dropdowns[name]['repo_combo'] = repo_combo
            else:
                print("No repos found for this user. Did you supply the correct username?")
        else:
            print(f"Error fetching data: {status_code}")
    

    def branchChoice(self, name, choosen_repo):
        response, status_code = self.a.get(f"repos/{name}/{choosen_repo}/branches")
        if status_code == 200:
            branchRes = dataFormatter.formatResponse(response)
            branch_options = dataFormatter.fetchRepos(branchRes)
            if branch_options:
                if 'branch_combo' not in self.dropdowns[name]:
                    self.branch_combo = ctk.CTkComboBox(self.user_tab, values=branch_options, command=lambda event=None: self.getCommits(name, choosen_repo, self.branch_combo.get()))
                    self.branch_combo.pack(pady=5)
                    self.dropdowns[name]['branch_combo'] = self.branch_combo
            else:
                print("Couldnt fetch branches for this repo")
        else:
            print(f"Error fetching data {status_code}")
    
    def getCommits(self, name, choosen_repo, choosen_Branch):
        response, status_code = self.a.get(f"repos/{name}/{choosen_repo}/commits", params={"sha" : choosen_Branch})
        if status_code == 200:
            commits_raw = dataFormatter.formatResponse(response)
            commits_pretty = dataFormatter.formatCommits(commits_raw)
            self.my_text.insert(END, commits_pretty)
            self.clearDropdowns(name)
            self.tabview.set("tab 2")
        
        else:
            print(f"Error fetching data {status_code}")


    def delete(self):
        self.my_text.delete(0.0, "end")

    def save(self):
        dialog = ctk.CTkInputDialog(text="What would you like your file to be named", title="Save file")
        fileName = dialog.get_input()
        txt = self.my_text.get(0.0, END)
        if fileName:
            txtFile = open(f"{fileName}.txt", "w")
            txtFile.write(f"{txt}")
            txtFile.close()
            
            
    def clearDropdowns(self, name):
        if name in self.dropdowns and 'repo_combo' in self.dropdowns[name]:
            self.dropdowns[name]['repo_combo'].destroy()
            del self.dropdowns[name]['repo_combo']
        if name in self.dropdowns and 'branch_combo' in self.dropdowns[name]:
            self.dropdowns[name]['branch_combo'].destroy()
            del self.dropdowns[name]['branch_combo']
    













app = gitApp()
app.app.mainloop()






