import pygame

from tool.globaldata import *
from .gamemenu import *
from .gamescene import *
from .deathscene import *


class SceneControl():
    def __init__(self, scene):
        self.scene = scene


    def show_scene(self):
        clock = pygame.time.Clock()
        while True:
            self.scene.show()

            if self.scene.next_scene != NOW_SCENE:
                if self.scene.next_scene == GAME_MENU:
                    self.scene = GameMenu()
                elif self.scene.next_scene == GAME_SCENE:
                    self.scene = GameScene()
                elif self.scene.next_scene == DEATH_SCENE:
                    self.scene = DeathScene(self.scene.mario)

            clock.tick(self.scene.fps)