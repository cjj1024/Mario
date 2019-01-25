
from src.tool.init import *
from src.tool.globaldata import *

class BrickManager():
    def __init__(self):
        pass


    # 判断哪种类型的砖块被撞击并做出相应的操作
    def bump(self, i, j):
        if scene1[i][j] == 2:
            pygame.mixer.Sound.play(sound['brick_smash'])
            scene1[i][j] = 0
        elif scene1[i][j] == 3:
            pygame.mixer.Sound.play(sound['coin'])
            scene1[i][j] = 4
            scene1[i-1][j] = 5