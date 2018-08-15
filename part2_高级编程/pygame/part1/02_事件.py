# -*- coding: utf-8 -*-
#   File Name：     02_事件
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/13

import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption("检验事件")

# font
font = pygame.font.SysFont("Arial", 18)

eventlist = []
while True:
    window.fill((255, 255, 255))

    '''
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    '''

    # 等待事件的到来
    event = pygame.event.wait()
    text_event = str(event)
    eventlist.append(text_event)
    #print(text_event)

    y = font.get_linesize()

    for text in eventlist:
        fonts = font.render(text, False, (0,0,0))
        window.blit(fonts, (0, 600-y))
        y += font.get_linesize()

    pygame.display.update()

