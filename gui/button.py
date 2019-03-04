from . clickableobject import *
from . statechangeableobject import *
from . textobject import *
from . constant import *


class Button(ClickableObject, StateChangeableObject, TextObject, pygame.sprite.Sprite):
    def __init__(self, size=INIT_BUTTON_SIZE, text=INIT_BUTTON_TEXT,
                 text_size=INIT_BUTTON_TEXT_SIZE, text_color=INIT_BUTTON_TEXT_COLOR,
                 normal_color=INIT_BUTTON_NORMAL_COLOR, hover_color=INIT_BUTTON_HOVER_COLOR,
                 active_color=INIT_BUTTON_ACTIVE_COLOR,
                 normal_image=None, hover_image=None, active_image=None):
        pygame.sprite.Sprite.__init__(self)

        ClickableObject.__init__(self, size=size)

        StateChangeableObject.__init__(
            self, size=size,
            normal_color=normal_color, hover_color=hover_color, active_color=active_color,
            normal_image=normal_image, hover_image=hover_image, active_image=active_image)

        TextObject.__init__(self,text=text, text_size=text_size, text_color=text_color)

        self.init_button()

        self.rect = self.image.get_rect()


    # 如果有图片则用图片
    # 没有用纯色
    def init_button(self):
        self.image = self.normal_image.copy()
        self.rect = self.image.get_rect()

        self.set_image(self.normal_image)

        self.status = NORMAL


    def set_image(self, image):
        self.image = self.merge_text_image(self.text, self.text_size, self.text_color, image)


    # 状态转为普通状态
    def change_to_normal(self):
        self.set_image(self.normal_image)


    # 状态转为悬浮状态
    def change_to_hover(self):
        self.set_image(self.hover_image)


    # 状态转为点击状态
    def change_to_active(self):
        self.set_image(self.active_image)

