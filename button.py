from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Done")
    myLabel.pack()


myButton = Button(root, text="Click", command=myClick)
myButton.pack()

root.mainloop()
