from .textobject import *


class Label(TextObject, pygame.sprite.Sprite):
    def __init__(self, size=INIT_LABEL_SIZE,
                 text=INIT_LABEL_TEXT, text_size=INIT_LABEL_TEXT_SIZE, text_color=INIT_LABEL_TEXT_COLOR):
        pygame.sprite.Sprite.__init__(self)

        TextObject.__init__(self, text=text, text_size=text_size, text_color=text_color)

        self.image = pygame.Surface(size)
        self.image.fill(WHITE, self.image.get_rect())
        self.rect = self.image.get_rect()
        self.image = self.merge_text_image(self.text, self.text_size, self.text_color, self.image, pos=CENTER)


    def adjust_pos(self, x, y):
        self.rect.x += x
        self.rect.y += y


    def process_event(self, event):
        pass