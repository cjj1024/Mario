from . stillobject import *

from tool.init import *


# 200 小云
# 201 大云
class Cloud(StillObject):
    def __init__(self, type, x, y):
        StillObject.__init__(self, type, x, y)


    def init_image(self):
        if self.type == 200:
            self.image = cloud_img[0]
        elif self.type == 201:
            self.image = cloud_img[1]
        else:
            self.image = cloud_img[0]