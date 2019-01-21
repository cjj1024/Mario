import sys
from pygame.locals import *

from src.sprite.mario import *

class GameScene():
    def __init__(self, screen):
        self.screen = screen

    def show(self):
        mario = Mario()
        marioGroup = pygame.sprite.Group()
        marioGroup.add(mario)
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(0)
                    elif event.key == K_LEFT:
                        mario.set_status(WALK)
                        mario.set_direction(LEFT)
                    elif event.key == K_RIGHT:
                        mario.set_status(WALK)
                        mario.set_direction(RIGHT)
                    else:
                        mario.set_status(STAND)
                else:
                    mario.set_status(STAND)


            self.screen.blit(background['background'], (0, 0))
            for i in range(0, 800, 40):
                self.screen.blit(ground['brick'], (i, 560))
            marioGroup.update()
            marioGroup.draw(self.screen)
            pygame.display.update()
            clock.tick(30)
