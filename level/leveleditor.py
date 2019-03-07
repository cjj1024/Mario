import json
import tkinter

from sprite.coin import *
from gui.gui import *
from gui.widget import *
from gui.button import *
from gui.inputbox import *
from gui.label import *
from gui.menuitem import *
from gui.menu import *
from gui.menubar import *


# 分为游戏编辑区域和物品选择区域
# 游戏编辑区域划分为40x40px的方格, 与一个二维数组对应
# 点击物品选择区域的物品即可选择该物品
# 在游戏编辑区域点击鼠标左键为放置物品
# 在游戏编辑区域点击鼠标右键为取消放置
# 进入游戏编辑器之前要设置游戏场景的长度, 大小要是40px的整数倍
# 退出游戏编辑器时要输入关卡名称
class MapEditor():
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 600))
        self.row = 0
        self.column = 0
        self.image = brick_img[0]
        self.imageId = 1000

        self.init_gui()

        self.start_x = 0
        self.length = 0
        self.get_length()

        self.map = []
        for i in range(30):
            self.map.append([0] * int(self.length / 20))

        # 标记用户是否编辑完成
        self.completed = False

        self.filename = ""


    def init_gui(self):
        self.gui = GUI()

        menubar = MenuBar()

        file_menu = Menu(text='文件')
        save_menuitem = MenuItem(text='保存')
        save_menuitem.bind_active(self.save_level_data, save_menuitem)
        file_menu.add_menuitem(save_menuitem)
        load_menuitem = MenuItem(text='导入')
        file_menu.add_menuitem(load_menuitem)

        system_menu = Menu(text="系统")
        return_menu_menuitem = MenuItem(text='返回菜单')
        return_menu_menuitem.bind_active(self.enter_gamemenu_sceen)
        system_menu.add_menuitem(return_menu_menuitem)
        exit_menuitem = MenuItem(text="退出")
        exit_menuitem.bind_active(
            lambda: sys.exit(0))
        system_menu.add_menuitem(exit_menuitem)

        menubar.add_menu(file_menu)
        menubar.add_menu(system_menu)

        self.gui.add_menubar(menubar, pos=(0, 0))


    def save_level_data(self, menuitem):
        menuitem.status = HOVER
        self.store()


    def enter_gamemenu_sceen(self):
        self.next_scene = GAME_MENU_SCENE


    def show(self):
        while not self.completed:
            self.check_event()

            self.draw_background()

            self.gui.update(self.screen)
            pygame.display.update()


    def check_event(self):
        for event in pygame.event.get():
            self.gui.process_event(event)
            if event.type == pygame.QUIT:
                self.store()
                self.completed = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.store()
                    self.completed = True
                elif event.key == pygame.K_LEFT:
                    if self.start_x >= 40:
                        self.start_x -= 40
                elif event.key == pygame.K_RIGHT:
                    if self.start_x + 800<= self.length - 40:
                        self.start_x += 40
            # 鼠标移动, 跟踪鼠标位置
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                self.row, self.column = self.get_grid(x, y)
            elif event.type == pygame.MOUSEBUTTONDOWN:
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
                        self.image = mushroom_img[2]
                        self.imageId = 2201
                    elif x > 1080 and x < 1120 and y > 0 and y < 40:
                        self.image = mushroom_img[4]
                        self.imageId = 2202
                    elif x > 1120 and x < 1160 and y > 0 and y < 40:
                        self.image = goomba_img[0]
                        self.imageId = 4000
                    elif x > 840 and x < 920 and y > 40 and y < 80:
                        self.image = brushwood_img[0]
                        self.imageId = 100
                    elif x > 920 and x < 1000 and y > 40 and y < 100:
                        self.image = cloud_img[0]
                        self.imageId = 200
                    elif x > 1000 and x < 1120 and y > 40 and y < 80:
                        self.image = cloud_img[1]
                        self.imageId = 201
                    elif x > 1120 and x < 1160 and y > 40 and y < 100:
                        self.image = piranha_img[0]
                        self.imageId = 4200
                    elif x > 1160 and x < 1200 and y > 40 and y < 100:
                        self.image = koopa_left_img[0]
                        self.imageId = 4100
                    elif x > 840 and x < 960 and y > 120 and y < 200:
                        self.image = brushwood_img[1]
                        self.imageId = 101
                    elif x > 960 and x < 1040 and y > 120 and y < 200:
                        self.image = pipe_img[0]
                        self.imageId = 1200
                    elif x > 840 and x < 880 and y > 200 and y < 240:
                        self.image = castle_brick_img[0]
                        self.imageId = 300
                    elif x > 880 and x < 920 and y > 200 and y < 240:
                        self.image = castle_brick_img[1]
                        self.imageId = 301
                    elif x > 920 and x < 960 and y > 200 and y < 240:
                        self.image = castle_brick_img[2]
                        self.imageId = 302
                    elif x > 960 and x < 1000 and y > 200 and y < 240:
                        self.image = castle_brick_img[3]
                        self.imageId = 303
                    elif x > 1000 and x < 1040 and y > 200 and y < 240:
                        self.image = castle_brick_img[4]
                        self.imageId = 304
                    elif x > 1040 and x < 1080 and y > 200 and y < 240:
                        self.image = castle_brick_img[5]
                        self.imageId = 305
                    elif x > 1080 and x < 1120 and y > 200 and y < 240:
                        self.image = castle_brick_img[6]
                        self.imageId = 306
                    elif x > 1120 and x < 1160 and y > 200 and y < 240:
                        self.image = castle_brick_img[7]
                        self.imageId = 307
                    else:
                        if x > 0 and x < 800 and y > 0 and y < 600:
                            self.row, self.column = self.get_grid(x, y)
                            self.map[self.row][self.column] = self.imageId
                # 鼠标右键
                elif event.button == 3:
                    x, y = event.pos
                    self.row, self.column = self.get_grid(x, y)
                    self.map[self.row][self.column] = 0
    


    # 物品选择区的物品
    def show_item(self):
        self.screen.fill(WHITE, (800, 0, 40, 600))
        self.screen.blit(brick_img[0], (840, 0))
        self.screen.blit(brick_img[1], (880, 0))
        self.screen.blit(brick_img[2], (920, 0))
        self.screen.blit(coin_img[0], (960, 0))
        self.screen.blit(mushroom_img[0], (1000, 0))
        self.screen.blit(mushroom_img[2], (1040, 0))
        self.screen.blit(mushroom_img[4], (1080, 0))
        self.screen.blit(goomba_img[0], (1120, 0))
        self.screen.blit(brushwood_img[0], (840, 40))
        self.screen.blit(cloud_img[0], (920, 40))
        self.screen.blit(cloud_img[1], (1000, 40))
        self.screen.blit(piranha_img[0], (1120, 40))
        self.screen.blit(koopa_left_img[0], (1160, 40))
        self.screen.blit(brushwood_img[1], (840, 120))
        self.screen.blit(pipe_img[0], (960, 120))
        self.screen.blit(castle_brick_img[0], (840, 200))
        self.screen.blit(castle_brick_img[1], (880, 200))
        self.screen.blit(castle_brick_img[2], (920, 200))
        self.screen.blit(castle_brick_img[3], (960, 200))
        self.screen.blit(castle_brick_img[4], (1000, 200))
        self.screen.blit(castle_brick_img[5], (1040, 200))
        self.screen.blit(castle_brick_img[6], (1080, 200))
        self.screen.blit(castle_brick_img[7], (1120, 200))


    def draw_background(self):
        self.screen.fill(SKYBLUE, (0, 0, 1200, 600))
        self.show_item()
        # 画40x40的方格
        for i in range(15):
            pygame.draw.line(self.screen, RED, (0, i * 40), (800, i * 40))
        for i in range(21):
            pygame.draw.line(self.screen, RED, (i * 40, 0), (i * 40, 600))

        # 用户当前选择的物品, 随鼠标的位置移动
        self.screen.blit(self.image, (self.column * 20 - self.start_x, self.row * 20))

        # 在游戏编辑区画出用户已放置的物品
        x = self.start_x
        end = self.start_x + 800
        while x < end:
            j = int(x / 20)
            for i in range(30):
                if self.map[i][j] == 1000:
                    self.screen.blit(brick_img[0], self.get_world_pos(i, j))
                elif self.map[i][j] == 1001:
                    self.screen.blit(brick_img[1], self.get_world_pos(i, j))
                elif self.map[i][j] == 1002:
                    self.screen.blit(brick_img[2], self.get_world_pos(i, j))
                elif self.map[i][j] == 100:
                    self.screen.blit(brushwood_img[0], self.get_world_pos(i, j))
                elif self.map[i][j] == 101:
                    self.screen.blit(brushwood_img[1], self.get_world_pos(i, j))
                elif self.map[i][j] == 200:
                    self.screen.blit(cloud_img[0], self.get_world_pos(i, j))
                elif self.map[i][j] == 201:
                    self.screen.blit(cloud_img[1], self.get_world_pos(i, j))
                elif self.map[i][j] == 1200:
                    self.screen.blit(pipe_img[0], self.get_world_pos(i, j))
                elif self.map[i][j] == 2100:
                    self.screen.blit(bonus_brick_img[1], self.get_world_pos(i, j))
                elif self.map[i][j] == 2200:
                    self.screen.blit(bonus_brick_img[1], self.get_world_pos(i, j))
                elif self.map[i][j] == 2201:
                    self.screen.blit(bonus_brick_img[1], self.get_world_pos(i, j))
                elif self.map[i][j] == 2202:
                    self.screen.blit(bonus_brick_img[1], self.get_world_pos(i, j))
                elif self.map[i][j] == 4000:
                    self.screen.blit(goomba_img[0], self.get_world_pos(i, j))
                elif self.map[i][j] == 4100:
                    self.screen.blit(koopa_left_img[0], self.get_world_pos(i, j))
                elif self.map[i][j] == 4200:
                    self.screen.blit(piranha_img[0], self.get_world_pos(i, j))
                elif self.map[i][j] == 300:
                    self.screen.blit(castle_brick_img[0], self.get_world_pos(i, j))
                elif self.map[i][j] == 301:
                    self.screen.blit(castle_brick_img[1], self.get_world_pos(i, j))
                elif self.map[i][j] == 302:
                    self.screen.blit(castle_brick_img[2], self.get_world_pos(i, j))
                elif self.map[i][j] == 303:
                    self.screen.blit(castle_brick_img[3], self.get_world_pos(i, j))
                elif self.map[i][j] == 304:
                    self.screen.blit(castle_brick_img[4], self.get_world_pos(i, j))
                elif self.map[i][j] == 305:
                    self.screen.blit(castle_brick_img[5], self.get_world_pos(i, j))
                elif self.map[i][j] == 306:
                    self.screen.blit(castle_brick_img[6], self.get_world_pos(i, j))
                elif self.map[i][j] == 307:
                    self.screen.blit(castle_brick_img[7], self.get_world_pos(i, j))

            x += 20



    def get_grid(self, x, y):
        x += self.start_x

        return int(y / 20), int(x / 20)


    def get_pos(self, i, j):
        return (j * 20, i * 20)

    def get_world_pos(self, i, j):
        return (j * 20 - self.start_x, i * 20)


    # 获得用户输入的场景的长度
    def get_length(self):
        label = Label(size=(300, 50), text="输入场景长度(40的整数倍):", text_size=48, text_pos=LEFT)
        inputbox = InputBox(text='800')
        button = Button(text="确定", normal_color=GREY, hover_color=YELLOW, active_color=RED)
        button.bind_active(self.save_length, inputbox)
        widget = Widget()
        widget.add_label(label, pos=(10, 50))
        widget.add_inputbox(inputbox, pos=(10, 100))
        widget.add_button(button, pos=(10, 150))
        self.gui.add_widget(widget, pos=(100, 100))


        while button.status != ACTIVE:
            self.screen.fill(BLACK, (0, 0, 1600, 800))
            for event in pygame.event.get():
                self.gui.process_event(event)
            self.gui.update(self.screen)
            pygame.display.update()

        widget.destroy()



    def save_length(self, inputbox):
        self.length = int(inputbox.get_text())


    # 用json格式保存关卡信息
    def store(self):
        label = Label(size=(300, 50), text='输入关卡名称(如level2)', text_size=48, text_pos=LEFT)
        inputbox = InputBox(text='default')
        button = Button(text='确定', normal_color=GREY, hover_color=YELLOW, active_color=RED)
        button.bind_active(self.save_filename, inputbox)
        widget = Widget()
        widget.add_label(label, pos=(10, 50))
        widget.add_inputbox(inputbox, pos=(10, 100))
        widget.add_button(button, pos=(10, 150))
        self.gui.add_widget(widget, pos=(100, 100))

        while button.status != ACTIVE:
            self.screen.fill(BLACK, (0, 0, 1600, 800))
            for event in pygame.event.get():
                self.gui.process_event(event)
            self.gui.update(self.screen)
            pygame.display.update()

        widget.destroy()


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
        data['piranha'] = []
        data['koopa'] = []
        data['castle_brick0'] = []
        data['castle_brick1'] = []
        data['castle_brick2'] = []
        data['castle_brick3'] = []
        data['castle_brick4'] = []
        data['castle_brick5'] = []
        data['castle_brick6'] = []
        data['castle_brick7'] = []

        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 1000:
                    data['brick1'].append(self.get_pos(i, j))
                elif self.map[i][j] == 1001:
                    data['brick2'].append(self.get_pos(i, j))
                elif self.map[i][j] == 1002:
                    data['brick3'].append(self.get_pos(i, j))
                elif self.map[i][j] == 1200:
                    data['pipe'].append(self.get_pos(i, j))
                elif self.map[i][j] == 100:
                    data['brushwood1'].append(self.get_pos(i, j))
                elif self.map[i][j] == 101:
                    data['brushwood2'].append(self.get_pos(i, j))
                elif self.map[i][j] == 200:
                    data['cloud1'].append(self.get_pos(i, j))
                elif self.map[i][j] == 201:
                    data['cloud2'].append(self.get_pos(i, j))
                elif self.map[i][j] == 2100:
                    data['coin'].append(self.get_pos(i, j))
                elif self.map[i][j] == 2200:
                    data['mushroom_grow'].append(self.get_pos(i, j))
                elif self.map[i][j] == 2201:
                    data['mushroom_life'].append(self.get_pos(i, j))
                elif self.map[i][j] == 2202:
                    data['mushroom_death'].append(self.get_pos(i, j))
                elif self.map[i][j] == 4000:
                    data['goomba'].append(self.get_pos(i, j))
                elif self.map[i][j] == 4100:
                    data['koopa'].append(self.get_pos(i, j))
                elif self.map[i][j] == 4200:
                    data['piranha'].append(self.get_pos(i, j))
                elif self.map[i][j] == 300:
                    data['castle_brick0'].append(self.get_pos(i, j))
                elif self.map[i][j] == 301:
                    data['castle_brick1'].append(self.get_pos(i, j))
                elif self.map[i][j] == 302:
                    data['castle_brick2'].append(self.get_pos(i, j))
                elif self.map[i][j] == 303:
                    data['castle_brick3'].append(self.get_pos(i, j))
                elif self.map[i][j] == 304:
                    data['castle_brick4'].append(self.get_pos(i, j))
                elif self.map[i][j] == 305:
                    data['castle_brick5'].append(self.get_pos(i, j))
                elif self.map[i][j] == 306:
                    data['castle_brick5'].append(self.get_pos(i, j))
                elif self.map[i][j] == 307:
                    data['castle_brick6'].append(self.get_pos(i, j))



        with open('./level/'+self.filename+'.json', 'w') as fp:
            fp.write(json.dumps(data, indent=4))


    def save_filename(self, inputbox):
        self.filename = inputbox.get_text()
