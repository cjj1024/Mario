import pygame

from tool.globaldata import *
from .gamemenu import *
from .gamescene import *
from .deathscene import *
from .selectlevelscene import *


class SceneControl():
    def __init__(self, scene):
        self.scene = scene
        self.pre_scene = GAME_MENU_SCENE


    def show_scene(self):
        clock = pygame.time.Clock()
        while True:
            self.scene.show()

            if self.scene.next_scene != NOW_SCENE:
                if self.scene.next_scene == GAME_MENU_SCENE:
                    self.scene = GameMenu()
                    self.pre_scene = GAME_SCENE
                elif self.scene.next_scene == GAME_SCENE:
                    if self.pre_scene == SELECT_LEVEL_SCENE:
                        self.scene = GameScene(self.scene.level + 1)
                    else:
                        self.scene = GameScene()
                    self.pre_scene = GAME_SCENE
                elif self.scene.next_scene == DEATH_SCENE:
                    self.scene = DeathScene(self.scene.mario)
                    self.pre_scene = DEATH_SCENE
                elif self.scene.next_scene == SELECT_LEVEL_SCENE:
                    self.scene = SelectLevelScene()
                    self.pre_scene = SELECT_LEVEL_SCENE


            clock.tick(self.scene.fps)