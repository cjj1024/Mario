import pygame
from .constant import *


class TextObject():
    font = pygame.font.Font('./res/font/simkai.ttf', 60)
    def __init__(self, text, text_size, text_color):
        self.text = text
        self.text_size = text_size
        self.text_color = text_color


    def get_text_image_size(self, text, size):
        text_size = TextObject.font.size(text)
        text_size = list(text_size)
        text_size[0] = int(text_size[0] * size / text_size[1])
        text_size[1] = size

        return text_size


    def get_text_image(self, text, text_size, text_color):

        text_image = TextObject.font.render(text, True, text_color)
        text_image = pygame.transform.scale(
            text_image, (int(text_image.get_width() * text_size / text_image.get_height()), text_size))

        return text_image


    # 把背景图片与文字合并起来
    # fit为真时，比较文字所需大小与图片大小，取小的size
    def merge_text_image(self, text, text_size, text_color, image, fit=True, pos=CENTER):
        if not text:
            return

        if fit:
            # 如果文字大小超过控件大小， 则使用控件的size
            if image.get_width() / len(list(text)) > text_size:
                text_size = text_size
            else:
                text_size = int(image.get_width() / len(list(text)))

        text_image = self.get_text_image(text, text_size, text_color)


        # 使用copy(), 避免修改原图片
        res_img = image.copy()
        if pos == LEFT:
            offset_x = 0
            offset_y = int((res_img.get_height() - text_image.get_height()) / 2)
            res_img.blit(text_image, (0, offset_y))
        elif pos == CENTER:
            # 使文字在图片中央
            offset_x = int((res_img.get_width() - text_image.get_width()) / 2)
            offset_y = int((res_img.get_height() - text_image.get_height()) / 2)
            res_img.blit(text_image, (offset_x, offset_y))
        elif pos == RIGHT:
            offset_x = res_img.get_width() - text_image.get_width()
            offset_y = int((res_img.get_height() - text_image.get_height()) / 2)
        res_img.blit(text_image, (offset_x, offset_y))

        return res_img