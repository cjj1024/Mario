import sys
from pygame.locals import *

from src.tool.init import *

class GameScene():
    def __init__(self, screen):
        self.screen = screen

    def show(self):
        self.screen.fill((100, 150, 250), (0, 0, 800, 600))
        for i in range(0, 800, 40):
            self.screen.blit(ground['brick'], (i, 560))


        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == KEYDOWN:
                    if event.type == K_ESCAPE:
                        sys.exit(0)

            pygame.display.update()
