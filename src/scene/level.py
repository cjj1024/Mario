import json

class Level():
    def __init__(self, level):


        filename = './res/level/level' + str(level) + '.json'
        with open(filename) as fp:
            data = json.load(fp)
            # print(data)

        self.length = data['length']
        self.start_x = 0
        # 把屏幕划分成二维的格子
        # 每个格子为40x40px
        # 0 什么都没有
        #
        # 100 小灌木
        # 101 大灌木
        # 200 小云
        # 201 大云
        #
        # 1000 砖块1
        # 1001 砖块2
        # 1002 砖块3
        #
        # 1200 管道
        # 1001 管道其他部分
        #
        # 2100 硬币箱子
        # 2200 长大蘑菇箱子
        # 2201 生命蘑菇箱子
        # 2202 死亡蘑菇箱子
        #
        # 3100 硬币
        # 3200 长大蘑菇
        # 3201 加命蘑菇
        # 3202 死亡蘑菇
        #
        # 4000 Goomba

        self.map = []
        for i in range(15):
            self.map.append([0] * int(self.length / 40))

        self.pipe = data['object']['pipe']
        for x, y in self.pipe:
            self.map[int(y / 40)][int(x / 40)] = 1200
            self.map[int(y / 40) + 1][int(x / 40)] = 1201
            self.map[int(y / 40)][int(x / 40) + 1] = 1201
            self.map[int(y / 40) + 1][int(x / 40) + 1] = 1201

        self.ground = data['object']['brick1']
        for x, y in self.ground:
            self.map[int(y / 40)][int(x / 40)] = 1000

        self.ground = data['object']['brick2']
        for x, y in self.ground:
            self.map[int(y / 40)][int(x / 40)] = 1001

        self.ground = data['object']['brick3']
        for x, y in self.ground:
            self.map[int(y / 40)][int(x / 40)] = 1002

        self.brick_coin = data['object']['coin']
        for x, y in self.brick_coin:
            self.map[int(y / 40)][int(x / 40)] = 2100

        self.brick_mushroom_grow = data['object']['mushroom_grow']
        for x, y in self.brick_mushroom_grow:
            self.map[int(y / 40)][int(x / 40)] = 2200

        self.brick_mushroom_grow = data['object']['mushroom_life']
        for x, y in self.brick_mushroom_grow:
            self.map[int(y / 40)][int(x / 40)] = 2201

        self.brick_mushroom_grow = data['object']['mushroom_death']
        for x, y in self.brick_mushroom_grow:
            self.map[int(y / 40)][int(x / 40)] = 2202