from .enemy import *
from tool.init import *


class Goomba(Enemy):
    def __init__(self, type, x, y):
        Enemy.__init__(self, type, x, y)


    def init_image(self):
        self.walk_left_img = goomba_img[1]
        self.walk_right_img = goomba_img[0]
        self.death_img = goomba_img[2]

        self.image = self.walk_left_img