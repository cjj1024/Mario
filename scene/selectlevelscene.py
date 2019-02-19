import sys

from .scene import *
from tool.character import *


@Singleton
class SelectLevelScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.selected = 0

        self.num = 4


    def show(self):
        self.screen.fill(SKYBLUE, (0, 0, 800, 600))

        self.draw_level()

        self.check_event()

        pygame.display.update()


    def draw_level(self):
        write_chars(self.screen, '第一关', 48, WHITE, (0, 0))


    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 1) % self.num
                elif event.key == pygame.K_UP:
                    self.selected = (self.selected - 1) % self.num
                elif event.key == pygame.K_RETURN:
                    self.next_scene = GAME_SCENE