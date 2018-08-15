
import tkinter as tk

# 按钮触发的方法
def click_button():
    print("已点击")

def click_button2():
    print("再次点击")

root = tk.Tk()
root.geometry("400x600")
root.title("这是一个测试窗口")
#root.minsize(width=400, height=300)
#root.maxsize(width=400, height=300)
#root.resizable(width=0,height=0) # width 0不可伸缩， 1可伸缩
'''
# 按钮类Button
button = tk.Button(root, text="确定", fg="red", bg = "black", command=click_button)
button["fg"] = "blue"
button["text"] = "退出"
button.config(fg="yellow")
button.pack(side="top", expand=0) # pack布局
button.invoke() # 触发按钮
button.config(command = click_button2)

button2 = tk.Button(root, text="退出")
button2.pack(side="left", expand=0)
'''

# 网格布局
b1 = tk.Button(root, text="1")
b2 = tk.Button(root, text="2")
b3 = tk.Button(root, text="3")
b4 = tk.Button(root, text="4")
b5 = tk.Button(root, text="5")
b1.grid(row = 1, column=1)
b2.grid(row = 1, column=0)
b3.grid(row = 1, column=2)
b4.grid(row = 2, column=0, columnspan=2)
b5.grid(row = 2, column=2)

'''
#place
b1 = tk.Button(root, text="1")
b2 = tk.Button(root, text="2")
b1.place(x=0, y= 0)
b2.place(x=100, y=100)
'''
root.mainloop() # 不结束

