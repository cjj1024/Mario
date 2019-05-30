
from gui.constant import *
from tool.init import *
from gui.gui import *
from gui.button import *

from . scene import *


# 选择游戏难度
class SelectDifficultyScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.self_scene = SELECT_DIFFICULTY_SCENE

        self.init_gui()

        self.globalData = GlobalData()



    def set_difficulty(self, probability):
        self.globalData.game_probability = probability


    def enter_next_scene(self):
        self.globalData.scene = SELECT_LEVEL_SCENE

    def enter_gamemenu_sceen(self):
        self.globalData.scene = GAME_MENU_SCENE


    def init_gui(self):
        self.gui = GUI()
        easy_button = Button(id=1, text='简单', size=(200, 50),
                             normal_color=SKYBLUE, hover_color=DEEPSKYBLUE1, active_color=DEEPSKYBLUE2,
                             text_color=WHITE, text_size=48, text_pos=CENTER)
        easy_button.bind_hover(self.set_difficulty, EASY)
        easy_button.bind_active(self.enter_next_scene)
        self.gui.add_button(easy_button, pos=(300, 200))

        normal_button = Button(id=1, text='普通', size=(200, 50),
                             normal_color=SKYBLUE, hover_color=DEEPSKYBLUE1, active_color=DEEPSKYBLUE2,
                             text_color=WHITE, text_size=48, text_pos=CENTER)
        normal_button.bind_hover(self.set_difficulty, NORMAL)
        normal_button.bind_active(self.enter_next_scene)
        self.gui.add_button(normal_button, pos=(300, 250))

        hard_button = Button(id=1, text='困难', size=(200, 50),
                             normal_color=SKYBLUE, hover_color=DEEPSKYBLUE1, active_color=DEEPSKYBLUE2,
                             text_color=WHITE, text_size=48, text_pos=CENTER)
        hard_button.bind_hover(self.set_difficulty, HARD)
        hard_button.bind_active(self.enter_next_scene)
        self.gui.add_button(hard_button, pos=(300, 300))

        return_menu_button = Button(text='返回菜单', text_color=WHITE, text_size=48,
                                    normal_color=SKYBLUE, hover_color=DEEPSKYBLUE1, active_color=DEEPSKYBLUE2)
        return_menu_button.bind_active(self.enter_gamemenu_sceen)
        self.gui.add_button(return_menu_button,
                            pos=(SCREEN_SIZE[0]-return_menu_button.rect.width - 5,
                                 SCREEN_SIZE[1]-return_menu_button.rect.height - 85))


    def show(self):
        self.screen.fill(SKYBLUE, (0, 0, 800, 600))
        self.draw_background()

        self.gui.update(self.screen)

        pygame.display.update()


    def process_event(self, event):
        self.gui.process_event(event)

    def draw_background(self):
        self.screen.fill(SKYBLUE, (0, 0, 800, 600))
        for i in range(0, 800, 40):
            self.screen.blit(brick_img[0], (i, 520))
        for i in range(0, 800, 40):
            self.screen.blit(brick_img[0], (i, 560))
        self.screen.blit(cloud_img[0], (600, 100))
        self.screen.blit(brushwood_img[0], (0, 480))
        self.screen.blit(brushwood_img[0], (40, 480))
        self.screen.blit(brushwood_img[0], (200, 480))
        self.screen.blit(brushwood_img[0], (600, 480))