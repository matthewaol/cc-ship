import tkinter as tk
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
    
    if result is not None:
        messagebox.showinfo("Here's your internships", result.to_string(index=False))
    else: 
        messagebox.showinfo("Here's your internships", "? Change majors")


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
