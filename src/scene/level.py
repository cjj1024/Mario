import json
import pygame
from src.sprite.brick import *
from src.sprite.goomba import *
from src.sprite.pipe import *
from src.sprite.background import *


# 关卡信息保存在json文件中
# 读取关卡信息, 初始化精灵, 并加入相应的精灵组
class Level():
    def __init__(self, level):
        filename = './res/level/level' + str(level) + '.json'
        with open(filename) as fp:
            data = json.load(fp)

        self.length = data['length']
        self.start_x = 0

        self.brick_group = pygame.sprite.Group()
        self.pipe_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.background_group = pygame.sprite.Group()

        # 把屏幕划分成二维的格子
        # 每个格子为40x40px
        # 0 什么都没有
        #
        # 100 小灌木
        # 101 大灌木
        # 200 小云
        # 201 大云
        #
        # 1000 砖块1  地面
        # 1001 砖块2  不可摧毁的砖块
        # 1002 砖块3  可崔摧毁的砖块
        #
        # 1200 管道
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
        # 4000 Goomba
        for x, y in data['pipe']:
            self.pipe_group.add(Pipe(1200, x, y))

        for x, y in data['brick1']:
            self.brick_group.add(Brick(1000, x, y))

        for x, y in data['brick2']:
            self.brick_group.add(Brick(1001, x, y))

        for x, y in data['brick3']:
            self.brick_group.add(Brick(1002, x, y))

        for x, y in data['coin']:
            self.brick_group.add(Brick(2100, x, y))

        for x, y in data['mushroom_grow']:
            self.brick_group.add(Brick(2200, x, y))

        for x, y in data['mushroom_life']:
            self.brick_group.add(Brick(2201, x, y))

        for x, y in data['mushroom_death']:
            self.brick_group.add(Brick(2202, x, y))

        for x, y in data['goomba']:
            self.enemy_group.add(Goomba(x, y))

        for x, y in data['cloud1']:
            self.background_group.add(Background(cloud_img[0], x, y))

        for x, y in data['cloud2']:
            self.background_group.add(Background(cloud_img[1], x, y))

        for x, y in data['brushwood1']:
            self.background_group.add(Background(brushwood_img[0], x, y))

        for x, y in data['brushwood2']:
            self.background_group.add(Background(brushwood_img[1], x, y))


    def update(self, screen):
        self.background_group.update(self.start_x)
        self.background_group.draw(screen)

        self.brick_group.update(self.start_x)
        self.brick_group.draw(screen)

        self.enemy_group.update()
        self.enemy_group.draw(screen)

        self.pipe_group.update(self.start_x)
        self.pipe_group.draw(screen)
