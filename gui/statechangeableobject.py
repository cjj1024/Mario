import pygame


class StateChangeableObject():
    def __init__(self, size, normal_color, hover_color, active_color,
                 normal_image, hover_image, active_image):
        if normal_image:
            # 按钮正常图片, 悬浮图片, 点击图片
            self.normal_image = pygame.transform.scale(normal_image, size)
            self.hover_image = pygame.transform.scale(hover_image, size)
            self.active_image = pygame.transform.scale(active_image, size)
        else:
            self.normal_image = pygame.Surface(size)
            self.normal_image.fill(normal_color, self.normal_image.get_rect())
            self.hover_image = pygame.Surface(size)
            self.hover_image.fill(hover_color, self.hover_image.get_rect())
            self.active_image = pygame.Surface(size)
            self.active_image.fill(active_color, self.active_image.get_rect())