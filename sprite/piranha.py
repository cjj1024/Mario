import pygame

from . enemy import *
from tool.init import *


class Piranha(Enemy):
    def __init__(self, type, x, y):
        Enemy.__init__(self, type, x, y)

        self.start_x = x
        self.status = PIRANHA_CLOSE

        self.animation_num = 0
        self.attack_time = 90



    def init_image(self):
        self.cut_img = [piranha_img[0], piranha_img[1]]

        self.image = self.cut_img[0]


    def update(self, offset):
        self.rect.x = self.start_x - offset

        self.animation_num = (self.animation_num + 0.05) % (len(self.cut_img))
        self.image = self.cut_img[int(self.animation_num)]

        self.attack_time -= 1
        if self.attack_time == 20:
            self.rect.y -= 50
        elif self.attack_time < 0:
            self.attack_time = 90
            self.rect.y += 50
