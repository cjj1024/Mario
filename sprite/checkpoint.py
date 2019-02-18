from .stillobject import *
from tool.globaldata import *


class Checkpoint(StillObject):
    def __init__(self, type, x, y):
        StillObject.__init__(self, type, x, y)


    def init_image(self):
        self.image = pygame.Surface((10, 600))
        # self.image.set_alpha(0)


