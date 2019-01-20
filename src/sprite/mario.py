from src.tool.init import *

class Mario(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = mario_small['stand_right']
        self.rect = self.image.get_rect()
        self.life = 3
        self.status = STAND
        self.direction = RIGHT
