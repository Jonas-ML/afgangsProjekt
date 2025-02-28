# Lavet for at generalisere error messages, så man bare kan lave dem som en print statement i en popup
import customtkinter as ctk

def popupHandler(message):
    popup_window = ctk.CTkToplevel()
    popup_window.title("Message")
    popup_window.geometry("300x150")
    popup_window.resizable(False, False)
    message_label = ctk.CTkLabel(popup_window, text=message)
    message_label.pack(pady=1)
    close_button = ctk.CTkButton(popup_window, text="Close", command=popup_window.destroy)
    close_button.pack(pady=30)
