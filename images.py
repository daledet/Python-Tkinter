from tkinter import *
from PIL import ImageTk, Image
# pip install Pillow

root = Tk()
root.title('Images')
root.iconbitmap('img/ecco.ico')

# Define Image
my_img = ImageTk.PhotoImage(Image.open("img/ecco.ico"))

# Create Thing To Put Image In
my_label = Label(image=my_img)

# Place the image
my_label.pack()

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
