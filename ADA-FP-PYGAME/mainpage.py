import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
# from tkinter.filedialog import *
# from tkinter.messagebox import *
# from tkinter.font import Font
# from tkinter.scrolledtext import *
import csv
import subprocess

# """Setting window"""
root = tk.Tk() #creates a blank parent widget

root.title(f"Storage Management System") #set title for the window
root.geometry("500x250") 
root.minsize(500, 250)

sms = ttk.Label(root, text='Storage Management System', background="blue", anchor=CENTER, font=("Helvetica", 25), width=500)
sms.pack(ipadx=0, ipady=0)

def open_merge():
    subprocess.call(["python", "mergepage.py"])

# def open_bubble():
#     subprocess.call(["python", "try-bubble.py"])
    
# def open_selection():
#     subprocess.call(["python", "try-selection.py"])
    
# def open_insertion():
#     subprocess.call(["python", "try-insertion.py"])
    
# def open_bogo():
#     subprocess.call(["python", "try-bogo.py"])
    
mergesort = tk.Button(master=root, text="Merge Sort", bg="yellow", command=open_merge)
mergesort.place(x=30, y=80)

# bubblesort = tk.Button(master=root, text="Bubble Sort", bg="yellow", command=open_bubble)
# bubblesort.place(x=125, y=150)

# selectionsort = tk.Button(master=root, text="Selection Sort", bg="yellow", command=open_selection)
# selectionsort.place(x=200, y=80)

# insertionsort = tk.Button(master=root, text="Insertion Sort", bg="yellow", command=open_insertion)
# insertionsort.place(x=300, y=150)

# bogosort = tk.Button(master=root, text="Bogo Sort", bg="yellow", command=open_bogo)
# bogosort.place(x=400, y=80)

btm = ttk.Label(root, text='', background="blue", font=("Helvetica", 25), width=500)
btm.place(relx=0, rely=1, anchor="s")

root.mainloop()
