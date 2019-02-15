
from scene.gamescene import *
from level.leveleditor import *
from tool.character import *
from .scene import *


@Singleton
class GameMenu(Scene):
    def __init__(self):
        Scene.__init__(self)

        # 记录用户的选择
        # 1 开始游戏
        # 2 编辑地图
        # 3 退出游戏
        self.selected = 0

        self.num = 3

        pygame.mixer.music.load(music['main_theme'])
        pygame.mixer.music.play()


    def show(self):
        self.next_scene = NOW_SCENE

        self.draw_background()

        self.check_event()

        pygame.display.update()


    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.key == pygame.K_DOWN:
                    self.selected += 1
                    self.selected %= self.num
                elif event.key == pygame.K_UP:
                    self.selected -= 1
                    self.selected %= self.num
                elif event.key == pygame.K_RETURN:
                    if self.selected == 0:
                        # gamescene = GameScene()
                        # gamescene.show()
                        self.next_scene = GAME_SCENE
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

        write_chars(self.screen, '开始游戏', 48, WHITE, (350, 200))
        write_chars(self.screen, '编辑游戏', 48, WHITE, (350, 250))
        write_chars(self.screen, '退出游戏', 48, WHITE, (350, 300))

        self.screen.blit(mushroom_img[0], (300, 200 + self.selected * 50))


