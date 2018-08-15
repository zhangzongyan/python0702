
import tkinter as tk
import sqlite3
import random
import tkinter.messagebox

QUESTIONS=[('感冒忌用下列哪种食物', '海鱼', '豆浆', '青菜', '生姜', 'A'), \
           ('柠檬汁有哪些营养含量', '维生素A和C', '维生素B1和C','维生素B1和B2','维生素B和C','A')]

class Question:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("python最强大脑")
        self.root.geometry("500x200")

        # 加载题
        self.save_question()

        # 取出第一题
        self.res = self.load_question()

        self.label = tk.Label(self.root, text=(self.res)[1], font=('Arial', 18),\
                              fg="blue")
        self.label.pack(side="top")

        # 单选框
        f1 = tk.Frame(self.root)
        f1.pack()

        self.var = tk.StringVar()
        self.var.set('E')
        self.buttonA = tk.Radiobutton(f1, text=(self.res)[2], variable=self.var, value="A")
        self.buttonA.pack(side="left")
        self.buttonB = tk.Radiobutton(f1, text=(self.res)[3], variable=self.var, value="B")
        self.buttonB.pack(side="left")
        self.buttonC = tk.Radiobutton(f1, text=(self.res)[4], variable=self.var, value="C")
        self.buttonC.pack(side="left")
        self.buttonD = tk.Radiobutton(f1, text=(self.res)[5], variable=self.var, value="D")
        self.buttonD.pack(side="left")

        f2 = tk.Frame(self.root)
        f2.pack()
        self.nextbutton = tk.Button(f2, text="下一题", command=self.click_next)
        self.nextbutton.pack(side=tk.LEFT)
        tk.Button(f2, text="结果", command=self.show_result).pack(side=tk.RIGHT)

        # 积分
        self.count = 0

    # 下一题
    def click_next(self):
        if self.var.get() == self.res[-1]:
            tkinter.messagebox.showinfo("恭喜", "厉害了！继续挑战")
            self.count += 10
        else:
            tkinter.messagebox.showinfo("失败", "错一个没关系，还有机会")
        if len(self.ls) == 0:
            self.nextbutton["state"] = "disabled"
            self.show_result()
            return None
        #取出下一题
        next = self.load_question()
        self.label["text"] = next[1]
        self.buttonA["text"] = next[2]
        self.buttonB["text"] = next[3]
        self.buttonC["text"] = next[4]
        self.buttonD["text"] = next[5]

    # 构建问答题数据库
    def save_question(self):
        self.conn = sqlite3.connect("question.db")
        self.cur = self.conn.cursor()

        self.cur.execute("DROP TABLE question_table")

        # 建表
        self.cur.execute('''
CREATE TABLE IF NOT EXISTS question_table(no integer PRIMARY KEY AUTOINCREMENT NOT NULL ,
question text NOT NULL , answerA text NOT NULL , answerB text NOT NULL , answerC text NOT NULL ,
answerD text NOT NULL , rightanswer text NOT NULL )
''')
        '''
        # 删除题
        self.cur.execute('DELETE FROM question_table')
        '''

        # 录入问题
        self.cur.executemany('''INSERT INTO question_table(question, answerA, answerB,
answerC, answerD, rightanswer) VALUES (?,?,?,?,?,?)''', QUESTIONS)
        self.cur.close()
        self.conn.commit()
        self.conn.close()

        # 题数
        self.count = self.cur.rowcount
        # 题号的列表
        self.ls = list(range(1, self.count+1))

    def show_result(self):
        # 题库全部完成
        tkinter.messagebox.showinfo("成功", "答题完毕！恭喜你获得%d分" % self.count)

    # 从数据库中加载题
    def load_question(self):
        # 随机从数据中加载一套题
        curnum = random.choice(self.ls)
        self.ls.pop(self.ls.index(curnum)) # 已选题，序号移除

        # 连接
        self.conn = sqlite3.connect("question.db")
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT * FROM question_table WHERE no=?", (curnum,))

        res = self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return res[0]# (1,"题干", "Axx", "Bxx", "Cxx", "Dxx", "right")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    ques = Question()

    # 运行
    ques.run()

