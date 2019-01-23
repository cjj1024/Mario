import sys
from pygame.locals import *

from src.sprite.mario import *
from src.sprite.goomba import *

class GameScene():
    def __init__(self, screen):
        self.screen = screen

    def show(self):
        palyer = pygame.sprite.Group()
        enemy = pygame.sprite.Group()
        mario = Mario()
        palyer.add(mario)
        toomba = Goomba()
        enemy.add(toomba)

        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(0)
                    elif event.key == K_LEFT:
                        mario.set_status(WALK)
                        mario.set_direction(LEFT)
                    elif event.key == K_RIGHT:
                        mario.set_status(WALK)
                        mario.set_direction(RIGHT)
                    elif event.key == K_a:
                        mario.set_status(JUMP)
                    else:
                        mario.set_status(STAND)
                else:
                    mario.set_status(STAND)

            if mario.detect_collision(enemy):
                mario.set_status(DEATH)

            self.screen.blit(background_img['background'], (0, 0))
            for i in range(0, 800, 40):
                self.screen.blit(ground_img['brick'], (i, 560))
            palyer.update()
            palyer.draw(self.screen)
            enemy.update()
            enemy.draw(self.screen)
            pygame.display.update()
            clock.tick(30)
