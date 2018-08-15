from tkinter import *

def hello(event):
    print(event.char)
    print("hello, x:%d, y:%d" % (event.x, event.y))
def hello_all(event):
    print("→→", event)

root = Tk()
root.geometry("200x200")

# 绑定事件
root.bind('<Button-1>', hello)
root.bind('<Return>', hello)
root.bind('<Key>', hello)

f1 = Frame(root, height=100, width=100, bg="red")
f1.bind_all('<Button-3>', hello_all)
f1.pack(side=TOP, expand=1, fill=BOTH)
l1 = Label(f1, text="这是一个标签")
l1.pack()

Button(root, text="确定").pack()

root.mainloop()
