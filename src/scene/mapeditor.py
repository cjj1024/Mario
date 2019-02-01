import pygame
from pygame.locals import *
import json
import tkinter
import sys, os

from src.tool.init import *


class MapEditor():
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.image = brick_img[0]
        self.imageId = 1

        tk = tkinter.Tk()
        b = tkinter.Button(tk, text="Hello")
        b.pack()
        tk.mainloop()


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
                    if self.x > 0:
                        self.x -= 1
                elif event.key == K_DOWN:
                    if self.x < 14:
                        self.x += 1
                elif event.key == K_LEFT:
                    if self.y > 0:
                        self.y -= 1
                elif event.key == K_RIGHT:
                    if self.y < 19:
                        self.y += 1
            elif event.type == MOUSEBUTTONDOWN:
                # 鼠标左键
                if event.button == 1:
                    x, y = event.pos
                    self.x = int(y / 40)
                    self.y = int(x / 40)
                # 鼠标右键
                elif event.button == 3:
                    x, y = event.pos


    def draw_background(self):
        self.screen.fill((100, 150, 250), (0, 0, 800, 600))
        for i in range(15):
            pygame.draw.line(self.screen, (255, 0, 0), (0, i * 40), (800, i * 40))
        for i in range(20):
            pygame.draw.line(self.screen, (255, 0, 0), (i * 40, 0), (i * 40, 600))

        self.screen.blit(self.image, (self.y * 40, self.x * 40))