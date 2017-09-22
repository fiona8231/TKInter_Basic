from tkinter import *
from tkinter import ttk

# Frame inside frame
root = Tk()

frame = Frame(root)
# x = StringVar() # Holds a string; default value ""
lableText = StringVar()
lableText.set("I am a Label")

label = Label(frame, textvariable=lableText)
button = Button(frame, text="Click Me")

label.pack()
button.pack()
frame.pack()

root.mainloop()