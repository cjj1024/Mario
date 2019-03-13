import pygame

from . constant import *


class Slider(pygame.sprite.Sprite):
    def __init__(self, value=INIT_SLIDER_VALUE, size=INIT_SLIDER_SIZE,
                color=INIT_SLIDER_COLOR):
        pygame.sprite.Sprite.__init__(self)

        self.value = value
        self.color = color

        self.background_image = pygame.Surface(size)
        self.background_image.fill(GREY, self.background_image.get_rect())
        self.rect = self.background_image.get_rect()


    def update(self, *args):
        self.image = self.background_image.copy()
        y = int(self.rect.height / 2)
        # self.image.fill(self.color, (self.rect.x, y, self.rect.x + int(self.rect.width * self.value), 20))
        pygame.draw.line(self.image, self.color, (0, y), (int(self.rect.width * self.value), y), 10)


    def adjust_pos(self, x, y):
        self.rect.x += x
        self.rect.y += y


    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.is_in_object_area(x, y):
                self.value = (x - self.rect.x) / self.rect.width



    # 判断x, y是否在控件区域内
    def is_in_object_area(self, x, y):
        if x > self.rect.left and x < self.rect.right \
            and y > self.rect.top and y < self.rect.bottom:
            return True
        else:
            return False