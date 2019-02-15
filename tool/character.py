import pygame

from tool.globaldata import *
from tool.init import *


class Character():
    def __init__(self, c, size=FONT_SIZE, antialias=False, color=WHITE, background=None):
        self.image = font.render(c, antialias, color, background)

        self.size = (self.image.get_rect().width, self.image.get_rect().height)
        self.size = (int(self.size[0] * size / self.size[1]), int(size))
        self.image = pygame.transform.scale(self.image, self.size)


char_img = {}


def add_chars(text, antialias=False, color=WHITE, background=None):
    text_list = list(text)
    for c in text_list:
        if c not in char_img.keys():
            char_img[c] = Character(c, FONT_SIZE, antialias, color, background)


def write_chars(screen, text, size=FONT_SIZE, color=WHITE, pos=(0, 0)):
    add_chars(text=text, color=color)
    text_list = list(text)
    offset = 0
    for c in text_list:
        img = pygame.transform.scale(char_img[c].image,
                                     (int(char_img[c].size[0] * size / char_img[c].size[1]), size))
        screen.blit(img, (pos[0] + offset, pos[1]))
        offset += char_img[c].size[0]