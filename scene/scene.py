import pygame
from functools import wraps

from tool.globaldata import *
from tool.singleton import *


class Scene():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.fps = 60
        self.self_scene = None
        self.next_scene = NOW_SCENE


    def show(self):
        pygame.display.update()


    def enter_scent(self):
        pass


    def process_event(self, event):
        pass


