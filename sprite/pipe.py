from . stillobject import *
from tool.init import *


class Pipe(StillObject):
    def __init__(self, type, x, y):
        StillObject.__init__(self, type, x, y)


    def init_image(self):
        self.image = pipe_img[0]
