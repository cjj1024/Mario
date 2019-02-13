from .stillobject import *
from tool.init import *


# 100 小灌木
# 101 大灌木
class Brushwood(StillObject):
    def __init__(self, type, x, y):
        StillObject.__init__(self, type, x, y)


    def init_image(self):
        if self.type == 100:
            self.image = brushwood_img[0]
        elif self.type == 101:
            self.image = brushwood_img[1]
        else:
            self.image = brushwood_img[0]