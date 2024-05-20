import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext 
from tkinter import messagebox
import pandas as pd

ships_df = pd.read_csv("stem_center_internships.csv")

def find_major():
    major = entry.get().lower()
    result = ""
    if "computer" in major.lower():
        result = ships_df[ships_df['Discipline'].str.contains('Computer|Coding|Multiple', case=False, na=False)]

    elif "engineering" in major.lower():
        result = ships_df[ships_df['Discipline'].str.contains('Engineering|Multiple', case=False, na=False)]
    
    names = result['Internship Opportunity']
    links = result['Application Link']
    names_links = dict(zip(names,links))    

    if result is not None:
        display_result(names_links)
    else: 
        messagebox.showinfo("Here's your internships", "? Change majors")

def display_result(result_dict):
    result_window = tk.Toplevel(root)

    text_widget = scrolledtext.ScrolledText(result_window, wrap=tk.WORD)
    text_widget.pack(expand=True, fill="both")

    for key, value in result_dict.items():
        text_widget.insert(tk.END,'\n')
        text_widget.insert(tk.END, f"{key}: {value}\n")

# Create GUI
root = tk.Tk()  
root.title("Internship Finder")

label = tk.Label(root, text="Enter major:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Find", command=find_major)
button.pack()

root.mainloop()
