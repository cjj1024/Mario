import pygame
from pygame.locals import *

from src.tool.init import *


class Character():
    def __init__(self, c, size=FONT_SIZE, antialias=False, color=WHITE, background=None):
        self.image = font.render(c, antialias, color, background)

        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size, self.size))


char_img = {}


def add_chars(text, size=FONT_SIZE, antialias=False, color=WHITE, background=None):
    text_list = list(text)
    for c in text_list:
        if c not in char_img.keys():
            char_img[c] = Character(c, size, antialias, color, background)
            print(c, char_img[c].image.get_rect())


def write_chars(screen, text, size=FONT_SIZE, color=WHITE, pos=(0, 0)):
    add_chars(text=text, size=size, color=color)
    text_list = list(text)
    offset = 0
    for c in text_list:
        screen.blit(char_img[c].image, (pos[0] + offset, pos[1]))
        offset += char_img[c].size