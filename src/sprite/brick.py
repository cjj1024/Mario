
from src.tool.init import *

# 砖块管理类
# 当Mario撞击扎砖块时, 根据砖块的类型做出相应的操作
class BrickManager():
    def __init__(self):
        pass

    # 10 表示空箱子
    # 11 表示可被撞击碎裂砖块
    # 12 表示有硬币的箱子
    # 13 表示有变大蘑菇的箱子
    #
    # 21 表示硬币
    # 22 表示长大蘑菇
    # 判断哪种类型的砖块被撞击并做出相应的操作
    def bump(self, i, j):
        # 可被撞碎的砖块
        if level.map[i][j] == 11:
            pygame.mixer.Sound.play(sound['brick_smash'])
            level.map[i][j] = 0
        # 有硬币的箱子
        elif level.map[i][j] == 12:
            pygame.mixer.Sound.play(sound['coin'])
            level.map[i][j] = 10
            level.map[i - 1][j] = 21
        # 有长大蘑菇的箱子
        elif level.map[i][j] == 13:
            pygame.mixer.Sound.play(sound['brick_smash'])
            level.map[i][j] = 10
            level.map[i - 1][j] = 22