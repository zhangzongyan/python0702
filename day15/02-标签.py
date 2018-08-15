
from tkinter import *
from PIL import Image,ImageTk

root = Tk()

l1 = Label(root, text="这是一个标签")
l1.pack()

#
img = Image.open("img1.jpg")
img = img.resize((50, 50))
img = ImageTk.PhotoImage(img)
l2 = Label(root, image=img)
l2.pack()

root.mainloop()
