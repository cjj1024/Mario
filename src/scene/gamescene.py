import sys

from src.sprite.mario import *
from src.sprite.coin import *
from src.sprite.mushroom import *
from src.tool.character import *
from src.scene.level import *


class GameScene():
    def __init__(self, screen):
        self.screen = screen
        
        self.level = Level(3)
        
        self.palyer = pygame.sprite.Group()
        self.bonus = pygame.sprite.Group()
        self.mario = Mario()
        self.palyer.add(self.mario)
        self.level.start_x = 0

    def show(self):
        clock = pygame.time.Clock()
        while self.mario.alive():
            self.draw_background()

            self.check_event()

            self.move_mario()
            self.move_enemy()

            self.palyer.update()
            self.palyer.draw(self.screen)
            self.bonus.update()
            self.bonus.draw(self.screen)
            self.level.update(self.screen)

            pygame.display.update()

            clock.tick(60)


    def move_mario(self):
        self.mario.rect.x += self.mario.speed_x
        self.check_move_scene()
        self.check_mario_border()
        self.check_mario_collision_x()

        if self.mario.speed_y != 0:
            self.mario.rect.y += self.mario.speed_y
            self.check_mario_border()
            self.check_mario_collision_y()


    def check_move_scene(self):
        if self.mario.rect.x > 400 and self.mario.speed_x > 0 \
           and self.level.start_x + self.mario.speed_x + 800 < self.level.length:
            self.level.start_x += self.mario.speed_x
            self.mario.rect.x -= self.mario.speed_x


    def check_mario_collision_x(self):
        brick = pygame.sprite.spritecollideany(self.mario, self.level.brick_group)
        pipe = pygame.sprite.spritecollideany(self.mario, self.level.pipe_group)

        if brick:
            self.process_mario_brick_collision_x(brick)

        if pipe:
            self.process_mario_brick_collision_x(pipe)


    def process_mario_brick_collision_x(self, brick):
        if self.mario.rect.x < brick.rect.x:
            self.mario.rect.right = brick.rect.left
        else:
            self.mario.rect.left = brick.rect.right

        self.mario.speed_x = 0


    def check_mario_collision_y(self):
        brick = pygame.sprite.spritecollideany(self.mario, self.level.brick_group)

        if brick:
            self.process_mario_brick_collision_y(brick)


    def process_mario_brick_collision_y(self, brick):
        if self.mario.rect.y > brick.rect.y:
            self.mario.rect.top = brick.rect.bottom
        else:
            self.mario.rect.bottom = brick.rect.top

        self.mario.speed_y = 0
        if self.mario.status == JUMP:
            self.mario.speed_x = 0
            self.mario.set_shape(STAND)



    def move_enemy(self):
        for enemy in self.level.enemy_group:
            enemy.rect.x += enemy.speed_x
            self.check_enemy_collision_x(enemy)

            enemy.rect.y += enemy.speed_y
            self.check_enemy_collision_y(enemy)

            self.check_enemy_border(enemy)


    def check_enemy_collision_x(self, enemy):
        brick = pygame.sprite.spritecollideany(enemy, self.level.brick_group)
        pipe = pygame.sprite.spritecollideany(enemy, self.level.pipe_group)
        # other_enemy = pygame.sprite.spritecollideany(enemy, self.level.enemy_group)

        if brick:

            enemy.rotate_direction()

        if pipe:
            print(pipe.rect)
            enemy.rotate_direction()

        # if other_enemy:
        #     enemy.rotate_direction()


    def check_enemy_collision_y(self, enemy):
        brick = pygame.sprite.spritecollideany(enemy, self.level.enemy_group)
        pipe = pygame.sprite.spritecollideany(enemy, self.level.pipe_group)

        if brick:
            enemy.speed_y = 0

        if pipe:
            enemy.speed_y = 0



    def check_enemy_border(self, enemy):
        if enemy.rect.x - self.level.start_x < 0 or enemy.rect.x - self.level.start_x > 800 \
            or enemy.rect.y < 0 or enemy.rect.y > 600:
            enemy.kill()



    def check_mario_border(self):
        if self.mario.rect.left < 0:
            self.mario.rect.left = 0

        if self.mario.rect.right > 800:
            self.mario.rect.right = 800

        if self.mario.rect.top < 0:
            self.mario.rect.top = 0

        if self.mario.rect.bottom > 560:
            self.mario.rect.bottom = 560


    def draw_background(self):
        self.screen.fill(SKYBLUE, (0, 0, 800, 600))
        self.show_info()
        # x = self.level.start_x
        # end = self.level.start_x + 800
        # if end == self.level.length:
        #     end -= 40
        # if end + 40 < self.level.length:
        #     end += 40
        # while x <= end:
        #     j = int(x / 40)
        #     for i in range(15):
        #         if self.level.map[i][j] == 1000:
        #             self.screen.blit(brick_img[0], (j * 40 - self.level.start_x, i * 40))
        #         # elif self.level.map[i][j] == 1001:
        #         #     self.screen.blit(brick_img[1], (j * 40 - self.level.start_x, i * 40))
        #         # elif self.level.map[i][j] == 1002:
        #         #     self.screen.blit(brick_img[2], (j * 40 - self.level.start_x, i * 40))
        #         elif self.level.map[i][j] == 100:
        #             self.screen.blit(brushwood_img[0], (j * 40 - self.level.start_x, i * 40))
        #         elif self.level.map[i][j] == 101:
        #             self.screen.blit(brushwood_img[1], (j * 40 - self.level.start_x, i * 40))
        #         elif self.level.map[i][j] == 200:
        #             self.screen.blit(cloud_img[0], (j * 40 - self.level.start_x, i * 40))
        #         elif self.level.map[i][j] == 201:
        #             self.screen.blit(cloud_img[1], (j * 40 - self.level.start_x, i * 40))
        #         elif self.level.map[i][j] == 1200:
        #             self.screen.blit(pipe_img[0], (j * 40 - self.level.start_x, i * 40))
        #         # elif self.level.map[i][j] == 2100:
        #         #     self.screen.blit(bonus_brick_img[1], (j * 40 - self.level.start_x, i * 40))
        #         # elif self.level.map[i][j] == 2200:
        #         #     self.screen.blit(bonus_brick_img[1], (j * 40 - self.level.start_x, i * 40))
        #         # elif self.level.map[i][j] == 2201:
        #         #     self.screen.blit(bonus_brick_img[1], (j * 40 - self.level.start_x, i * 40))
        #         # elif self.level.map[i][j] == 2202:
        #         #     self.screen.blit(bonus_brick_img[1], (j * 40 - self.level.start_x, i * 40))
        #         elif self.level.map[i][j] == 2100:
        #             self.bonus.add(Coin(j * 40 - self.level.start_x, i * 40))
        #             self.level.map[i][j] = 0
        #         elif self.level.map[i][j] == 2201:
        #             self.bonus.add(Mushroom(j * 40 - self.level.start_x, i * 40))
        #             self.level.map[i][j] = 0
        #     x += 40

    def show_info(self):
        write_chars(self.screen, "分数: " + str(self.mario.score), 32, WHITE, (0, 0))


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
