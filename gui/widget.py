import pygame
import sys

from . constant import *
from . gui import *
from . button import *


class Widget(GUI, pygame.sprite.Sprite):
    def __init__(self, size=INIT_WIDGET_SIZE, color=INIT_WIDGET_COLOR):
        pygame.sprite.Sprite.__init__(self)
        GUI.__init__(self)

        self.size = size
        self.color = color
        self.offset = (0, TITLE_BAR_HEIGHT)

        self.background = pygame.Surface(self.size)
        self.background.fill(self.color)
        pygame.draw.line(self.background, GREY, (0, 30), (size[1], 30))

        self.image = self.background.copy()
        self.rect = self.image.get_rect()

        # 标记窗口是否可拖拽
        self.enable_drag = False

        self.screen = pygame.display.get_surface()

        self.init_widget()


    def init_widget(self):
        exit_button = Button(text='X', size=(30, 30), normal_color=INIT_WIDGET_COLOR, hover_color=RED,
                             active_color=RED)
        exit_button.bind_active(self.destroy)
        self.add_button(exit_button, pos=(self.rect.width - 30, 0))


    def destroy(self):
        for button in self.button_group:
            button.kill()
        for menubar in self.menubar_group:
            menubar.kill()
        for inputbox in self.inputbox_group:
            inputbox.kill()
        for widget in self.widget_group:
            widget.kill()

        self.kill()


    def update(self, screen):
        self.screen.blit(self.image, self.rect)
        super().update(screen)


    def process_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.is_in_object_area(x, y):
                self.enable_drag = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.enable_drag = False
        elif event.type == pygame.MOUSEMOTION:
            if self.enable_drag:
                self.drag(event.rel)

        for button in self.button_group:
            button.process_event(event)
        for menubar in self.menubar_group:
            menubar.process_event(event)
        for inputbox in self.inputbox_group:
            inputbox.process_event(event)
        for widget in self.widget_group:
            widget.process_event(event)


    # 判断x, y是否在控件区域内
    def is_in_object_area(self, x, y):
        if x > self.rect.left and x < self.rect.right \
            and y > self.rect.top and y < self.rect.bottom:
            return True
        else:
            return False


    # rel为相对位移
    def drag(self, rel):
        self.rect.x += rel[0]
        self.rect.y += rel[1]

        for button in self.button_group:
            button.rect.x += rel[0]
            button.rect.y += rel[1]
        for menubar in self.menubar_group:
            menubar.drag(rel)
        for inputbox in self.inputbox_group:
            inputbox.rect.x += rel[0]
            inputbox.rect.y += rel[1]
        for widget in self.widget_group:
            widget.rect.x += rel[0]
            widget.rect.y += rel[1]
        for label in self.label_group:
            label.rect.x += rel[0]
            label.rect.y += rel[1]


    def check_event(self):
        pass


    def adjust_pos(self, x, y):
        self.rect.x += x
        self.rect.y += y

        for button in self.button_group:
            button.adjust_pos(x, y)
        for label in self.label_group:
            label.adjust_pos(x, y)
        for inputbox in self.inputbox_group:
            inputbox.adjust_pos(x, y)
        for menubar in self.menubar_group:
            menubar.adjust_pos(x, y)
