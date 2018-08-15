# -*- coding: utf-8 -*-
#   File Name：     01_精灵
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/14

import pygame, sys
from pygame.locals import *
from random import randint

DIR_LEFT = 0
DIR_RIGHT = 1
DIR_TOP = 2
DIR_DOWN = 3

# 圆类
class Circle(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        self.image = pygame.image.load("./img2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, direct):
        if direct == DIR_RIGHT:
            if self.rect.left >= 400-self.rect.width:
                return
            self.rect.left += self.speed
        elif direct == DIR_LEFT:
            if self.rect.left <= 0:
                return
            self.rect.left -= self.speed
        elif direct == DIR_TOP:
            if self.rect.top <= 0:
                return
            self.rect.top -= self.speed
        elif direct == DIR_DOWN:
            if self.rect.top >= 300-self.rect.height:
                return
            self.rect.top += self.speed



# 方块
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed = 1, direction=None):
        super().__init__()
        #self.image = pygame.Surface((width, height))
        #self.image.fill(color)
        self.image = pygame.image.load("./Circle.png")
        self.rect = self.image.get_rect()
        self.speed = speed
        self.direct = direction
        self.mask = pygame.mask.from_surface(self.image)

    #自由移动
    def move(self, redir = None):
        if redir:
            self.direct = redir
        if self.direct == DIR_RIGHT:
            self.rect.left += self.speed
            if self.rect.left >= 400-self.rect.width:
                self.direct = DIR_DOWN
        elif self.direct == DIR_DOWN:
            self.rect.top += self.speed
            if self.rect.top >= 300-self.rect.height:
                self.direct = DIR_LEFT
        elif self.direct == DIR_LEFT:
            self.rect.left -= self.speed
            if self.rect.left <= 0:
                self.direct = DIR_TOP
        else:
            self.rect.top -= self.speed
            if self.rect.top <= 0:
                self.direct = DIR_RIGHT

if __name__ == '__main__':
    pygame.init()

    window = pygame.display.set_mode((400, 300))

    # 精灵组
    group = pygame.sprite.Group()
    # 创建方块对象
    block = []
    for i in range(3):
        block.append(Block((randint(0, 255), randint(0, 255), randint(0, 255)),\
                           50+i*10, 50+i*10, 5, randint(0, 3)))
        block[i].rect.topleft = (i * 60, i * 60)
        group.add(block[i])
    # 创建圆对象
    circle = Circle((300, 200), 10)
    circle_dir = None
    # FPS
    clock = pygame.time.Clock()

    while True:
        window.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # 圆与方块是否碰撞
        collide_list = pygame.sprite.spritecollide(circle, group, False, \
                                                   pygame.sprite.collide_mask)
        for i in collide_list:
            group.remove(i)

        # 圆方向
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            circle_dir = DIR_TOP
        if keys[K_DOWN]:
            circle_dir = DIR_DOWN
        if keys[K_LEFT]:
            circle_dir = DIR_LEFT
        if keys[K_RIGHT]:
            circle_dir = DIR_RIGHT
        circle.move(circle_dir)
        window.blit(circle.image, circle.rect)

        for b in group:
            window.blit(b.image, b.rect)
            b.move()

        pygame.display.update()
        clock.tick(10)

