from .item import *


class Pipe(Item):
    def __init__(self, type, x, y):
        self.init_image()

        Item.__init__(self, type, x, y)


    def init_image(self):
        self.image = pipe_img[0]
