import pygame

from tool.globaldata import *
from . gamemenu import *
from . gamescene import *
from . deathscene import *
from . selectlevelscene import *
from . winscene import *
from . selectdifficultyscene import *


class SceneControl():
    def __init__(self, scene):
        self.scene = scene
        self.is_active = True
        self.is_pause = False


    def show_scene(self):
        clock = pygame.time.Clock()
        while True:
            if not self.is_active or self.is_pause:
                clock.tick(self.scene.fps)
                self.check_event()
                continue

            self.scene.show()
            self.check_event()


            if self.scene.next_scene != NOW_SCENE:
                pre_scene = self.scene.self_scene
                next_scene = self.scene.next_scene
                self.scene.next_scene = NOW_SCENE

                if next_scene == GAME_MENU_SCENE:
                    self.scene = GameMenu()
                    print('game menu')
                elif next_scene == GAME_SCENE:
                    if pre_scene == SELECT_LEVEL_SCENE:
                        level = self.scene.level
                        self.scene = GameScene()
                        self.scene.set_level(level)
                        self.scene.mario.__init__()
                    else:
                        self.scene = GameScene()
                        self.scene.mario.__init__()


                elif next_scene == DEATH_SCENE:
                    self.scene = DeathScene(self.scene.mario)
                elif next_scene == WIN_SCENE:
                    self.scene = WinScene(self.scene.mario)
                elif next_scene == SELECT_LEVEL_SCENE:
                    self.scene = SelectLevelScene()
                elif next_scene == SELECT_DIFFICULTY_SCENE:
                    self.scene = SelectDifficultyScene()

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
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.key == pygame.K_SPACE:
                    self.is_pause = not self.is_pause
                    if self.is_pause:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()