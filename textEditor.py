# Text editor - modulariseret da den begyndte at tage store mængder plads fra main
from customtkinter import *
import customtkinter as ctk
from dataHandling.JSON_Formatter import *
from dataHandling.PDFconverter import TextToPDF
from popupHandler import *


class TxtWidget:
    def __init__(self, parent_frame, popup_handler):
        self.my_text = ctk.CTkTextbox(parent_frame, width=800, height=600, corner_radius=1)
        self.my_text.pack(pady=10)
        
        self.txt_frame = ctk.CTkFrame(parent_frame)
        self.txt_frame.pack(pady=10)

        self.delete_button = ctk.CTkButton(self.txt_frame, text="Delete", command=self.delete)
        self.delete_button.grid(padx=2, row=2, column=4)

        self.import_button = ctk.CTkButton(self.txt_frame, text="Import Commits", command=self.importTXT)
        self.import_button.grid(padx=2, row=2, column=0)

        self.format_button = ctk.CTkButton(self.txt_frame, text="Format", command=self.formatTXT)
        self.format_button.grid(padx=2, row=2, column=2)

        self.save_option = ctk.CTkComboBox(self.txt_frame, values=["Save as", "TXT", "PDF"], command=self.save)
        self.save_option.grid(padx=2, row=2, column=6)

        self.popup = popup_handler

        self.commits_pretty = None # bliver assignet fra main

    def delete(self):
        try:
            self.my_text.delete(0.0, "end")
        except Exception as e:
            self.popup(f"An error occurred while deleting text:\n {e}")

    def importTXT(self):
        try:
            if self.commits_pretty:
                self.my_text.insert(ctk.END, self.commits_pretty)
            else:
                self.popup("No commit data currently stored.")
        except Exception as e:
            self.popup(f"Error importing commit data:\n {e}")

    def formatTXT(self):
        try:
            dialog = ctk.CTkInputDialog(text="Enter keywords separated by commas", title="Keyword Input")
            keywords = dialog.get_input().split(',')
            txt = self.my_text.get(0.0, ctk.END)
            formatted_commits = dataFormatter().textFormatting(txt, keywords)
            self.my_text.delete(0.0, ctk.END)
            self.my_text.insert(ctk.END, formatted_commits)
        except Exception as e:
            self.popup(f"An error occurred while formatting commits:\n {e}")

    def save(self, choice):
        try:
            choice = self.save_option.get()
            text = self.my_text.get(0.0, ctk.END)
            
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
            pdf = TextToPDF(title=docName)
            pdf.createPDF(text, f"{docName}.pdf")
            self.popup(f"PDF created successfully in project root.")
        except Exception as e:
            self.popup(f"Error creating PDF:\n {e}")

    def save_as_txt(self, text):
        try:
            dialog = ctk.CTkInputDialog(text="Enter title of file", title="Save file")
            fileName = dialog.get_input()
            if fileName:
                with open(f"{fileName}.txt", "w") as txtFile:
                    txtFile.write(text)
                self.popup(f"File '{fileName}.txt' saved successfully.")
        except Exception as e:
            self.popup(f"Error saving file:\n {e}")
