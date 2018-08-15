
from tkinter import *

def click_it():
    print("你要干啥")

root = Tk()

# 主菜单
m = Menu(root)
# m.add_command(label="File")
# m.add_command(label="Edit")
# m.add_command(label="Tools")

# 下拉菜单
filemenu = Menu(m)
filemenu.add_command(label = "新建", command=click_it)
filemenu.add_command(label = "打开")

m.add_cascade(label="File", menu=filemenu)

root['menu'] = m

root.mainloop()

