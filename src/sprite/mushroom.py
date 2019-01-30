
from src.tool.init import *
from src.tool.globaldata import *


class Mushroom(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = mushroom_img[2]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = RIGHT
        # 蘑菇的类型
        self.type = GROW_BIGGER


    def get_type(self):
        return self.type


    # 在屏幕里左右来回运动
    # 如果下方没有砖块， 则向下掉落
    def update(self):
        if self.direction == LEFT and self.rect.x > 0:
            self.rect.x -= 5
        elif self.direction == RIGHT and self.rect.x < 760:
            self.rect.x += 5
        elif self.rect.x <= 0:
            self.direction = RIGHT
        elif self.rect.x >= 760:
            self.direction = LEFT

        i = int(self.rect.y / 40) + 1
        j = int(self.rect.x / 40)
        if level.map[i][j] == 0:
            self.rect.y += 10

