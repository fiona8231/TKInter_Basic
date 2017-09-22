from tkinter import *
from tkinter import ttk

root = Tk()

Label(root, text="Fisrt Name").grid(row=0, sticky=W, padx=4)

Entry(root).grid(row=0, column=2, sticky=W, padx=4)

# button on the third row
Button(root, text="Submit").grid(row=3)

root.mainloop()