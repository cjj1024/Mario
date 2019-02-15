import pygame

from tool.init import *

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mario_small_right_img[0][6]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 300
        self.shape = SMALL
        self.status = STAND
        self.direction = NODIRECTION
        self.animation_num = 0
        self.speed_x = 0
        self.speed_y = 0

        self.is_collider = True

        self.score = 0
        self.coin_num = 0
        self.life = 3
        self.level_num = 1

        self.init_image()
        self.set_shape(SMALL)


    def update(self):
        if abs(self.speed_y + GRAVITY_Y) < MAX_SPEED_Y:
            self.speed_y += GRAVITY_Y

        if self.status == DEATH:
            self.death()
        elif self.status == STAND:
            self.stand()
        elif self.status == WALK:
            self.walk()
        elif self.status == JUMP:
            self.jump()


    def death(self):
        if self.rect.y >= 560:
            self.kill()
            self.rect.x = 0
            self.rect.y = 300
            self.status = STAND
            self.is_collider = True

        self.image = self.small_dead_img


    def jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speed_x = -3
            self.image = self.jump_left
        elif key[pygame.K_RIGHT]:
            self.speed_x = 3
            self.image = self.jump_right


    def walk(self):
        # 循环播放动画
        self.animation_num = (self.animation_num + 1) % (len(self.walk_left) - 1)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if abs(self.speed_x) < MAX_SPEED_X:
                self.speed_x -= GRAVITY_X
            self.image = self.walk_left[self.animation_num]
        elif key[pygame.K_RIGHT]:
            if abs(self.speed_x) < MAX_SPEED_X:
                self.speed_x += GRAVITY_X
            self.image = self.walk_right[self.animation_num]
        else:
            self.speed_x = 0
            self.status = STAND


    def stand(self):
        if self.direction == LEFT:
            self.image = self.stand_left
        else:
            self.image = self.stand_right


    def set_status(self, status):
        if self.status == DEATH or self.status == JUMP:
            return

        self.status = status

        # 要变成死亡状态
        if status == DEATH:
            if self.shape == BIG:
                self.shape = SMALL
            elif self.shape == SMALL:
                self.life -= 1
                self.status = DEATH
                self.is_collider = False
                self.speed_y = INIT_JUMP_SPEED_Y
                self.speed_x = 0
                pygame.mixer.Sound.play(sound['death'])
        elif status == JUMP:
            self.speed_y = INIT_JUMP_SPEED_Y
            pygame.mixer.Sound.play(sound['small_jump'])
        elif status == STAND:
            self.speed_x = 0
            self.speed_y = 0


    def set_direction(self, direction):
        if self.status != JUMP:
            self.direction = direction


    def set_shape(self, shape):
        self.shape = shape
        if self.shape == SMALL:
            self.stand_left = self.small_stand_left_img
            self.stand_right = self.small_stand_right_img
            self.walk_left = self.small_walk_left_img
            self.walk_right = self.small_walk_right_img
            self.jump_left = self.small_jump_left_img
            self.jump_right = self.small_jump_right_img

            self.rect.width = self.stand_left.get_rect().width
            self.rect.height = self.stand_left.get_rect().height
            self.rect.y += 40
        elif self.shape == BIG:
            self.stand_left = self.big_stand_left_img
            self.stand_right = self.big_stand_right_img
            self.walk_left = self.big_walk_left_img
            self.walk_right = self.big_walk_right_img
            self.jump_left = self.big_jump_left_img
            self.jump_right = self.big_jump_right_img

            self.rect.width = self.stand_left.get_rect().width
            self.rect.height = self.stand_left.get_rect().height
            self.rect.y -= 40


    def init_image(self):
        self.big_stand_right_img = mario_big_right_img_img[0][6]
        self.big_stand_left_img = mario_big_left[0][6]

        self.big_walk_right_img = [mario_big_right_img_img[0][0], mario_big_right_img_img[0][1],
                                   mario_big_right_img_img[0][2]]
        self.big_walk_left_img = [mario_big_left[0][0], mario_big_left[0][1],
                                  mario_big_left[0][2]]

        self.big_jump_right_img = mario_big_right_img_img[0][4]
        self.big_jump_left_img = mario_big_left[0][4]

        self.small_dead_img = mario_small_right_img[0][5]

        self.small_stand_right_img = mario_small_right_img[0][6]
        self.small_stand_left_img = mario_small_left_img[0][6]

        self.small_walk_right_img = [mario_small_right_img[0][0], mario_small_right_img[0][1],
                                     mario_small_right_img[0][2]]
        self.small_walk_left_img = [mario_small_left_img[0][0], mario_small_left_img[0][1],
                                    mario_small_left_img[0][2]]

        self.small_jump_right_img = mario_small_right_img[0][4]
        self.small_jump_left_img = mario_small_left_img[0][4]

        self.small_dead_img = mario_small_right_img[0][5]



