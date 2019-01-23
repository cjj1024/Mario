import sys
from pygame.locals import *

from src.sprite.mario import *
from src.sprite.goomba import *

class GameScene():
    def __init__(self, screen):
        self.screen = screen
        self.palyer = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.mario = Mario()
        self.palyer.add(self.mario)
        self.toomba = Goomba()
        self.enemy.add(self.toomba)

    def show(self):


        clock = pygame.time.Clock()
        while True:
            self.check_event()

            death = self.mario.detect_collision(self.enemy)
            if death[0] != 0:
                death[1].set_status(DEATH)


            self.screen.blit(background_img['background'], (0, 0))
            for i in range(0, 800, 40):
                self.screen.blit(ground_img['brick'], (i, 560))
            self.palyer.update()
            self.palyer.draw(self.screen)
            self.enemy.update()
            self.enemy.draw(self.screen)
            pygame.display.update()
            clock.tick(30)


    def check_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit(0)
                elif event.key == K_LEFT:
                    self.mario.set_status(WALK)
                    self.mario.set_direction(LEFT)
                elif event.key == K_RIGHT:
                    self.mario.set_status(WALK)
                    self.mario.set_direction(RIGHT)
                elif event.key == K_a:
                    self.mario.set_status(JUMP)
                else:
                    self.mario.set_status(STAND)
            else:
                self.mario.set_status(STAND)