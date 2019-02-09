import pygame

from src.tool.init import *


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.init_image()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x


    def init_image(self):
        self.image = pipe_img[0]


    def update(self, offset):
        self.rect.x = self.start_x - offset