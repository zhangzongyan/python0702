
from tkinter import  *

root = Tk()
root.geometry="200x200+0+0"
root.title("计算器1.0")

Button(root, text="7", width=5).grid(row=0, column=0)
Button(root, text="8", width=5).grid(row=0, column=1)
Button(root, text="9", width=5).grid(row=0, column=2)
Button(root, text="4", width=5).grid(row=1, column=0)
Button(root, text="5", width=5).grid(row=1, column=1)
Button(root, text="6", width=5).grid(row=1, column=2)
Button(root, text="1", width=5).grid(row=2, column=0)
Button(root, text="2", width=5).grid(row=2, column=1)
Button(root, text="3", width=5).grid(row=2, column=2)

Button(root, text="/", width=5).grid(row=0, column=3)
Button(root, text="%", width=5).grid(row=0, column=4)
Button(root, text="*", width=5).grid(row=1, column=3)
Button(root, text="x", width=5).grid(row=1, column=4)
Button(root, text="-", width=5).grid(row=2, column=3)
Button(root, text="+", width=5).grid(row=3, column=3)

Button(root, text="0", width=5).grid(row=3, column = 0, columnspan=2, sticky=W+E+S+N)
Button(root, text=".", width=5).grid(row=3, column=2)
Button(root, text="=", width=5).grid(row=2, column=4, rowspan=2, sticky=W+E+S+N)

root.mainloop()
