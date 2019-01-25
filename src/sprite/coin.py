
from src.tool.init import *


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bonus_img['coin1']
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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
        self.coin_rotate = [bonus_img['coin1'], bonus_img['coin2'], bonus_img['coin3'], bonus_img['coin4']]