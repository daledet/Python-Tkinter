from tkinter import *

root = Tk()
root.title('Frames')
root.iconbitmap('img/ecco.ico')

frame = LabelFrame(root, text="Label The Frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

# Put things in the frame instead of root
button = Button(frame, text="Don't Click This")
button2 = Button(frame, text="Or This")
button.grid(row=0, column=0)
button2.grid(row=1, column=1)


root.mainloop()
