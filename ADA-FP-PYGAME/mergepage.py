import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
import random
import itertools
from randoms import randoms
from calls import mergesort
from calls import searchStorage
# from tkinter.filedialog import *
# from tkinter.messagebox import *
# from tkinter.font import Font
# from tkinter.scrolledtext import *
import csv
import subprocess


# """Setting window"""
root = tk.Tk() #creates a blank parent widget

root.title(f"Storage Management System") #set title for the window
root.geometry("500x500") 
root.minsize(500, 500)

sms = ttk.Label(root, text='Merge Sort', background="blue", anchor=CENTER, font=("Helvetica", 25), width=500)
sms.pack(ipadx=0, ipady=0)


# def sort_merge():
#     subprocess.call(["python", "/adafp/calls/mergesort.py"])
    
# def randoms():
#     subprocess.call(["python", "/adafp/calls/randoms.py"])
    
# def search_storage():
#     subprocess.call(["python", "/adafp/calls/searchStorage.py"])

sortmerge = tk.Button(master=root, text="Sort", bg="yellow", command=mergesort)
sortmerge.place(x=30, y=80)

randommerge = tk.Button(master=root, text="Random", bg="yellow", command=randoms)
randommerge.place(x=80, y=80)

storage = ttk.Label(root, text='STORAGE', font=("Helvetica", 10), width=400)
storage.place(x=300, y=83)

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "You searched for: "+ inp + "\n Please click Search to continue...")

inputtxt = tk.Text(root,
                   height = 3,
                   width = 20)
inputtxt.place(x=300, y=125)

  
# Label Creation
lbl = tk.Label(root, text = "")
lbl.place(x=295, y=250)

inpt = tk.Button(master=root, text="Input", bg="yellow", command=printInput)
inpt.place(x=300, y=200)

search = tk.Button(master=root, text="Search", bg="yellow", command=searchStorage)
search.place(x=416, y=200)
  

def searchStorage(x, items, inp):
    for i in range(len(x)):
        if(x[i]==items==inp):
            if(i<=43):
                A = ('A',[x[i]])
                print("In Storage A")
                break
            elif(43<i<=86):
                B = ('B',[x[i]])
                print("In Storage B")
                break
            elif(86<i<=130):
                C = ('C',[x[i]])
                print("In Storage C")
                break
            else:
                print("The items you are looking for does not exist in our csv file")
                break
    


TableMargin = Frame(height = 100, width=80)
# TableMargin.pack(side=LEFT)
TableMargin.place(x=28, y=125)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("LIST"), height=100, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('LIST', text="LIST", anchor=N)
# tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#0', stretch=NO, minwidth=0, width=0)

tree.pack()

with open('/ADAexcelFP.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        list = row['LIST']

        tree.insert("", 'end', values=(list))
        

btm = ttk.Label(root, text='', background="blue", anchor=CENTER, width=500, font=("Helvetica", 25))
btm.place(relx=0, rely=1, anchor="s")




root.mainloop()