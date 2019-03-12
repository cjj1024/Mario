import pygame

from tool.init import *


# 3200 长大蘑菇
# 3201 加命蘑菇
# 3202 死亡蘑菇
class Mushroom(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        pygame.sprite.Sprite.__init__(self)
        # 蘑菇的类型
        self.type = type
        self.init_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.y -= self.rect.height
        self.direction = RIGHT
        self.speed_x = 2
        self.speed_y = 0


    def bump(self, player):
        if self.type == 3200:
            player.set_shape(BIG)
        elif self.type == 3201:
            player.life += 1
        elif self.type == 3202:
            player.set_status(DEATH)

        self.kill()


    def update(self):
        if self.rect.right < 0:
            self.kill()
        if abs(self.speed_y + GRAVITY_Y) < MAX_SPEED_Y:
            self.speed_y += GRAVITY_Y


    def init_image(self):
        print(self.type)
        if self.type == 3200:
            self.image = mushroom_img[0]
        elif self.type == 3201:
            self.image = mushroom_img[2]
        elif self.type == 3202:
            self.image = mushroom_img[4]
        else:
            self.image = mushroom_img[0]


    # 掉头
    def rotate_direction(self):
        if self.direction == LEFT:
            self.direction = RIGHT
        elif self.direction == RIGHT:
            self.direction = LEFT

        self.speed_x = -self.speed_x

