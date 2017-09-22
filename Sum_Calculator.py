from tkinter import *
from tkinter import ttk

def get_sum(event):
    num1 = int(num1Entery.get())
    num2 = int(num2Entry.get())

    sum = num1 + num2

    # Insert sumEntry
    sumEntry.delete(0, "end")

    sumEntry.insert(0, sum)


root = Tk()

num1Entery = Entry(root)
num1Entery.pack(side=LEFT)

Label(root, text="+").pack(side = LEFT)

num2Entry = Entry(root)
num2Entry.pack(side= LEFT)

equalButton = Button(root, text="=")

# Bind the handler to the button
# <Button-1> is the left button on the mouse

equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()