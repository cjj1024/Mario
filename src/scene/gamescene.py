import sys
from pygame.locals import *

from src.sprite.mario import *
from src.sprite.goomba import *
from src.sprite.coin import *
from src.sprite.mushroom import *


class GameScene():
    def __init__(self, screen):
        self.screen = screen
        self.palyer = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.bonus = pygame.sprite.Group()
        self.mario = Mario()
        self.palyer.add(self.mario)
        self.toomba = Goomba()
        self.enemy.add(self.toomba)
        level.start = 0


    def show(self):
        clock = pygame.time.Clock()
        while True:
            self.draw_background()

            self.check_event()

            # 处理与敌人发生碰撞
            self.mario.process_enemy_collision(self.enemy)

            # 处理与奖励蘑菇发生碰撞
            self.mario.process_bonus_collision(self.bonus)


            self.palyer.update()
            self.palyer.draw(self.screen)
            self.enemy.update()
            self.enemy.draw(self.screen)
            self.bonus.update()
            self.bonus.draw(self.screen)
            pygame.display.update()
            clock.tick(30)


    def draw_background(self):
        self.screen.blit(background_img['background'], (0, 0))
        if self.mario.check_move_scene() and level.start + 840 <= level.length:
            level.start += 10
        x = level.start
        end = level.start + 800
        while x <= end:
            j = int(x / 40)
            for i in range(15):
                if level.map[i][j] == 1:
                    self.screen.blit(ground_img['brick'], (j * 40 - level.start, i * 40))
                elif level.map[i][j] == 2:
                    self.screen.blit(bonus_img['crackstone'], (j * 40 - level.start, i * 40))
                elif level.map[i][j] == 3:
                    self.screen.blit(bonus_img['box'], (j * 40 - level.start, i * 40))
                elif level.map[i][j] == 4:
                    self.screen.blit(bonus_img['boxempty'], (j * 40 - level.start, i * 40))
                elif level.map[i][j] == 5:
                    self.bonus.add(Coin(j * 40 - level.start, i * 40))
                    level.map[i][j] = 0
                elif level.map[i][j] == 6:
                    self.screen.blit(bonus_img['box'], (j * 40 - level.start, i * 40))
                elif level.map[i][j] == 7:
                    self.bonus.add(Mushroom(j * 40 - level.start, i * 40))
                    level.map[i][j] = 0
            x += 40


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
