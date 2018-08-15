from tkinter import *

def click():
    v1 = var1.get()
    v2 = var2.get()

    print(v1, v2)


root = Tk()

var1 = StringVar()
var2 = StringVar()
# 复选框
ck1 = Checkbutton(root, text="足球", variable=var1, onvalue="football", \
                  bitmap="error" ,offvalue=100,command=click)
ck1.deselect()
ck1.pack()
ck2 = Checkbutton(root, text="篮球", variable=var2, onvalue="basketball",\
                  bitmap = "questhead",offvalue=200,command=click)
ck2.deselect()
ck2.pack()

root.mainloop()

