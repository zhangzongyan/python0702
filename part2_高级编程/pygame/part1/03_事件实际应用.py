# -*- coding: utf-8 -*-
#   File Name：     03_事件实际应用
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/13

import pygame
from pygame.locals import *
import sys


pygame.init()

window = pygame.display.set_mode((800, 600))

font = pygame.font.SysFont("Arial", 20)

#rendtext = font.render("please press a key", True, (255,0,0))

clock = pygame.time.Clock()

teststr = "please press a key"

while True:
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        '''
        if event.type == KEYDOWN:
            # 按键
            if event.key == K_UP:
                rendtext = font.render("upupup", False, (255,0,0))
            elif event.key == K_DOWN:
                rendtext = font.render("downdown", False, (255, 0, 0))
            elif event.key == K_LEFT:
                rendtext = font.render("leftleft", False, (255, 0, 0))
            elif event.key == K_RIGHT:
                rendtext = font.render("rightright", False, (255, 0, 0))
        '''

    # 判断按键
    keys = pygame.key.get_pressed()

    if keys[K_UP]: # 按键的值就是在keys列表中的索引，如果为True则按下，False则没按
        teststr = "upupup"
    if keys[K_DOWN]:
        teststr = "downdown"
    if keys[K_LEFT]:
        teststr = "leftleft"
    if keys[K_RIGHT]:
        teststr = "rightright"
    rendtext = font.render(teststr, False, (255, 0, 0))
    window.blit(rendtext, (400, 300))

    pygame.display.update()
    clock.tick(20)

