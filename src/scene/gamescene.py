import sys

from src.sprite.mario import *
from src.tool.character import *
from src.scene.level import *


class GameScene():
    def __init__(self, screen):
        self.screen = screen
        
        self.level = Level(1)
        
        self.player_group = pygame.sprite.Group()
        self.bonus_group = pygame.sprite.Group()

        self.mario = Mario()
        self.player_group.add(self.mario)



    def show(self):
        clock = pygame.time.Clock()
        while self.mario.alive():
            self.show_info()

            self.check_event()

            self.level.update(self.screen)
            self.bonus_group.update()
            self.bonus_group.draw(self.screen)
            self.player_group.update()
            self.player_group.draw(self.screen)

            self.move_mario()
            self.move_enemy()

            pygame.display.update()

            clock.tick(60)


    # 根据mario的x, y轴的速度移动mario
    # 在x轴, y轴移动后, 检测碰撞, 处理碰撞
    def move_mario(self):
        if self.mario.speed_x != 0:
            self.mario.rect.x += self.mario.speed_x
            self.check_move_scene()
            self.check_mario_border()
            self.check_mario_collision_x()

        if self.mario.speed_y != 0:
            self.mario.rect.y += self.mario.speed_y
            self.check_mario_border()
            self.check_mario_collision_y()


    # 检测是否移动场景
    # 当mairo走过屏幕的一半时, 移动场景
    def check_move_scene(self):
        if self.mario.rect.x > 400 and self.mario.speed_x > 0 \
           and self.level.start_x + self.mario.speed_x + 800 < self.level.length:
            self.level.start_x += self.mario.speed_x

            self.mario.rect.x -= self.mario.speed_x

            for enemy in self.level.enemy_group:
                enemy.rect.x -= self.mario.speed_x

            for bonus in self.bonus_group:
                bonus.rect.x -= self.mario.speed_x


    # 检测mario在x轴上的碰撞
    def check_mario_collision_x(self):
        brick = pygame.sprite.spritecollideany(self.mario, self.level.brick_group)
        pipe = pygame.sprite.spritecollideany(self.mario, self.level.pipe_group)

        if brick:
            self.process_mario_collision_x(brick)

        if pipe:
            self.process_mario_collision_x(pipe)


    # 处理Mario在x轴上的碰撞
    def process_mario_collision_x(self, collider):
        if self.mario.rect.x < collider.rect.x:
            self.mario.rect.right = collider.rect.left
        else:
            self.mario.rect.left = collider.rect.right

        # mario在x轴上遇到碰撞, 则x水平速度置为0
        self.mario.speed_x = 0


    # 检测mario在y轴上的碰撞
    def check_mario_collision_y(self):
        brick = pygame.sprite.spritecollideany(self.mario, self.level.brick_group)
        pipe = pygame.sprite.spritecollideany(self.mario, self.level.pipe_group)

        if brick:
            self.process_mario_collision_y(brick)

        if pipe:
            self.process_mario_collision_y(pipe)


    # 处理mario在y轴上的碰撞
    def process_mario_collision_y(self, collider):
        if self.mario.rect.y < collider.rect.y:
            self.mario.rect.bottom = collider.rect.top
        else:
            self.mario.rect.top = collider.rect.bottom
            # 当mario用头撞击物体时, 处理奖励
            collider.bump(self.bonus_group)

        # mairo在y轴方向遇到碰撞, 垂直速度置为0
        self.mario.speed_y = 0

        # 如果mario在跳跃中遇到y轴方向的碰撞
        # 水平速度置为0
        if self.mario.status == JUMP:
            self.mario.speed_x = 0
            self.mario.set_shape(STAND)


    # 移动敌人
    # 移动后检测碰撞并处理碰撞
    def move_enemy(self):
        for enemy in self.level.enemy_group:
            enemy.rect.x += enemy.speed_x
            self.check_enemy_collision_x(enemy)

            enemy.rect.y += enemy.speed_y
            self.check_enemy_collision_y(enemy)

            self.check_enemy_border(enemy)


    # 检测敌人在x轴方向的碰撞
    # 碰到砖块, 水管则调转方向
    def check_enemy_collision_x(self, enemy):
        brick = pygame.sprite.spritecollideany(enemy, self.level.brick_group)
        pipe = pygame.sprite.spritecollideany(enemy, self.level.pipe_group)
        # other_enemy = pygame.sprite.spritecollideany(enemy, self.level.enemy_group)

        if brick:
            enemy.rotate_direction()

        if pipe:
            enemy.rotate_direction()

        # if other_enemy:
        #     enemy.rotate_direction()


    # 检测敌人在y轴方向的碰撞
    def check_enemy_collision_y(self, enemy):
        brick = pygame.sprite.spritecollideany(enemy, self.level.enemy_group)
        pipe = pygame.sprite.spritecollideany(enemy, self.level.pipe_group)

        if brick:
            enemy.speed_y = 0

        if pipe:
            enemy.speed_y = 0


    # 检测敌人边界, 超出边界则死亡
    def check_enemy_border(self, enemy):
        if enemy.rect.x < 0 or enemy.rect.x > self.level.length:
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


    # 展示信息
    def show_info(self):
        self.screen.fill(SKYBLUE, (0, 0, 800, 600))
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
