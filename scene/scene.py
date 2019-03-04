import pygame
from functools import wraps

from tool.globaldata import *


class Scene():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.fps = 60
        self.next_scene = NOW_SCENE


    def show(self):
        pygame.display.update()


    def process_event(self, event):
        pass


def Singleton(cls):
    _instance = {}

    @wraps(cls)
    def _singlenton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singlenton