from tkinter import *

''' Frame类 + pack布局'''
root = Tk()
root.geometry("400x400+0+0") # width x height + x + y

# 创建Label标签对象
Label(root, text="校训", font=('Arial', 16)).pack()

# Frame是一个框架,就是用于存放其他组件的
fr = Frame(root)

fr_left = Frame(fr)
Label(fr_left, text="困知").pack()
Label(fr_left, text="积厚").pack()
fr_left.pack(side=LEFT)

fr_right = Frame(fr)
Label(fr_right, text="勉行").pack()
Label(fr_right, text="成器").pack()
fr_right.pack(side=RIGHT)

fr.pack()

root.mainloop()

