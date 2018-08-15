# -*- coding: utf-8 -*-
#   File Name：     mygame
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/15

from plane_sprites import  *
from pygame.locals import *
from sys import exit

BULLET_EVENT = pygame.USEREVENT
ENEMY_EVENT = pygame.USEREVENT+1

# 构建游戏类
class GamePlane():
    def __init__(self):
        self.window = pygame.display.set_mode(SCREEN.size)
        pygame.display.set_caption("飞机大战1.0")
        self.__init_role()
        # 定义产生子弹和敌机的时钟
        pygame.time.set_timer(BULLET_EVENT, 500)
        pygame.time.set_timer(ENEMY_EVENT, 1000)

    # 开始游戏
    def game_start(self):
        # 帧率
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == BULLET_EVENT:
                    b = BulletSprite()
                    b.rect.midbottom = self.hero.rect.midtop
                    self.hero.bullet_group.add(b)
                if event.type == ENEMY_EVENT:
                    e = EnemySprite()
                    self.enemy_group.add(e)

            keypresslist =  pygame.key.get_pressed()
            if keypresslist[K_LEFT]:
                self.hero.speed = -5
            elif keypresslist[K_RIGHT]:
                self.hero.speed = 5
            else:
                self.hero.speed = 0
            self.__spritecollide()
            self.__show()
            pygame.display.update()
            clock.tick(60)

    # 构建人物 角色
    def __init_role(self):
        # 背景组和精灵
        bg1 = BgSprite()
        bg2 = BgSprite(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        # 英雄
        self.hero = HeroSprite()
        self.hero_group = pygame.sprite.Group(self.hero)
        # 子弹组--》已构建
        # 敌机组
        self.enemy_group = pygame.sprite.Group()

    # 显示角色
    def __show(self):
        self.bg_group.update()
        self.bg_group.draw(self.window)
        self.hero_group.update()
        self.hero_group.draw(self.window)
        self.enemy_group.update()
        self.enemy_group.draw(self.window)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.window)

    # 碰撞检测
    def __spritecollide(self):
        collidelist = pygame.sprite.spritecollide(self.hero, self.enemy_group, True, \
                                    collided=pygame.sprite.collide_mask)
        if len(collidelist) > 0:
            self.game_over()
        # 子弹与敌机是否碰撞
        for bullet in self.hero.bullet_group:
            collidelist = pygame.sprite.spritecollide(bullet, self.enemy_group, True,\
                                        collided=pygame.sprite.collide_mask)
            if len(collidelist) > 0:
                bullet.kill()


    # 游戏结束
    def game_over(self):
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = GamePlane()
    game.game_start()


