from . enemy import *
from tool.init import *


class Koopa(WalkEnemy):
    def __init__(self, type, x, y):
        WalkEnemy.__init__(self, type, x, y)


    def init_image(self):
        self.walk_left_img = [koopa_left_img[0], koopa_left_img[1]]
        self.walk_right_img = [koopa_right_img[0], koopa_right_img[1]]
        self.death_img = koopa_left_img[4]

        self.image = self.walk_left_img[0]