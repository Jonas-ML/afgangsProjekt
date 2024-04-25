import requests
from apiClient import *
import json
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Dashboard")
root.configure(background="white")
root.minsize(200, 200)
root.maxsize(1920, 1080)
root.geometry("1200x400+50+50")
tabsystem = ttk.Notebook(root)


tab1 = Frame(tabsystem)
tabsystem.add(tab1, text="!H")
tabsystem.pack(expand=1, fill="both")




root.mainloop()