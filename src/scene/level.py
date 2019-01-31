import json

class Level():
    def __init__(self, level):


        filename = './res/level/level' + str(level) + '.json'
        with open(filename) as fp:
            data = json.load(fp)
            # print(data)

        self.length = data['length']
        self.start = 0
        # 把屏幕划分成二维的格子
        # 每个格子为40x40px
        # 0 表示什么都没有
        # 1 表示地面
        #
        # 10 表示空箱子
        # 11 表示可被撞击碎裂砖块
        # 12 表示有硬币的箱子
        # 13 表示有变大蘑菇的箱子
        #
        # 21 表示硬币
        # 22 表示长大蘑菇
        #
        # 31 表示Goomba

        self.map = []
        for i in range(15):
            self.map.append([0] * int(self.length / 40))

        self.ground = data['object']['ground']
        for x, y in self.ground:
            self.map[int(y / 40)][int(x / 40)] = 1

        self.brick = data['object']['brick']
        for x, y in self.brick:
            self.map[int(y / 40)][int(x / 40)] = 11

        self.brick_coin = data['object']['brick_coin']
        for x, y in self.brick_coin:
            self.map[int(y / 40)][int(x / 40)] = 12

        self.brick_mushroom_grow = data['object']['brick_mushroom_grow']
        for x, y in self.brick_mushroom_grow:
            self.map[int(y / 40)][int(x / 40)] = 13