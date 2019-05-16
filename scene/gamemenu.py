
from scene.gamescene import *
from level.leveleditor import *
from tool.character import *
from . scene import *
from gui.gui import *
from gui.button import *


@Singleton
class GameMenu(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.self_scene = GAME_MENU_SCENE

        # 记录用户的选择
        # 1 开始游戏
        # 2 编辑地图
        # 3 退出游戏
        self.selected = 0

        self.num = 3

        pygame.mixer.music.load(music['main_theme'])
        pygame.mixer.music.play(loops=100)
        pygame.mixer.music.set_volume(0.1)

        self.init_gui()


    def init_gui(self):
        self.gui = GUI()
        TextObject.font = pygame.font.Font('./res/font/minicanton.ttf', 60)
        start_game_button = Button(text='开始游戏', size=(200, 50),
                                   normal_color=SKYBLUE, hover_color=DEEPSKYBLUE1, active_color=DEEPSKYBLUE2,
                                   text_color=WHITE, text_size=48, text_pos=CENTER)
        start_game_button.bind_hover(self.set_selected, 0)
        start_game_button.bind_active(self.enter_next_scene)
        edit_level_button = Button(text='编辑游戏', size=(200, 50),
                                   normal_color=SKYBLUE, hover_color=DEEPSKYBLUE1, active_color=DEEPSKYBLUE2,
                                   text_color=WHITE, text_size=48, text_pos=CENTER)
        edit_level_button.bind_hover(self.set_selected, 1)
        edit_level_button.bind_active(self.enter_next_scene)
        exit_game_button = Button(text='退出游戏', size=(200, 50),
                                   normal_color=SKYBLUE, hover_color=DEEPSKYBLUE1, active_color=DEEPSKYBLUE2,
                                   text_color=WHITE, text_size=48, text_pos=CENTER)
        exit_game_button.bind_hover(self.set_selected, 2)
        exit_game_button.bind_active(self.enter_next_scene)
        self.gui.add_button(start_game_button, pos=(350, 200))
        self.gui.add_button(edit_level_button, pos=(350, 250))
        self.gui.add_button(exit_game_button, pos=(350, 300))


    def set_selected(self, x):
        self.selected = x


    def show(self):
        self.draw_background()

        self.gui.update(self.screen)
        pygame.display.update()


    def process_event(self, event):
        self.gui.process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected += 1
                self.selected %= self.num
            elif event.key == pygame.K_UP:
                self.selected -= 1
                self.selected %= self.num
            elif event.key == pygame.K_RETURN:
                self.enter_next_scene()


    def enter_next_scene(self):
        if self.selected == 0:
            # self.next_scene = SELECT_LEVEL_SCENE
            self.next_scene = SELECT_DIFFICULTY_SCENE
        elif self.selected == 1:
            mapeditor = MapEditor()
            mapeditor.show()
            self.screen = pygame.display.set_mode((800, 600))
        elif self.selected == 2:
            sys.exit(0)


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

        # write_chars(self.screen, '开始游戏', 48, WHITE, (350, 200))
        # write_chars(self.screen, '编辑游戏', 48, WHITE, (350, 250))
        # write_chars(self.screen, '退出游戏', 48, WHITE, (350, 300))

        self.screen.blit(mushroom_img[0], (300, 200 + self.selected * 50))


