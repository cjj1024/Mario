
from src.tool.init import *
from src.tool.globaldata import *

class Goomba(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = goomba_img[1]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = LEFT
        self.speed_x = -2
        self.speed_y = 0
        self.status = WALK

        self.init_image()


    def update(self):
        if self.status == DEATH:
            self.death()
        elif self.status == WALK:
            self.walk()


    def death(self):
        if self.rect.x < 0:
            self.kill()
        self.image = self.death_img
        self.rect.x -= self.speed


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
        self.walk_left_img = goomba_img[0]
        self.walk_right_img = goomba_img[1]
        self.death_img = goomba_img[2]