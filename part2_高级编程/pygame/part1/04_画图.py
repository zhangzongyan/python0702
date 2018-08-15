# -*- coding: utf-8 -*-
#   File Name：     03_事件实际应用
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/13

import pygame
from pygame.locals import *
import sys
from random import randint


pygame.init()

window = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

points = []

# 音效(可以多个)
mixer = pygame.mixer.Sound("sound1.wav")
mixer.set_volume(1.0)

# 背景音乐(一个)
pygame.mixer.music.load("bg.wav")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # 按下鼠标
        if event.type == MOUSEBUTTONDOWN:
            mixer.play()

            window.fill((255, 255, 255))

            # 画矩形
            rc = (randint(0, 255), randint(0, 255), randint(0, 255))
            rp = (randint(0, 799), randint(0, 599))
            rs = (randint(1, 800-rp[0]), randint(1, 600-rp[1]))
            pygame.draw.rect(window, rc, (rp, rs))

            # 画圆
            rc = (randint(0, 255), randint(0, 255), randint(0, 255))
            rp = (randint(0, 799), randint(0, 599))
            rs = (randint(1, rp[1] // 2))
            pygame.draw.circle(window, rc, rp, rs)

            # 鼠标按下坐标
            x, y = pygame.mouse.get_pos()
            points.append((x, y))
            # 划线
            pygame.draw.line(window, (0, 0, 255), (0, 0), (x, y))
            pygame.draw.line(window, (0, 0, 255), (800, 600), (x, y))

            if len(points) > 1:
                pygame.draw.lines(window, (255,0,0), False, points)

    pygame.display.update()
    clock.tick(20)

