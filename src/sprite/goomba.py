
from src.tool.init import *

class Goomba(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = goomba_img['walk_left']
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 520
        self.direction = LEFT
        self.speed = 5
        self.status = WALK


    def update(self):
        if self.status == WALK:
            self.walk()
        elif self.status == DEATH:
            self.death()


    def death(self):
        if self.rect.x < 0:
            self.kill()
        self.image = goomba_img['death']
        self.rect.x -= self.speed

    def walk(self):
        if self.rect.x > 0 and self.rect.x < 760:
            if self.direction == LEFT:
                self.rect.x -= self.speed
            elif self.direction == RIGHT:
                self.rect.x += self.speed
        else:
            if self.rect.x <= 10:
                self.image = goomba_img['walk_right']
                self.direction = RIGHT
                self.rect.x += self.speed
            elif self.rect.x >= 750:
                self.image = goomba_img['walk_left']
                self.direction = LEFT
                self.rect.x -= self.speed


    def set_status(self, status):
        if self.status != DEATH:
            self.status = status


    def get_status(self):
        return self.status