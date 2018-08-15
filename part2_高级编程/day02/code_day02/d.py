from tkinter import *
from PIL import Image ,ImageTk
import random
import time

class Puke:
    def __init__(self):
        self.root = Tk()
        self.root.title('扑克游戏')
        self.root.geometry('700x600')
        #创建一个宽为400，高为400，背景为蓝色色的画布
        self.canvas = Canvas(self.root,width=700,height=600,bg="pink")
        self.canvas.pack(expand=1,fill=BOTH)
        self.dianji()
        self.root.mainloop()

    def dianji(self):
        button = Button(self.canvas,height=1, width=10, text='开始游戏', bg='red',command=self.send_image)
        button.place(x=300,y=300)
    #添加图片
    def send_image(self):
        img = [0]*13
        img1 = [0]*13
        img2 = [0]*13
        img3 = [0]*13
        #交换次序洗牌
        shuzi = [i for i in range(1,53)]
        for i in range(50):
            index1 = random.randint(0, 51)
            index2 = random.randint(0, 51)
            shuzi[index1], shuzi[index2] = shuzi[index2], shuzi[index1]
        for i in range(13):
            m=(i)*4
            img[i] = Image.open("pukeImage\\"+\
                                str(shuzi[m]) +".jpg")
            img1[i] = Image.open("pukeImage\\" + \
                                str(shuzi[m+1]) + ".jpg")
            img2[i] = Image.open("pukeImage\\" + \
                                 str(shuzi[m+2]) + ".jpg")
            img3[i] = Image.open("pukeImage\\" + \
                                 str(shuzi[m+3]) + ".jpg")
            img[i] = img[i].resize((60, 80))
            img[i] = ImageTk.PhotoImage(img[i])
            img1[i] = img1[i].resize((60, 80))
            img1[i] = ImageTk.PhotoImage(img1[i])
            img2[i] = img2[i].resize((60, 80))
            img2[i] = ImageTk.PhotoImage(img2[i])
            img3[i] = img3[i].resize((60, 80))
            img3[i] = ImageTk.PhotoImage(img3[i])
            r1 = self.canvas.create_image(200+5*m,50,anchor=NW,image=img[i])
            r2 = self.canvas.create_image(100,150+5*m, anchor=NW, image=img1[i])
            r3 = self.canvas.create_image(550,150+5*m, anchor=NW, image=img2[i])
            r4 = self.canvas.create_image(200+5*m,500, anchor=NW, image=img3[i])
            self.canvas.update()
            time.sleep(0.5)

puke = Puke()