from src.scene.gamescene import *

class GameMenu():
    def __init__(self, screen):
        self.screen = screen
        self.status = 1



    def show(self):
        self.screen.fill((100, 150, 250), (0, 0, 800, 600))
        for i in range(0, 800, 40):
            self.screen.blit(ground['brick'], (i, 560))
        self.screen.blit(background['bush1'], (0, 435))
        self.screen.blit(background['bush3'], (300, 515))
        self.screen.blit(background['bush2'], (620, 420))

        write_word(screen, '开始游戏', 36, (255, 255, 255), (350, 250))
        write_word(screen, '退出游戏', 36, (255, 255, 255), (350, 300))
        self.screen.blit(bonus['life'], (300, 250))

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
                        if self.status == 1:
                            screen.fill((100, 150, 250), (300, 250, 40, 40))
                            screen.blit(bonus['life'], (300, 300))
                            self.status = 2
                    elif event.key == K_UP:
                        if self.status == 2:
                            screen.fill((100, 150, 250), (300, 300, 40, 40))
                            screen.blit(bonus['life'], (300, 250))
                            self.status = 1
                    elif event.key == K_RETURN:
                        if self.status == 1:
                            gamescene = GameScene(self.screen)
                            gamescene.show()
                        elif self.status == 2:
                            sys.exit(0)

            pygame.display.update()