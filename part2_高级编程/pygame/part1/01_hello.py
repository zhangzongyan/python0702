# -*- coding: utf-8 -*-
#   File Name：     01_hello
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/13

import pygame,sys
# 常量
from pygame.locals import *

# 初始化
pygame.init()

# 构建Surface对象
screen = pygame.display.set_mode((400,300))
# 设置主题
pygame.display.set_caption("第一个游戏")

# 加载图片
image = pygame.image.load("./test1.jpeg")
imageRect = image.get_rect() # (left, top, width, height)

print(imageRect.top, imageRect.left, imageRect.bottom, imageRect.right,\
      imageRect.center)

x, y = 0, 0
dirction = "right"

# 指定背景颜色
COLOR = (255,255,255)

# 显示文字
myfont = pygame.font.SysFont("Fira Code", 40, bold=True, italic=True)
# 生成surface
font_surf = myfont.render("Pygame", False, (255,0,0))

# 速率
FPS = 40
clock = pygame.time.Clock()

while True:
    # 游戏在点击关闭按钮时终止
    for event in pygame.event.get():
        if event.type == QUIT:
            print("bye-bye")
            pygame.quit()
            sys.exit(0)
    # 添加背景颜色
    screen.fill(COLOR)

    if dirction == "right":
        x += 10
        if x == 300:
            dirction = "down"
    elif dirction == "down":
        y += 10
        if y == 200:
            dirction = "left"
    elif dirction == "left":
        x -= 10
        if x == 0:
            dirction = "up"
    else:
        y -= 10
        if y == 0:
            dirction = "right"


    # 将图片加载到游戏界面
    screen.blit(image, (x, y))
    # 显示文字
    screen.blit(font_surf, (150, 150))

    pygame.display.update() #更新游戏界面
    clock.tick(FPS)
