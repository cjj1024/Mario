
from src.scene.gamescene import *
from src.tool.init import *

class GameMenu():
    def __init__(self, screen):
        self.screen = screen
        # 记录用户的选择
        # 1 为开始游戏
        # 2 为退出游戏
        self.selected = 1


    def show(self):
        self.screen.fill((100, 150, 250), (0, 0, 800, 600))
        for i in range(0, 800, 40):
            self.screen.blit(ground_img[0], (i, 520))
        for i in range(0, 800, 40):
            self.screen.blit(ground_img[0], (i, 560))
        self.screen.blit(cloud_img[0], (600, 100))
        self.screen.blit(brushwood[0], (0, 480))
        self.screen.blit(brushwood[0], (40, 480))
        self.screen.blit(brushwood[0], (200, 480))
        self.screen.blit(brushwood[0], (600, 480))


        write_word(screen, '开始游戏', 36, (255, 255, 255), (350, 250))
        write_word(screen, '退出游戏', 36, (255, 255, 255), (350, 300))
        self.screen.blit(bonus_img['life'], (300, 250))

        pygame.mixer.music.load(music['main_theme'])
        pygame.mixer.music.play()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(0)
                    elif event.key == K_DOWN:
                        if self.selected == 1:
                            screen.fill((100, 150, 250), (300, 250, 40, 40))
                            screen.blit(bonus_img['life'], (300, 300))
                            self.selected = 2
                    elif event.key == K_UP:
                        if self.selected == 2:
                            screen.fill((100, 150, 250), (300, 300, 40, 40))
                            screen.blit(bonus_img['life'], (300, 250))
                            self.selected = 1
                    elif event.key == K_RETURN:
                        if self.selected == 1:
                            gamescene = GameScene(self.screen)
                            gamescene.show()
                        elif self.selected == 2:
                            sys.exit(0)

            pygame.display.update()