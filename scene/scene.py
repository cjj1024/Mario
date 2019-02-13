import pygame

from tool.globaldata import *


class Scene():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.fps = 60
        self.next_scene = NOWSCENE