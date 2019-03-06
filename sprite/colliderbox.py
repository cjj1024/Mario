import pygame


class ColliderBox(pygame.sprite.Sprite):
    def __init__(self, size, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos