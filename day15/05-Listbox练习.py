
from tkinter import *

# 移动
def moveToAnother():
    selections = list1.curselection()
    for i in selections:
        name = list1.get(i)
        list2.insert(END, name)
        list1.delete(i)

# 添加
def addItem():
    s = var.get()
    list1.insert(END, s)
    var.set("")

root = Tk()

list1 = Listbox(root)
list2 = Listbox(root)
bnt1 = Button(root, text="移动->")
bnt2 = Button(root, text="添加", command=addItem)

var = StringVar()
entry = Entry(root, textvariable = var)

for name in ["Python", "C", "C++", "Go"]:
    list1.insert(0, name)
# 默认第一个被选中
list1.activate(1) #????????
list1.pack(side=LEFT)
list2.pack(side=RIGHT)

bnt1['width'] = 10
bnt2['width'] = 10

# 移动按钮添加方法
bnt1['command'] = moveToAnother

bnt1.pack()
bnt2.pack()
entry.pack()


root.mainloop()
