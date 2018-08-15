
from tkinter import  *

root = Tk()
root.geometry("200x200+0+0")

# 画布对象
cvs = Canvas(root, width=100, height=100, bg="green")
cvs.pack()
cvs.create_line((0,0), (50, 50), (100,0))
cvs.create_bitmap(80, 80, bitmap="error")

root.mainloop()
