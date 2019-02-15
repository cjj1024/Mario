import pygame

from tool.globaldata import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = type

        self.init_image()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.direction = LEFT

        self.speed_x = -2
        self.speed_y = 0

        self.status = WALK


    def update(self):
        if self.rect.right < 0:
            self.kill()
        if abs(self.speed_y + GRAVITY_Y) < MAX_SPEED_Y:
            self.speed_y += GRAVITY_Y
        if self.status == DEATH:
            self.death()
        elif self.status == WALK:
            self.walk()


    def death(self):
        self.image = self.death_img
        self.rect.x -= 5


    def walk(self):
        if self.direction == LEFT:
            self.image = self.walk_left_img
        elif self.direction == RIGHT:
            self.image = self.walk_right_img


    # 掉头
    def rotate_direction(self):
        if self.direction == LEFT:
            self.direction = RIGHT
        elif self.direction == RIGHT:
            self.direction = LEFT

        self.speed_x = -self.speed_x


    def set_status(self, status):
        if self.status != DEATH:
            self.status = status


    def init_image(self):
        pass