import pygame

from tool.init import *
from tool.character import *
from .scene import *


@Singleton
class DeathScene(Scene):
    def __init__(self, mario):
        Scene.__init__(self)

        self.mario = mario
        self.remain_time = DEATH_SCENE_TIME


    def show(self):
        self.screen.fill(BLACK, (0, 0, 800, 600))

        write_chars(self.screen, "硬币: " + str(self.mario.coin_num), 48, WHITE, (100, 100))
        write_chars(self.screen, "分数: " + str(self.mario.score), 48, WHITE, (300, 100))
        write_chars(self.screen, "关卡: " + str(self.mario.level_num), 48, WHITE, (500, 100))

        self.screen.blit(mario_small_right_img[0][6], (300, 300))
        write_chars(self.screen, "X", 32, WHITE, (360, 300))
        write_chars(self.screen, str(self.mario.life), 48, WHITE, (400, 300))

        pygame.display.update()

        self.remain_time -= 1
        if self.remain_time < 0:
            self.next_scene = GAME_SCENE
            self.remain_time = DEATH_SCENE_TIME
        else:
            self.next_scene = NOW_SCENE