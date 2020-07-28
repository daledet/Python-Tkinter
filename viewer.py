from tkinter import *
from PIL import ImageTk, Image
# pip install Pillow

root = Tk()
root.title('Images')
root.iconbitmap('img/ecco.png')

# Define Image
my_img1 = ImageTk.PhotoImage(Image.open("img/ecco.ico"))
my_img2 = ImageTk.PhotoImage(Image.open("img/ecco.ico"))
my_img3 = ImageTk.PhotoImage(Image.open("img/ecco.ico"))
my_img4 = ImageTk.PhotoImage(Image.open("img/ecco.ico"))
my_img5 = ImageTk.PhotoImage(Image.open("img/ecco.ico"))

# Image List

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


# Place the image
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<")
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>")

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()
