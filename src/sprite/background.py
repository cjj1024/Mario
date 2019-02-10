import pygame


# 背景
# 如云, 灌木之类无需检测碰撞的精灵
class Background(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.start_x = x


    def update(self, offset):
        self.rect.x = self.start_x - offset