import pygame

from tool.globaldata import *
from . gamemenu import *
from . gamescene import *
from . deathscene import *
from . selectlevelscene import *


class SceneControl():
    def __init__(self, scene):
        self.scene = scene
        self.pre_scene = GAME_MENU_SCENE
        self.is_active = True


    def show_scene(self):
        clock = pygame.time.Clock()
        while True:
            self.scene.show()

            self.check_event()

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


    def check_event(self):
        if not self.is_active and pygame.display.get_active():
            self.is_active = True
            pygame.mixer.music.unpause()
        elif not pygame.display.get_active():
            self.is_active = False
            pygame.mixer.music.pause()

        for event in pygame.event.get():
            self.scene.process_event(event)