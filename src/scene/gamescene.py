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
        level.start_x = 0

    def show(self):
        clock = pygame.time.Clock()
        while self.mario.alive():
            self.draw_background()

            self.check_event()

            self.palyer.update()
            self.palyer.draw(self.screen)
            self.enemy.update()
            self.enemy.draw(self.screen)
            self.bonus.update()
            self.bonus.draw(self.screen)
            pygame.display.update()

            # 处理与敌人发生碰撞
            self.mario.process_enemy_collision(self.enemy)

            # 处理与奖励蘑菇发生碰撞
            self.mario.process_bonus_collision(self.bonus)

            clock.tick(60)

    def draw_background(self):
        self.screen.fill(SKYBLUE, (0, 0, 800, 600))
        if self.mario.check_move_scene() and level.start_x + 10 + 800 <= level.length:
            level.start_x += 10
        x = level.start_x
        end = level.start_x + 800
        if end == level.length:
            end -= 40
        if end + 40 < level.length:
            end += 40
        while x <= end:
            j = int(x / 40)
            for i in range(15):
                if level.map[i][j] == 1000:
                    self.screen.blit(brick_img[0], (j * 40 - level.start_x, i * 40))
                elif level.map[i][j] == 1001:
                    self.screen.blit(brick_img[1], (j * 40 - level.start_x, i * 40))
                elif level.map[i][j] == 1002:
                    self.screen.blit(brick_img[2], (j * 40 - level.start_x, i * 40))
                elif level.map[i][j] == 100:
                    self.screen.blit(brushwood_img[0], (j * 40 - level.start_x, i * 40))
                elif level.map[i][j] == 101:
                    self.screen.blit(brushwood_img[1], (j * 40 - level.start_x, i * 40))
                elif level.map[i][j] == 200:
                    self.screen.blit(cloud_img[0], (j * 40 - level.start_x, i * 40))
                elif level.map[i][j] == 201:
                    self.screen.blit(cloud_img[1], (j * 40 - level.start_x, i * 40))
                elif level.map[i][j] == 1200:
                    self.screen.blit(pipe_img[0], (j * 40 - level.start_x, i * 40))
                elif level.map[i][j] == 2100:
                    self.screen.blit(bonus_brick_img[1], (j * 40 - level.start_x, i * 40))
                elif level.map[i][j] == 2200:
                    self.screen.blit(bonus_brick_img[1], (j * 40 - level.start_x, i * 40))
                elif level.map[i][j] == 2201:
                    self.screen.blit(bonus_brick_img[1], (j * 40 - level.start_x, i * 40))
                elif level.map[i][j] == 2202:
                    self.screen.blit(bonus_brick_img[1], (j * 40 - level.start_x, i * 40))
                elif level.map[i][j] == 2100:
                    self.bonus.add(Coin(j * 40 - level.start_x, i * 40))
                    level.map[i][j] = 0
                elif level.map[i][j] == 2201:
                    self.bonus.add(Mushroom(j * 40 - level.start_x, i * 40))
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
                    self.mario.set_direction(NODIRECTION)
            else:
                self.mario.set_direction(NODIRECTION)
                self.mario.set_status(STAND)
