import tkinter as tk
import tkinter.messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_entry = tk.Entry(self)
        self.input_entry.pack()

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "确定"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side = tk.LEFT)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="right")

    def say_hi(self):
        #print("hi there, everyone!")
        # 创建一个对话框
        tk.messagebox.showinfo(title="注意了", message=self.input_entry.get() or "就没什么想说的吗")


root = tk.Tk()
root.geometry("800x600")
app = Application(master=root)
app.mainloop()

# root = tk.Tk()
#
# button1 = tk.Button(root, text = "测试", fg = "blue")
# button1.pack(side = "left")
# root.mainloop()
