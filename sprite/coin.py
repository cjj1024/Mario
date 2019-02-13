import pygame

from tool.init import *

# 硬币类
# 当Mario撞击有硬币的砖块时, 出现在砖块的上方
# 硬币出现后, 旋转一定时间后消失
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = coin_img[1]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.y -= self.rect.height
        # 表示硬币剩余的时间, 为0时消失
        self.life = 9
        self.animationNum = 0

        self.init_animation()


    def update(self):
        if  self.life == 0:
            self.kill()

        if self.animationNum < len(self.coin_rotate) - 1:
            self.animationNum += 1
        else:
            self.animationNum = 0

        self.image = self.coin_rotate[self.animationNum]

        self.life -= 1


    def init_animation(self):
        self.coin_rotate = [coin_img[0], coin_img[1], coin_img[2], coin_img[3]]