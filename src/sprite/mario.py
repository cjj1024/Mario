
from src.tool.init import *
from src.tool.globaldata import *

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mario_small_right_img[0][6]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 300
        self.shape = SMALL
        self.status = STAND
        self.direction = NODIRECTION
        self.animationNum = 0
        self.speed_x = 0
        self.speed_y = 0

        self.move_scene = False

        self.init_image()
        self.set_shape(SMALL)


    # 处理与group中的奖励蘑菇发生碰撞
    def process_bonus_collision(self, group):
        for bonus in group:
            if pygame.Rect.colliderect(self.rect, bonus.rect):
                # 变大蘑菇
                if bonus.get_type() == GROW_BIGGER:
                    self.set_shape(BIG)
                    bonus.kill()


    # 处理与group中的敌人发生碰撞
    def process_enemy_collision(self, group):
        pass
        
        # if self.status == DEATH:
        #     return (0, 0)
        # for enemy in group:
        #     if enemy.get_status() == DEATH:
        #         continue
        #     if pygame.Rect.colliderect(self.rect, enemy.rect):
        #         # 踩在敌人的头上, 杀死敌人
        #         print(self.Y, enemy.Y)
        #         if self.Y + self.rect.height - 20 < enemy.Y:
        #             enemy.set_status(DEATH)
        #         # 其他位置碰到敌人, 死亡
        #         else:
        #             self.set_status(DEATH)


    def check_move_scene(self):
        return self.move_scene


    def update(self):
        if self.is_sky():
            self.move_y()

        if self.status == DEATH:
            self.death()
        elif self.status == STAND:
            self.stand()
        elif self.status == WALK:
            self.walk()
        elif self.status == JUMP:
            self.jump()


        if self.X > 400 and level.start + 840 < level.length:
            self.X -= 10
            self.move_scene = True
        else:
            self.move_scene = False
            

    def is_sky(self):
        i, j = self.get_foot_grid()
        if level.map[i][j] == 0:
            return True
        else:
            return False


    def death(self):
        # if self.Y > 600:
        #     self.kill()
        self.image = self.small_dead_img
        self.kill()
        # self.Y += self.speed_y
        # self.speed_y -= GRAVITY_Y


    def jump(self):
        self.move_y()

        if self.direction == LEFT:
            self.speed_x = -15
            self.move_x()
            self.image = self.jump_left
        elif self.direction == RIGHT:
            self.speed_x = 15
            self.move_x()
            self.image = self.jump_right



    def move_y(self):
        # 在速度小于最大速度之前, 速度不断增加
        if self.speed_y < MAX_SPEED_Y:
            self.speed_y += GRAVITY_Y

        i, j = self.get_next_grid_vert()

        # 向下落会遇到障碍换或超出屏幕边界
        if self.Y + self.speed_y < 0 or self.Y + self.speed_y >= 560 or level.map[i][j] != 0:
            self.Y = (i - 1) * 40
            self.speed_y = 0
            if self.status == JUMP:
                self.status = STAND
        else:
            self.Y += self.speed_y


    def move_x(self):
        i, j = self.get_next_grid_vert()
        # 向左走会遇到障碍换或超出屏幕边界
        if self.X + self.speed_x >= 760 or self.X + self.speed_x <= 0 or level.map[i][j] != 0 :
            self.speed_x = 0
            self.status = STAND
        else:
            self.X += self.speed_x



    def walk(self):
        # 循环播放动画
        self.animationNum = (self.animationNum + 1) % (len(self.walk_left) - 1)

        if self.direction == LEFT:
            self.speed_x = -15
            self.move_x()
            self.image = self.walk_left[self.animationNum]
        else:
            self.speed_x = 15
            self.move_x()
            self.image = self.walk_right[self.animationNum]


    def stand(self):
        if self.direction == LEFT:
            self.image = self.stand_left
        else:
            self.image = self.stand_right


    def set_status(self, status):
        # 当前状态已经是死亡, 跳跃
        if self.status == DEATH or self.status == JUMP:
            return
        # 要变成死亡状态
        if status == DEATH:
            self.status = DEATH
            pygame.mixer.Sound.play(sound['death'])
            return

        if self.status != JUMP:
            self.status = status

        if status == JUMP:
            self.speed_y = -40
            pygame.mixer.Sound.play(sound['small_jump'])
        elif status == STAND:
            self.speed_x = 0
            self.speed_y = 0


    def set_direction(self, direction):
        if self.status != JUMP:
            self.direction = direction


    # 获得坐标在地图中的映射, x, y 为偏移量
    def get_grid(self, x=0, y=0):
        i = int((self.Y + y) / 40)
        j = int((level.start + self.X + x) / 40)

        return i, j


    def get_next_grid_hori(self):
        i, j = self.get_grid(x=self.speed_x)

        # 速度大于0, 向右移动, j加1时因为i,j为左上角
        if self.speed_x > 0:
            return i, j + 1
        else:
            return i, j


    def get_next_grid_vert(self):
        i, j = self.get_grid(y=self.speed_y)

        # 速度大于0, 向下移动, i加1时因为i,j为左上角
        if self.speed_y > 0:
            return i + 1, j
        else:
            return i, j


    def get_foot_grid(self):
        i, j = self.get_grid(x=self.rect.width / 2)

        return i + 1, j


    @property
    def X(self):
        return self.rect.x


    @X.setter
    def X(self, x):
        self.rect.x = x


    @property
    def Y(self):
        return self.rect.y


    @Y.setter
    def Y(self, y):
        self.rect.y = y


    def set_shape(self, shape):
        self.shape = shape
        if self.shape == SMALL:
            self.stand_left = self.small_stand_left_img
            self.stand_right = self.small_stand_right_img
            self.walk_left = self.small_walk_left_img
            self.walk_right = self.small_walk_right_img
            self.jump_left = self.small_jump_left_img
            self.jump_right = self.small_jump_right_img

            self.rect.width = self.stand_left.get_rect().width
            self.rect.height = self.stand_left.get_rect().height
            self.Y += 40
        elif self.shape == BIG:
            self.stand_left = self.big_stand_left_img
            self.stand_right = self.big_stand_right_img
            self.walk_left = self.big_walk_left_img
            self.walk_right = self.big_walk_right_img
            self.jump_left = self.big_jump_left_img
            self.jump_right = self.big_jump_right_img

            self.rect.width = self.stand_left.get_rect().width
            self.rect.height = self.stand_left.get_rect().height
            self.Y -= 40


    def init_image(self):
        self.big_stand_right_img = mario_big_right_img_img[0][6]
        self.big_stand_left_img = mario_big_left[0][6]

        self.big_walk_right_img = [mario_big_right_img_img[0][0], mario_big_right_img_img[0][1],
                                   mario_big_right_img_img[0][2]]
        self.big_walk_left_img = [mario_big_left[0][0], mario_big_left[0][1],
                                  mario_big_left[0][2]]

        self.big_jump_right_img = mario_big_right_img_img[0][4]
        self.big_jump_left_img = mario_big_left[0][4]

        self.small_dead_img = mario_small_right_img[0][5]

        self.small_stand_right_img = mario_small_right_img[0][6]
        self.small_stand_left_img = mario_small_left_img[0][6]

        self.small_walk_right_img = [mario_small_right_img[0][0], mario_small_right_img[0][1],
                                     mario_small_right_img[0][2]]
        self.small_walk_left_img = [mario_small_left_img[0][0], mario_small_left_img[0][1],
                                    mario_small_left_img[0][2]]

        self.small_jump_right_img = mario_small_right_img[0][4]
        self.small_jump_left_img = mario_small_left_img[0][4]

        self.small_dead_img = mario_small_right_img[0][5]



