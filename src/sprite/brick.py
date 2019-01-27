
from src.tool.init import *

# 砖块管理类
# 当Mario撞击扎砖块时, 根据砖块的类型做出相应的操作
class BrickManager():
    def __init__(self):
        pass


    # 判断哪种类型的砖块被撞击并做出相应的操作
    def bump(self, i, j):
        if level.map[i][j] == 2:
            pygame.mixer.Sound.play(sound['brick_smash'])
            level.map[i][j] = 0
        elif level.map[i][j] == 3:
            pygame.mixer.Sound.play(sound['coin'])
            level.map[i][j] = 4
            level.map[i - 1][j] = 5
        elif level.map[i][j] == 6:
            pygame.mixer.Sound.play(sound['brick_smash'])
            level.map[i][j] = 4
            level.map[i - 1][j] = 7