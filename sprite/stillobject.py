import pygame


# 静止物体
class StillObject(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.type = type
        self.init_image()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.start_x = x


    def init_image(self):
        pass


    # offset为世界坐标与屏幕坐标在x轴上的偏移
    def update(self, offset):
        self.rect.x = self.start_x - offset