import pygame
from pygame.locals import *
import json
import tkinter
import sys, os

from src.tool.init import *
from src.sprite.mushroom import *
from src.sprite.coin import *


class MapEditor():
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 600))
        self.row = 0
        self.column = 0
        self.image = brick_img[0]
        self.imageId = 1000

        self.start_x = 0
        self.length = 0
        self.get_length()

        self.map = []
        for i in range(15):
            self.map.append([0] * int(self.length / 40))

        self.completed = False

        self.filename = ""


    def show(self):
        while not self.completed:
            self.check_event()

            self.draw_background()

            pygame.display.update()


    def check_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.store()
                self.completed = True
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
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                self.row, self.column = self.get_grid(x, y)
            elif event.type == MOUSEBUTTONDOWN:
                # 鼠标左键
                if event.button == 1:
                    x, y = event.pos
                    if x > 840 and x < 880 and y > 0 and y < 40:
                        self.image = brick_img[0]
                        self.imageId = 1000
                    elif x > 880 and x < 920 and y > 0 and y < 40:
                        self.image = brick_img[1]
                        self.imageId = 1001
                    elif x > 920 and x < 960 and y > 0 and y < 40:
                        self.image = brick_img[2]
                        self.imageId = 1002
                    elif x > 960 and x < 1000 and y > 0 and y < 40:
                        self.image = coin_img[0]
                        self.imageId = 2100
                    elif x > 1000 and x < 1040 and y > 0 and y < 40:
                        self.image = mushroom_img[0]
                        self.imageId = 2200
                    elif x > 1040 and x < 1080 and y > 0 and y < 40:
                        self.image = mushroom_img[1]
                        self.imageId = 2201
                    elif x > 1080 and x < 1140 and y > 0 and y < 40:
                        self.image = mushroom_img[2]
                        self.imageId = 2202
                    elif x > 840 and x < 920 and y > 40 and y < 80:
                        self.image = brushwood_img[0]
                        self.imageId = 100
                    elif x > 920 and x < 1000 and y > 40 and y < 100:
                        self.image = cloud_img[0]
                        self.imageId = 200
                    elif x > 1000 and x < 1200 and y > 40 and y < 80:
                        self.image = cloud_img[1]
                        self.imageId = 201
                    elif x > 840 and x < 960 and y > 120 and y < 200:
                        self.image = brushwood_img[1]
                        self.imageId = 101
                    elif x > 960 and x < 1040 and y > 120 and y < 200:
                        self.image = pipe_img[0]
                        self.imageId = 1200
                    elif x > 840 and x < 880 and y > 200 and y < 240:
                        self.image = goomba_img[0]
                        self.imageId = 4000
                    else:
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
        self.screen.fill(SKYBLUE, (0, 0, 1200, 600))
        self.show_item()
        for i in range(15):
            pygame.draw.line(self.screen, RED, (0, i * 40), (800, i * 40))
        for i in range(21):
            pygame.draw.line(self.screen, RED, (i * 40, 0), (i * 40, 600))

        self.screen.blit(self.image, (self.column * 40 - self.start_x, self.row * 40))

        x = self.start_x
        end = self.start_x + 800
        while x < end:
            j = int(x / 40)
            for i in range(15):
                if self.map[i][j] == 1000:
                    self.screen.blit(brick_img[0], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 1001:
                    self.screen.blit(brick_img[1], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 1002:
                    self.screen.blit(brick_img[2], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 100:
                    self.screen.blit(brushwood_img[0], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 101:
                    self.screen.blit(brushwood_img[1], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 200:
                    self.screen.blit(cloud_img[0], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 201:
                    self.screen.blit(cloud_img[1], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 1200:
                    self.screen.blit(pipe_img[0], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 2100:
                    self.screen.blit(bonus_brick_img[1], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 2200:
                    self.screen.blit(bonus_brick_img[1], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 2201:
                    self.screen.blit(bonus_brick_img[1], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 2202:
                    self.screen.blit(bonus_brick_img[1], (j * 40 - self.start_x, i * 40))
                elif self.map[i][j] == 4000:
                    self.screen.blit(goomba_img[0], (j * 40 - self.start_x, i * 40))


            x += 40


    def show_item(self):
        self.screen.fill(WHITE, (800, 0, 40, 600))
        self.screen.blit(brick_img[0], (840, 0))
        self.screen.blit(brick_img[1], (880, 0))
        self.screen.blit(brick_img[2], (920, 0))
        self.screen.blit(coin_img[0], (960, 0))
        self.screen.blit(mushroom_img[0], (1000, 0))
        self.screen.blit(mushroom_img[2], (1040, 0))
        self.screen.blit(mushroom_img[4], (1080, 0))
        self.screen.blit(brushwood_img[0], (840, 40))
        self.screen.blit(cloud_img[0], (920, 40))
        self.screen.blit(cloud_img[1], (1000, 40))
        self.screen.blit(brushwood_img[1], (840, 120))
        self.screen.blit(pipe_img[0], (960, 120))
        self.screen.blit(goomba_img[0], (840, 200))


    def get_length(self):
        win = tkinter.Tk()
        tkinter.Label(win, text='请输入长度(单位为px, 要求为40的整数倍): ').pack()
        text = tkinter.StringVar()
        text.set("1600")
        b = tkinter.Entry(win, textvariable=text)
        tkinter.Button(win, text='确定', command=lambda :self.save_length(text)).pack(side=tkinter.RIGHT)
        b.pack(side=tkinter.TOP)
        b.focus()
        win.mainloop()


    def save_length(self, text):
        self.length = int(str(text.get()))


    def save_filename(self, text):
        self.filename = str(text.get())


    def store(self):
        win = tkinter.Tk()
        frame = tkinter.Frame()
        tkinter.Label(frame, text="输入关卡名: ").pack(side=tkinter.LEFT)
        filename = tkinter.StringVar()
        filename.set('default')
        tkinter.Entry(frame, textvariable=filename).pack(side=tkinter.RIGHT)
        frame.pack(side=tkinter.TOP)
        tkinter.Button(win, text='确认', command=lambda :self.save_filename(filename)).pack(side=tkinter.BOTTOM)
        tkinter.mainloop()


        data = {}
        data["id"] = 2
        data['length']  = self.length
        data['brick1'] = []
        data['brick2'] = []
        data['brick3'] = []
        data['cloud1'] = []
        data['cloud2'] = []
        data['brushwood1'] = []
        data['brushwood2'] = []
        data['coin'] = []
        data['mushroom_grow'] = []
        data['mushroom_life'] = []
        data['mushroom_death'] = []
        data['pipe'] = []
        data['goomba'] = []


        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 1000:
                    data['brick1'].append([j * 40, i * 40])
                elif self.map[i][j] == 1001:
                    data['brick2'].append([j * 40, i * 40])
                elif self.map[i][j] == 1002:
                    data['brick3'].append([j * 40, i * 40])
                elif self.map[i][j] == 1200:
                    data['pipe'].append([j * 40, i * 40])
                elif self.map[i][j] == 100:
                    data['brushwood1'].append([j * 40, i * 40])
                elif self.map[i][j] == 101:
                    data['brushwood2'].append([j * 40, i * 40])
                elif self.map[i][j] == 200:
                    data['cloud1'].append([j * 40, i * 40])
                elif self.map[i][j] == 201:
                    data['cloud2'].append([j * 40, i * 40])
                elif self.map[i][j] == 2100:
                    data['coin'].append([j * 40, i * 40])
                elif self.map[i][j] == 2200:
                    data['mushroom_grow'].append([j * 40, i * 40])
                elif self.map[i][j] == 2201:
                    data['mushroom_life'].append([j * 40, i * 40])
                elif self.map[i][j] == 2202:
                    data['mushroom_death'].append([j * 40, i * 40])
                elif self.map[i][j] == 4000:
                    data['goomba'].append([j * 40, i * 40])


        with open('./res/level/'+self.filename+'.json', 'w') as fp:
            fp.write(json.dumps(data, indent=4))


