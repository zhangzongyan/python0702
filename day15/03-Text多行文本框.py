
from tkinter import *

root = Tk()

# 多行文本框
t = Text(root, height=6)
t.pack(side=LEFT)

t.insert(END, "super(Caculation, self).__init__()\
        self.master.title('计算器')\
        #self.master.resizable(0, 0)\
        self.pack(expand=1, fill=BOTH) # 允许扩展\
        # 显示表达式\
        display = StringVar()\
        #self.display.set()")
# 滚动条
s = Scrollbar(root, command=t.yview)
s.pack(side=RIGHT,expand=1, fill=BOTH)

t['yscrollcommand'] = s.set

root.mainloop()

