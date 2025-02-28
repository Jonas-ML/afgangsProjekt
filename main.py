import customtkinter as ctk
from apiClient import restClient
from dataHandling.JSON_Formatter import dataFormatter
from dataHandling.PDFconverter import TextToPDF
from dataHandling.textEditor import TxtWidget
from popupHandler import popupHandler

class gitApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.a = restClient()
        self.geometry("1200x800")
        self.title("Commit extractor")
        self.createWidgets()
        self.dropdowns = {}
        self.dataFormatter = dataFormatter()
        self.choosen_repo = None
        self.choosen_branch = None
    
    def createWidgets(self):
        self.createTabs()
        self.createEntryBoxes()
        self.createButtons()
        self.txtEditor = TxtWidget(self.search_tab, self.popup)

    def createTabs(self):
        self.tabview = ctk.CTkTabview(master=self, width=1200, height=800)
        self.tabview.pack()
        self.user_tab = self.tabview.add("Selection")
        self.search_tab = self.tabview.add("Formatting")
        self.tabview._segmented_button.grid(sticky="NSEW")
    
    def createEntryBoxes(self):
        self.user_entry = ctk.CTkEntry(self.user_tab, placeholder_text="Github username:")
        self.user_entry.pack(pady=40)

    def createButtons(self):
        self.user_button = ctk.CTkButton(self.user_tab, text="Submit", command=self.repoChoice)
        self.user_button.pack(pady=40)
        
    def repoChoice(self):
        name = self.user_entry.get()
        try:
            response, status_code = self.a.get(f"users/{name}/repos")
            if status_code == 200:
                repoRes = dataFormatter().formatResponse(response) # bedre readability
                repo_options = dataFormatter().fetchRepos(repoRes) # extracter repo names
                if repo_options: # if repo navne
                    if name not in self.dropdowns: # laver en dropdown for user hvis den ikke esksisterer
                        self.dropdowns[name] = {}
                    if 'repo_combo' not in self.dropdowns[name]: # laver repo choice dict for user og dropdown med valgene
                        repo_combo = ctk.CTkComboBox(self.user_tab, values=repo_options,
                                                     command=lambda event=None: self.branchChoice(name, repo_combo.get()), # lamdba for at kunne passere multiple arguiments til funktionen
                                                     width=180) # normal eventhandler tager kun 1 argument men med en lambda, kan vi pass flere
                        repo_combo.pack(pady=1)
                        self.dropdowns[name]['repo_combo'] = repo_combo
                else:
                    self.popup(f"No repos found for this user. Did you supply the correct username?")
            else:
                self.popup(f"Error fetching data:\n {status_code}")

        except Exception as e:
            self.popup(f"An error occurred while fetching repositories:\n {e}")
    
    def branchChoice(self, name, chosen_repo):
        try:
            response, status_code = self.a.get(f"repos/{name}/{chosen_repo}/branches")
            if status_code == 200:
                branchRes = dataFormatter().formatResponse(response)
                branch_options = dataFormatter().fetchRepos(branchRes)
                if branch_options:
                    if 'branch_combo' not in self.dropdowns[name]:
                        self.branch_combo = ctk.CTkComboBox(self.user_tab, values=branch_options,
                                                           command=lambda event=None: self.getCommits(name, chosen_repo, self.branch_combo.get()),
                                                           width=180)
                        self.branch_combo.pack(pady=5)
                        self.dropdowns[name]['branch_combo'] = self.branch_combo
                else:
                    self.popup(f"Could not fetch branches for: {chosen_repo}")
            else:
                self.popup(f"Error fetching response data {status_code}")

        except Exception as e:
            self.popup(f"An error occurred while fetching branches for: {chosen_repo}, Error: {e}")

    def getCommits(self, name, chosen_repo, chosen_branch):
        try:
            self.choosen_repo = chosen_repo
            self.choosen_branch = chosen_branch
            response, status_code = self.a.get(f"repos/{name}/{chosen_repo}/commits", params={"sha": chosen_branch})
            if status_code == 200:
                commits_raw = dataFormatter().formatResponse(response)
                commits_pretty = dataFormatter().formatCommits(commits_raw, chosen_repo, chosen_branch) # formatere commits til display i txt editor
                self.txtEditor.commits_pretty = commits_pretty # Skal assignes til txteditor efter modularisering
                self.txtEditor.my_text.insert(ctk.END, commits_pretty)
                self.clearDropdowns(name)
                self.tabview.set("Formatting")
            else:
                self.popup(f"Error fetching response data: {status_code}")
        except Exception as e:
            self.popup(f"An error occurred while fetching commits: {e}")

    def clearDropdowns(self, name):
        try:
            if name in self.dropdowns and 'repo_combo' in self.dropdowns[name]:
                self.dropdowns[name]['repo_combo'].destroy()
                del self.dropdowns[name]['repo_combo'] # tjekker efter repo selection dropdowns hvis de eksisterer så slettes
            if name in self.dropdowns and 'branch_combo' in self.dropdowns[name]:
                self.dropdowns[name]['branch_combo'].destroy()
                del self.dropdowns[name]['branch_combo']
        except Exception as e:
            self.popup(f"An error occurred while clearing dropdowns: {e}")

    def popup(self, text):
        try:
            popupHandler(text)
        except Exception as e:
            print(f"Error displaying popup: {e}")

if __name__ == "__main__":
    app = gitApp()
    app.mainloop()
