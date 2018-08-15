
from tkinter import *

# 创建框架
def create_frame(parent, side):
    f = Frame(parent)
    f.pack(side=side,expand=1, fill=BOTH)
    return f

class Caculation(Frame):
    def __init__(self):
        super(Caculation, self).__init__()
        self.master.title("计算器")
        #self.master.resizable(0, 0)
        self.pack(expand=1, fill=BOTH) # 允许扩展
        # 显示表达式
        display = StringVar()
        #self.display.set("0")
        Entry(self, textvariable=display, state = DISABLED).pack(side=TOP, expand=1, fill=BOTH)

        # 按钮
        buttons = ("789+", "456*", "123/", "-0.=")
        for f in buttons:
            fm = create_frame(self, TOP)
            for b in f: # 按钮
                if b != "=":
                    newbutton = Button(fm, text=b,  command=lambda ch=b,w=display: w.set(w.get()+ch))
                    newbutton.pack(side = LEFT, expand=1, fill = BOTH)
                else:
                    newbutton = Button(fm, text=b, command=lambda w=display:w.set(self.cal(w.get())))
                    newbutton.pack(side=LEFT, expand=1, fill=BOTH)
            #for x in "+*/":
    # 计算
    def cal(self, exp):
        try:
            return eval(exp)
        except:
            return "error"
# fm = Frame() # fm.master --->Tk()
# fm.master.geometry("400x400+0+0")
# fm.master.title("计算器")
# # 输入框
# c = StringVar()
# entry = Entry(fm, width=50, justify = CENTER, \
#               relief=GROOVE, state=DISABLED, textvariable=c, font=("Arial", 14)) # show="*"
# c.set("1+100")
#
# entry.pack()
#
# fm.pack()
# fm.mainloop()

if __name__ == '__main__':
    Caculation().mainloop()

