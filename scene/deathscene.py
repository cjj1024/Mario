import pygame

from tool.init import *
from .scene import *


class DeathScene(Scene):
    def __init__(self, mario):
        Scene.__init__(self)

        self.mario = mario
        self.remain_time = 1000


    def show(self):
        clock = pygame.time.Clock()
        while self.remain_time > 0:
            self.screen.blit(mario_small_right_img[0][6], (300, 300))

            pygame.display.update()

            self.remain_time -= 1

            clock.tick(self.fps)