
from src.tool.init import *
from src.tool.globaldata import *

class Goomba(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = goomba_img[1]
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 480
        self.direction = LEFT
        self.speed = 5
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

    # 向左走, 碰到障碍掉头
    # 向右走, 碰到障碍掉头
    # 走出屏幕边界则消失
    def walk(self):
        if self.rect.x < 0 or self.rect.x > 800:
            self.kill()

        i = int(self.rect.y / 40)
        if self.direction == LEFT:
            j = int((self.rect.x - self.speed) / 40)
            if self.rect.x - self.speed > 0 and level.map[i][j] != 0:
                self.direction = RIGHT
            else:
                self.rect.x -= self.speed
        else:
            j = int((self.rect.x + self.speed + self.rect.width) / 40)
            if self.rect.x + self.speed < 800 and level.map[i][j] != 0:
                self.direction = LEFT
            else:
                self.rect.x += self.speed

        # # 向左走
        # if self.direction == LEFT and self.rect.x > 0:
        #     self.rect.x -= self.speed
        # # 向右走
        # elif self.direction == RIGHT and self.rect.x < 760:
        #     self.rect.x += self.speed
        # # 掉头
        # else:
        #     if self.rect.x <= 10:
        #         self.image = self.walk_left_img
        #         self.direction = RIGHT
        #         self.rect.x += self.speed
        #     elif self.rect.x >= 750:
        #         self.image = self.walk_left_img
        #         self.direction = LEFT
        #         self.rect.x -= self.speed


    def set_status(self, status):
        if self.status != DEATH:
            self.status = status


    def get_status(self):
        return self.status


    def init_image(self):
        self.walk_left_img = goomba_img[0]
        self.walk_right_img = goomba_img[1]
        self.death_img = goomba_img[2]