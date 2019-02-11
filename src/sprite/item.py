import pygame

from src.tool.init import *


class Item(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.type = type

        self.init_image()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x


    def init_image(self):
        pass


    def bump(self, *args):
        pass

    def update(self, offset):
        self.rect.x = self.start_x - offset