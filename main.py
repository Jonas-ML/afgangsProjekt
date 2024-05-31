
import time
from apiClient import *
from customtkinter import *
import customtkinter as ctk
from JSON_Formatter import *
from PDFconverter import TextToPDF




class gitApp(ctk.CTk):
    def __init__(self):
        super().__init__() # makes sure that CTK is intialised before other inits
        self.a = restClient()
        self.geometry("1200x800")
        self.title("Commit extractor")
        self.createWidgets()
        self.dropdowns = {}
        self.dataFormatter = dataFormatter()
        self.choosen_repo = None
        self.choosen_branch = None
    
        
        
    def createWidgets(self): # Handles the creation of widgets
        self.createTabs()
        self.createEntryBoxes()
        self.createButtons()
        self.createTxtWidget()


    def createTabs(self):
        self.tabview = ctk.CTkTabview(master=self, width=1200, height=800)
        self.tabview.pack()
        self.user_tab = self.tabview.add("Selection")
        self.search_tab = self.tabview.add("Formatting")
        self.tabview._segmented_button.grid(sticky="NSEW") # Placement of tabs
    
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
        corner_radius=1)

        self.my_text.pack(pady=10)

        self.txt_frame = ctk.CTkFrame(self.search_tab)
        self.txt_frame.pack(pady=10)
        
        self.delete_button = ctk.CTkButton(self.txt_frame, text="Delete", command=self.delete)
        self.delete_button.grid(padx=2, row=2, column=4)
        
        
        self.import_button = ctk.CTkButton(self.txt_frame, text="Import Commits", command=self.importTXT)
        self.import_button.grid(padx=2, row=2, column=0)
        
        self.format_button = ctk.CTkButton(self.txt_frame, text="Format", command=self.formatTXT) #####
        self.format_button.grid(padx=2, row=2, column=2)
        
        self.save_option = ctk.CTkComboBox(self.txt_frame, values=["Save as","TXT", "PDF"], command=self.save)
        self.save_option.grid(padx=2, row=2, column=6)

    def repoChoice(self):
        name = self.user_entry.get()
        try:
            response, status_code = self.a.get(f"users/{name}/repos")
            if status_code == 200:
                repoRes = dataFormatter().formatResponse(response)
                repo_options = dataFormatter().fetchRepos(repoRes)
                if repo_options:
                    if name not in self.dropdowns: # Makes sure that dropdown element sare only created once pr username
                        self.dropdowns[name] = {}
                    if 'repo_combo' not in self.dropdowns[name]:
                        repo_combo = ctk.CTkComboBox(self.user_tab, values=repo_options, command=lambda event=None: self.branchChoice(name, repo_combo.get()),
                            width=180)
                        
                        repo_combo.pack(pady=1)
                        self.dropdowns[name]['repo_combo'] = repo_combo # Creates repo_combo key in dictionary
                else:
                    self.popup(f"No repos found for this user.\n Did you supply the correct username?")
            else:
                self.popup(f"Error fetching data:\n {status_code}")
    
        except Exception as e:
            self.popup(f"An error occurred while fetching repositories:\n {e}")
            
            

    def branchChoice(self, name, choosen_repo):
        try:
            response, status_code = self.a.get(f"repos/{name}/{choosen_repo}/branches")
            if status_code == 200:
                branchRes = dataFormatter().formatResponse(response)
                branch_options = dataFormatter().fetchRepos(branchRes)
                if branch_options:
                    if 'branch_combo' not in self.dropdowns[name]:
                        self.branch_combo = ctk.CTkComboBox(self.user_tab, values=branch_options, command=lambda event=None: self.getCommits(name, choosen_repo, self.branch_combo.get()),
                            width=180)
                        
                        self.branch_combo.pack(pady=5)
                        self.dropdowns[name]['branch_combo'] = self.branch_combo
                else:
                    self.popup(f"Couldnt fetch branches for:\n {choosen_repo}")
            else:
                self.popup(f"Error fetching response data {status_code}")
        except Exception as e:
            self.popup(f"An error occurred while fetching branches for: \n {choosen_repo}, \n Error: {e}")
            
            
    
    def getCommits(self, name, choosen_repo, choosen_Branch):
        try:
            self.choosen_repo = choosen_repo
            self.choosen_branch = choosen_Branch
            response, status_code = self.a.get(f"repos/{name}/{choosen_repo}/commits", params={"sha" : choosen_Branch})
            if status_code == 200:
                commits_raw = dataFormatter().formatResponse(response)
                commits_pretty = dataFormatter().formatCommits(commits_raw, choosen_repo, choosen_Branch)
                self.my_text.insert(END, commits_pretty)
                self.clearDropdowns(name)
                self.tabview.set("Formatting")
                self.commits_pretty = commits_pretty
            else:
                self.popup(f"Error fetching response data:\n {status_code}")
        except Exception as e:
            self.popup(f"An error occurred while fetching commmits:\n {e}")
    
    def popup(self, text):
        try:
            self.popupWindow = ctk.CTkToplevel()
            self.popupWindow.title("Message")
            self.popupWindow.geometry("300x150")
            self.popupWindow.resizable(False, False)
            self.message = ctk.CTkLabel(self.popupWindow, width=10, height=10, text=f"{text}")
            self.message.pack(pady=1)
            
            self.popupButton = ctk.CTkButton(self.popupWindow, text="Close", command=self.closePopup)
            self.popupButton.pack(pady=30)
        except Exception as e:
            print(f"Error making popup window: {e} ")


    def closePopup(self):
        self.popupWindow.destroy()
        self.popupWindow.update()

    def delete(self):
        try:
            self.my_text.delete(0.0, "end")
        except Exception as e:
            self.popup(f"An error occurred while deleting text:\n {e}")

     
    def save(self, choice):
        try:
            choice = self.save_option.get()
            text = self.my_text.get(0.0, END)
            
            if choice == "PDF":
                self.save_as_pdf(text)
            elif choice == "TXT":
                self.save_as_txt(text)
            else:
                self.popup("Invalid choice")
        except Exception as e:
            self.popup(f"An error occurred while saving:\n {e}")

    def save_as_pdf(self, text):
        try:
            pdfDialog = ctk.CTkInputDialog(text="Enter title of document", title="PDF creation")
            docName = pdfDialog.get_input()
            pdf = TextToPDF(ttle=docName)
            pdf.createPDF(text, f"{docName}.pdf")
            self.popup(f"PDF created successfully,\n in project root")
        except Exception as e:
            self.popup(f"Error creating PDF:\n {e}")

    def save_as_txt(self, text):
        try:
            dialog = ctk.CTkInputDialog(text="Enter title of file", title="Save file")
            fileName = dialog.get_input()
            with open(f"{fileName}.txt", "w") as txtFile:
                txtFile.write(text)
        except IOError as e:
            self.popup(f"An error occurred while saving the file:\n {e}")
        except Exception as e:
            self.popup(f"Error getting filename or text content:\n {e}")
     
    def importTXT(self):
        try:
            self.my_text.insert(END, self.commits_pretty)
        except Exception as e:
            self.popup(f"No commit data currently stored:\n {e}")
            
        
    def formatTXT(self):
        try:
            dialog = ctk.CTkInputDialog(text="Enter keywords separated by commas", title="Keyword Input")
            keywords = dialog.get_input().split(',')
            txt = self.my_text.get(0.0, END)
            formatted_commits = dataFormatter().textFormatting(txt, keywords)
            self.my_text.delete(0.0, END)
            self.my_text.insert(END, formatted_commits)
        except Exception as e:
            self.popup(f"An error occurred while formatting commits:\n {e}")       
              
    def clearDropdowns(self, name):
        try:
            if name in self.dropdowns and 'repo_combo' in self.dropdowns[name]:
                self.dropdowns[name]['repo_combo'].destroy()
                del self.dropdowns[name]['repo_combo']
            if name in self.dropdowns and 'branch_combo' in self.dropdowns[name]:
                self.dropdowns[name]['branch_combo'].destroy()
                del self.dropdowns[name]['branch_combo']
        except Exception as e:
            self.popup(f"An error occurred while clearing dropdowns:\n {e}")
    


app = gitApp()
app.mainloop()






