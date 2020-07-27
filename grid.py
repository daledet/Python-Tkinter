from tkinter import *

root = Tk()

# Create item

myLabel1 = Label(root, text="Hello")
myLabel2 = Label(root, text="There")

# Build the window

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# Make it loop
root.mainloop()
