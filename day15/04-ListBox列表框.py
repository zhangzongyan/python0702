from tkinter import  *

# 按钮触发的函数
def click():
    # 获取列表框中选中的列表
    index = l1.curselection() # 获取选中的列表索引 从0开始
    for i in index:
        print(l1.get(i)) # 根据索引获取列表成员名字
        l1.delete(i)

root = Tk()

# 列表框
l1 = Listbox(root, height=2, selectmode=EXTENDED)
l1.pack(side=LEFT, expand=1, fill=BOTH)

#
l1.insert(END, "中国")
l1.insert(END, "美国")
l1.insert(1, "意大利")

# 绑定滚动条
scorll = Scrollbar(root, command=l1.yview)
l1['yscrollcommand'] = scorll.set
scorll.pack(side=RIGHT, expand=1, fill=Y)

# 按钮
btn = Button(root, text = "确定", command=click)
btn.pack(side=TOP)

root.mainloop()