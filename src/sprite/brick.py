import pygame

from src.tool.init import *


class Brick(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.type = type

        self.init_image()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x


    def init_image(self):
        if self.type == 1001:
            self.image = brick_img[1]
        elif self.type == 1000:
            self.image = brick_img[0]
        elif self.type == 1002:
            self.image = brick_img[2]
        elif self.type == 2100:
            self.image = bonus_brick_img[1]
        elif self.type == 2200:
            self.image = bonus_brick_img[1]
        elif self.type == 2201:
            self.image = bonus_brick_img[1]
        elif self.type == 2202:
            self.image = bonus_brick_img[1]
        else:
            self.image = brick_img[0]


    def update(self, offset):
        self.rect.x = self.start_x - offset


# 砖块管理类
# 当Mario撞击扎砖块时, 根据砖块的类型做出相应的操作
class BrickManager():
    def __init__(self):
        pass
    # 1000 砖块1
    # 1001 砖块2
    # 1002 砖块3
    #
    # 2100 硬币箱子
    # 2200 长大蘑菇箱子
    # 2201 生命蘑菇箱子
    # 2202 死亡蘑菇箱子
    #
    # 3100 硬币
    # 3200 长大蘑菇
    # 3201 加命蘑菇
    # 3202 死亡蘑菇
    #
    # 判断哪种类型的砖块被撞击并做出相应的操作
    def bump(self, i, j):
        # 可被撞碎的砖块
        if level.map[i][j] == 1002:
            pygame.mixer.Sound.play(sound['brick_smash'])
            level.map[i][j] = 0
        # 有硬币的箱子
        elif level.map[i][j] == 2100:
            pygame.mixer.Sound.play(sound['coin'])
            level.map[i][j] = 1001
            level.map[i - 1][j] = 3100
        # 有长大蘑菇的箱子
        elif level.map[i][j] == 2200:
            pygame.mixer.Sound.play(sound['brick_smash'])
            level.map[i][j] = 1001
            level.map[i - 1][j] = 3200