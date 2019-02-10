import pygame

from src.tool.init import *
from .coin import *


# 1000 砖块1  地面
# 1001 砖块2  不可摧毁的砖块
# 1002 砖块3  可摧毁的砖块
# 1003 砖块4  奖励被拿走后的砖块
#
# 2100 硬币箱子
# 2200 长大蘑菇箱子
# 2201 生命蘑菇箱子
# 2202 死亡蘑菇箱子
class Brick(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.type = type

        self.init_image()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x


    # 0 地面
    # 1 不可摧毁的砖块
    # 2 可崔摧毁的砖块
    # 6 奖励出现后的砖块
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

    # 1000 砖块1  地面
    # 1001 砖块2  不可摧毁的砖块
    # 1002 砖块3  可摧毁的砖块
    # 1003 砖块4  奖励被拿走后的砖块
    #
    # 2100 硬币箱子
    # 2200 长大蘑菇箱子
    # 2201 生命蘑菇箱子
    # 2202 死亡蘑菇箱子
    # 处理mario用头撞击砖块时应给的奖励
    def bump(self, group):
        if self.type == 1002:
            self.kill()
        elif self.type == 2100:
            self.type = 1003
            self.image = brick_img[6]
            group.add(Coin(self.rect.x, self.rect.y))
        elif self.type == 2200:
            self.type = 1003
            self.image = brick_img[6]
        elif self.type == 2201:
            self.type = 1003
            self.image = brick_img[6]
        elif self.type == 2202:
            self.type = 1003
            self.image = brick_img[6]


    # offset为世界坐标与屏幕坐标在x轴上的偏移
    def update(self, offset):
        self.rect.x = self.start_x - offset
