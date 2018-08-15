from tkinter import *

def click():
    #print("hello")
    if var.get() == 1:
        print("中国是个好地方")
    elif var.get() == 2:
        print("你要去美国玩吗")
    elif var.get() == 3:
        print("日本也挺漂亮的")

root = Tk()


# 单选按钮
var = IntVar()

radio1 = Radiobutton(root, text="中国", variable=var, value=1, command=click)
radio1.pack()
radio2 = Radiobutton(root, text="美国", variable=var, value=2, command=click)
radio2.pack()
radio3 = Radiobutton(root, text="日本", variable=var, value=3, command=click,\
                     state=DISABLED)
radio3.pack()

root.mainloop()
