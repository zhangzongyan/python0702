# -*- coding: utf-8 -*-
#   File Name：     plane_sprites
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/15
######################################

import pygame, random

SCREEN = pygame.Rect(0, 0, 480, 700)
HEROBOTTOM = 20


# 飞机大战游戏精灵类
class PlaneSprite(pygame.sprite.Sprite):
    def __init__(self, imgpath, speed = 1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imgpath)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)

    # 重写父类的update方法
    def update(self):
        self.rect.y += self.speed

# 我方飞机类
class HeroSprite(PlaneSprite):
    def __init__(self):
        super().__init__("../images/me1.png")
        self.rect.centerx = SCREEN.centerx
        self.rect.bottom = SCREEN.height - HEROBOTTOM
        # 子弹组
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right >= SCREEN.right:
            self.rect.right = SCREEN.right

    # 发射子弹
    def fire(self):
        for i in range(3):
            b = BulletSprite()
            # 子弹位置
            b.rect.midbottom = self.rect.midtop
            self.bullet_group.add(b)


# 子弹类
class BulletSprite(PlaneSprite):
    def __init__(self, speed = -3):
        PlaneSprite.__init__(self, "../images/bullet1.png")
        self.speed = speed

    def update(self):
        PlaneSprite.update(self)
        if self.rect.y < 0:
            self.kill() # 销毁

    # 销毁自动调用的方法
    def __del__(self):
        print("子弹销毁了")


# 敌机类
class EnemySprite(PlaneSprite):
    def __init__(self):
        PlaneSprite.__init__(self, "../images/enemy1.png")
        self.rect.x = random.randint(0, SCREEN.width-self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 3)

    def update(self):
        PlaneSprite.update(self)
        if self.rect.y > SCREEN.height:
            self.kill()

    def __del__(self):
        print("敌机销毁了....")


# 背景类
class BgSprite(PlaneSprite):
    def __init__(self, flag = False):
        PlaneSprite.__init__(self, "../images/background.png")
        print(self.rect)
        if flag:
            self.rect.y = -SCREEN.height

    def update(self):
        PlaneSprite.update(self)
        if self.rect.y >= SCREEN.height:
            self.rect.y = -SCREEN.height

