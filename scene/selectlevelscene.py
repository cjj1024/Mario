import sys

from . scene import *
from tool.character import *
from tool.globaldata import *
from gui.constant import *
from gui.gui import *
from gui.button import *



@Singleton
class SelectLevelScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.level = 0

        self.row = 1
        self.column = 4
        self.num = 5

        self.init_gui()

    def set_level(self, level):
        self.level = level


    def enter_next_scene(self):
        self.next_scene = GAME_SCENE


    def init_gui(self):
        self.gui = GUI()
        level1_button = Button(id=1, text='第一关', size=(200, 50),
                               normal_color=SKYBLUE, hover_color=DEEPSKYBLUE1, active_color=DEEPSKYBLUE2,
                               text_color=WHITE, text_size=48, text_pos=CENTER)
        level1_button.bind_hover(self.set_level, 1)
        level1_button.bind_active(self.enter_next_scene)
        self.gui.add_button(level1_button, pos=(0, 0))
        level2_button = Button(id=2, text='第二关', size=(200, 50),
                               normal_color=SKYBLUE, hover_color=DEEPSKYBLUE1, active_color=DEEPSKYBLUE2,
                               text_color=WHITE, text_size=48, text_pos=CENTER)
        level2_button.bind_hover(self.set_level, 2)
        level2_button.bind_active(self.enter_next_scene)
        self.gui.add_button(level2_button, pos=(200, 0))
        level3_button = Button(id=3, text='第三关', size=(200, 50),
                               normal_color=SKYBLUE, hover_color=DEEPSKYBLUE1, active_color=DEEPSKYBLUE2,
                               text_color=WHITE, text_size=48, text_pos=CENTER)
        level3_button.bind_hover(self.set_level, 3)
        level3_button.bind_active(self.enter_next_scene)
        self.gui.add_button(level3_button, pos=(400, 0))
        level4_button = Button(id=4, text='第四关', size=(200, 50),
                               normal_color=SKYBLUE, hover_color=DEEPSKYBLUE1, active_color=DEEPSKYBLUE2,
                               text_color=WHITE, text_size=48, text_pos=CENTER)
        level4_button.bind_hover(self.set_level, 4)
        level4_button.bind_active(self.enter_next_scene)
        self.gui.add_button(level4_button, pos=(600, 0))
        level5_button = Button(id=5, text='第五关', size=(200, 50),
                               normal_color=SKYBLUE, hover_color=DEEPSKYBLUE1, active_color=DEEPSKYBLUE2,
                               text_color=WHITE, text_size=48, text_pos=CENTER)
        level5_button.bind_hover(self.set_level, 4)
        level5_button.bind_active(self.enter_next_scene)
        self.gui.add_button(level5_button, pos=(0, 100))


    def set_level(self, level):
        self.level = level


    def show(self):
        self.screen.fill(SKYBLUE, (0, 0, 800, 600))

        self.gui.update(self.screen)
        pygame.display.update()


    def process_event(self, event):
        self.gui.process_event(event)
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_DOWN:
        #         self.level = (self.level + self.column) % self.num
        #     elif event.key == pygame.K_UP:
        #         self.level = (self.level - self.column) % self.num
        #     elif event.key == pygame.K_LEFT:
        #         self.level = (self.level - 1) % self.num
        #     elif event.key == pygame.K_RIGHT:
        #         self.level = (self.level + 1) % self.num
        #     elif event.key == pygame.K_RETURN:
        #         self.next_scene = GAME_SCENE