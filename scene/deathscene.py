import pygame

from tool.init import *
from tool.character import *
from . scene import *


@Singleton
class DeathScene(Scene):
    def __init__(self, mario):
        Scene.__init__(self)

        self.self_scene = DEATH_SCENE

        self.mario = mario
        self.remain_time = DEATH_SCENE_TIME

        self.globalData = GlobalData()


    def show(self):
        self.screen.fill(BLACK, (0, 0, 800, 600))

        write_chars(self.screen, "Y O U  D E A D", 64, WHITE, (250, 50))
        write_chars(self.screen, "硬币: " + str(self.mario.coin_num), 48, WHITE, (100, 200))
        write_chars(self.screen, "分数: " + str(self.mario.score), 48, WHITE, (300, 200))
        write_chars(self.screen, "关卡: " + str(self.mario.level_num), 48, WHITE, (500, 200))

        self.screen.blit(mario_small_right_img[0][6], (300, 400))
        write_chars(self.screen, "X", 32, WHITE, (360, 400))
        write_chars(self.screen, str(self.mario.life), 48, WHITE, (400, 400))

        pygame.display.update()

        self.remain_time -= 1
        if self.remain_time < 0:
            self.remain_time = DEATH_SCENE_TIME
            self.globalData.scene = GAME_SCENE