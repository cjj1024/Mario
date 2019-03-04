import pygame

from . constant import *


# 可点击控件
# 有三种状态
# normal 普通状态
# hover 鼠标悬浮在控件上方
# active 鼠标点击控件
# 当发生状态改变时会调用相应的状态改变函数和状态函数
class ClickableObject():
    def __init__(self, size):
        self.normal_function = None
        self.normal_function_args = None
        self.active_function = None
        self.active_function_args = None
        self.hover_function = None
        self.hover_function_args = None

        print(size)
        self.rect = pygame.Rect((0, 0), size)

        self.change_status = False


    def update(self, *args):
        # 没有状态变化则返回
        if not self.change_status:
            return

        if self.status == NORMAL:
            self.change_to_normal()
            self.normal()
        elif self.status == HOVER:
            self.change_to_hover()
            self.hover()
        elif self.status == ACTIVE:
            self.change_to_active()
            self.active()
        self.change_status = False


    # 处理事件
    # 当有鼠标移动事件时, 判断鼠标是否在控件区域内, 如果在, 则状态改为hover, 否则改为normal
    # 当有鼠标点击事件时, 判断鼠标是否在控件区域内, 如果在, 则状态改为active
    # 当有鼠标按键松开事件时, 判断鼠标是否在控件区域内, 如果在, 则状态改为hover, 否则改为normal
    def process_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if self.is_in_object_area(x, y):
                self.status = HOVER
                self.change_status = True
            else:
                self.status = NORMAL
                self.change_status = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if self.is_in_object_area(x, y):
                    self.status = ACTIVE
                    self.change_status = True
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if self.is_in_object_area(x, y):
                self.status = HOVER
                self.change_status = True
            else:
                self.status = NORMAL
                self.change_status = True


    # 判断x, y是否在控件区域内
    def is_in_object_area(self, x, y):
        if x > self.rect.left and x < self.rect.right \
            and y > self.rect.top and y < self.rect.bottom:
            return True
        else:
            return False


    # 状态转为普通状态
    def change_to_normal(self):
        pass


    # 普通状态
    def normal(self):
        if self.normal_function:
            self.normal_function(*self.normal_function_args)


    # 状态转为普通状态
    def change_to_hover(self):
        pass


    # 鼠标指针悬浮在控件上方
    def hover(self):
        if self.hover_function:
            self.hover_function(*self.hover_function_args)


    # 状态转为点击状态
    def change_to_active(self):
        pass


    # 点击状态
    def active(self):
        if self.active_function:
            self.active_function(*self.active_function_args)


    def bind_normal(self, func, *args):
        self.normal_function = func
        self.normal_function_args = args


    def bind_hover(self, func, *args):
        self.hover_function = func
        self.hover_function_args = args


    def bind_active(self, func, *args):
        self.active_function = func
        self.active_function_args = args


    def adjust_pos(self, x, y):
        self.rect.x += x
        self.rect.y += y