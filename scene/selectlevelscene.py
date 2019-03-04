import sys

from . scene import *
from tool.character import *
from tool.globaldata import *


@Singleton
class SelectLevelScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.level = 0

        self.row = 1
        self.column = 4
        self.num = 5


    def show(self):
        self.screen.fill(SKYBLUE, (0, 0, 800, 600))

        self.draw_level()

        pygame.display.update()


    def draw_level(self):
        pygame.draw.rect(self.screen, BLUE,
                         (int(self.level % self.column) * 200, int(self.level / self.column) * 100, 120, 50))

        write_chars(self.screen, '第一关', 48, WHITE, (0, 0))
        write_chars(self.screen, '第二关', 48, WHITE, (200, 0))
        write_chars(self.screen, '第三关', 48, WHITE, (400, 0))
        write_chars(self.screen, '第四关', 48, WHITE, (600, 0))
        write_chars(self.screen, '第五关', 48, WHITE, (0, 100))


    def process_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)
            elif event.key == pygame.K_DOWN:
                self.level = (self.level + self.column) % self.num
            elif event.key == pygame.K_UP:
                self.level = (self.level - self.column) % self.num
            elif event.key == pygame.K_LEFT:
                self.level = (self.level - 1) % self.num
            elif event.key == pygame.K_RIGHT:
                self.level = (self.level + 1) % self.num
            elif event.key == pygame.K_RETURN:
                self.next_scene = GAME_SCENE