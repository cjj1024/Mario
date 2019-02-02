import pygame
from pygame.locals import *
import json
import tkinter
import sys, os

from src.tool.init import *
from src.sprite.mushroom import *
from src.sprite.coin import *


class MapEditor():
    def __init__(self, screen):
        self.screen = screen
        self.row = 0
        self.column = 0
        self.image = brick_img[0]
        self.imageId = 1

        self.start_x = 0
        self.length = 0
        self.get_length()

        self.map = []
        for i in range(15):
            self.map.append([0] * int(self.length / 40))


    def show(self):
        while True:
            self.check_event()

            self.draw_background()

            pygame.display.update()


    def check_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    pass
                elif event.key == K_DOWN:
                    pass
                elif event.key == K_LEFT:
                    if self.start_x >= 40:
                        self.start_x -= 40
                elif event.key == K_RIGHT:
                    if self.start_x + 800<= self.length - 40:
                        self.start_x += 40
                elif event.key == K_g:
                    self.image = brick_img[0]
                    self.imageId = 1
                elif event.key == K_c:
                    self.image = coin_img[0]
                    self.imageId = 2
                elif event.key == K_b:
                    self.image = brick_img[1]
                    self.imageId = 11
                elif event.key == K_c:
                    self.image = coin_img[0]
                    self.imageId = 21
                elif event.key == K_m:
                    self.image = mushroom_img[0]
                    self.imageId = 22
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                self.row, self.column = self.get_grid(x, y)
            elif event.type == MOUSEBUTTONDOWN:
                # 鼠标左键
                if event.button == 1:
                    x, y = event.pos
                    self.row, self.column = self.get_grid(x, y)
                    self.map[self.row][self.column] = self.imageId
                # 鼠标右键
                elif event.button == 3:
                    x, y = event.pos
                    self.row, self.column = self.get_grid(x, y)
                    self.map[self.row][self.column] = 0

    def get_grid(self, x, y):
        x += self.start_x

        return int(y / 40), int(x / 40)


    def draw_background(self):
        self.screen.fill((100, 150, 250), (0, 0, 800, 600))
        for i in range(15):
            pygame.draw.line(self.screen, (255, 0, 0), (0, i * 40), (800, i * 40))
        for i in range(20):
            pygame.draw.line(self.screen, (255, 0, 0), (i * 40, 0), (i * 40, 600))

        self.screen.blit(self.image, (self.column * 40 - self.start_x, self.row * 40))

        x = self.start_x
        end = self.start_x + 800
        while x < end:
            j = int(x / 40)
            for i in range(15):
                if self.map[i][j] == 1:
                    self.screen.blit(brick_img[0], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 10:
                    self.screen.blit(brick_img[3], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 11:
                    self.screen.blit(brick_img[1], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 21:
                    self.screen.blit(bonus_brick_img[1], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 22:
                    self.screen.blit(bonus_brick_img[1], (j * 40 - self.start_x, i * 40))


            x += 40


    def get_length(self):
        win = tkinter.Tk()
        tkinter.Label(win, text='请输入长度(单位为px, 要求为40的整数倍): ').pack()
        text = tkinter.StringVar()
        text.set("1600")
        b = tkinter.Entry(win, textvariable=text)
        tkinter.Button(win, text='退出', command=win.destroy).pack(side=tkinter.RIGHT)
        tkinter.Button(win, text='确定', command=lambda: self._ok(text)).pack(side=tkinter.RIGHT)
        b.pack(side=tkinter.TOP)
        b.focus()
        win.mainloop()


    def _ok(self, text):
        self.length = int(str(text.get()))