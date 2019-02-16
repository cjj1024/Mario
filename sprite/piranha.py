import pygame

from .enemy import *
from tool.init import *


class Piranha(Enemy):
    def __init__(self, type, x, y):
        Enemy.__init__(self, type, x, y)



    def init_image(self):
        self.open_img = piranha_img[0]
        self.close_img = piranha_img[1]

        self.image = self.open_img