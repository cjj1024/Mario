
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


    @property
    def X(self):
        return self.rect.x


    @X.setter
    def X(self, x):
        self.rect.x = x


    @property
    def Y(self):
        return self.rect.y


    @Y.setter
    def Y(self, y):
        self.rect.y = y


    def get_grid(self):
        i = int((self.Y + self.rect.height / 2) / 40)
        j = int((level.start + self.X + self.rect.width / 2) / 40)

        return i, j


    def update(self):
        if self.status == DEATH:
            self.death()
        elif self.status == WALK:
            self.walk()


    def death(self):
        if self.X < 0:
            self.kill()
        self.image = self.death_img
        self.X -= self.speed


    # 向左走, 碰到障碍掉头
    # 向右走, 碰到障碍掉头
    # 走出屏幕边界则消失
    def walk(self):
        i, j = self.get_grid()
        level.map[i][j] = 0
        if self.X < 0 or self.X > 800:
            self.kill()

        i = int(self.Y / 40)
        if self.direction == LEFT:
            j = int((self.X - self.speed) / 40)
            if self.X - self.speed > 0 and level.map[i][j] != 0:
                self.direction = RIGHT
            else:
                self.X -= self.speed
        else:
            j = int((self.X + self.speed + self.rect.width) / 40)
            if self.X + self.speed < 800 and level.map[i][j] != 0:
                self.direction = LEFT
            else:
                self.X += self.speed

        i, j = self.get_grid()
        level.map[i][j] = 31


    def set_status(self, status):
        if self.status != DEATH:
            self.status = status


    def get_status(self):
        return self.status


    def init_image(self):
        self.walk_left_img = goomba_img[0]
        self.walk_right_img = goomba_img[1]
        self.death_img = goomba_img[2]