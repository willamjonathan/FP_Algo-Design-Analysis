from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Treeview, Scrollbar
import numpy as np
def randoms(x):
    np.random.shuffle(x)
    
    root = tk.Tk()
    root.geometry("150x450")

    window = tk.Canvas(bg = "#FFFFFF",
            height = 450,
            width = 150,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
    window.place(x = 0, y = 0)
    columns = {
        "Items": ["Items", 75]
    }
    
    treeview = Treeview(columns=list(columns.keys()),
                    show="headings",
                    height=200,
                    selectmode="browse", )
                    
    for idx, txt in columns.items():
        treeview.heading(idx, text=txt[0])
        treeview.column(idx, width=txt[1])
    treeview.pack(side='left')

    treeview.tag_configure("oddrow", background="white")
    treeview.tag_configure("evenrow", background="lightblue")
    vsb = Scrollbar(root, orient="vertical", command=treeview.yview)
    vsb.pack(side='right', fill='y')

    treeview.configure(yscrollcommand=vsb.set)

    treeview.place(x=0.0, y=0.0, width=150.0, height=450.0)
    count = 0
    for row in x:
        if count % 2 == 0:
            treeview.insert("", "end", values=row, tags=("evenrow",))
        else:
            treeview.insert("", "end", values=row, tags=("oddrow",))
        count += 1


    root.resizable(False, False)
    root.mainloop()
    


