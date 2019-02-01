
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
        if self.is_sky() and self.status != JUMP:
            self.status = FALL

        if self.status == DEATH:
            self.death()
        elif self.status == STAND:
            self.stand()
        elif self.status == WALK:
            self.walk()
        elif self.status == JUMP:
            self.jump()
        elif self.status == FALL:
            self.fall()

        if self.X > 400 and level.start_x + 840 < level.length:
            self.X -= 10
            self.move_scene = True
        else:
            self.move_scene = False
            

    def is_sky(self):
        x, y = self.get_world_point()
        i, j = self.get_grid(x + self.rect.width / 2, y + self.rect.height + 5)
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
        if self.direction == LEFT:
            self.speed_x = -10
            self.move_left()
            self.image = self.jump_left
        elif self.direction == RIGHT:
            self.speed_x = 10
            self.move_right()
            self.image = self.jump_right

        if self.speed_y < 0:
            self.move_up()
        else:
            self.status = FALL




    def fall(self):
        self.move_down()


    def move_up(self):
        if abs(self.speed_y) < MAX_SPEED_Y:
            self.speed_y += GRAVITY_Y

        x, y = self.get_world_point()

        i, j = self.get_grid(x + self.rect.width / 2, y + self.speed_y)
        if level.map[i][j] == 0:
            self.Y += self.speed_y
        else:
            brick_manager.bump(i, j)
            self.Y = (i + 1) * 40
            self.speed_y = 0
            self.status = STAND

        if self.Y < 0:
            self.Y = 0
        if self.Y > 560:
            self.Y = 560


    def move_down(self):
        if abs(self.speed_y) < MAX_SPEED_Y:
            self.speed_y += GRAVITY_Y

        x, y = self.get_world_point()

        i, j = self.get_grid(x + self.rect.width / 2, y + self.rect.height + self.speed_y)
        if level.map[i][j] == 0:
            self.Y += self.speed_y
        else:
            self.Y = i * 40 - self.rect.height
            self.speed_y = 0
            self.status = STAND

        if self.Y < 0:
            self.Y = 0
        if self.Y > 560:
            self.Y = 560



    def move_left(self):
        x, y = self.get_world_point()

        i, j = self.get_grid(x + self.speed_x, y)
        if level.map[i][j] == 0:
            self.X += self.speed_x
        else:
            self.speed_x = 0


        if self.X < 0:
            self.X = 0
        if self.X > 760:
            self.X = 760


    def move_right(self):
        x, y = self.get_world_point()

        i, j = self.get_grid(x + self.rect.width + self.speed_x, y)
        if level.map[i][j] == 0:
            self.X += self.speed_x
        else:
            self.speed_x = 0


        if self.X < 0:
            self.X = 0
        if self.X > 760:
            self.X = 760


    def walk(self):
        # 循环播放动画
        self.animationNum = (self.animationNum + 1) % (len(self.walk_left) - 1)

        if self.direction == LEFT:
            self.speed_x = -10
            self.move_left()
            self.image = self.walk_left[self.animationNum]
        else:
            self.speed_x = 10
            self.move_right()
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
            self.speed_y = -39
            pygame.mixer.Sound.play(sound['small_jump'])
        elif status == STAND:
            self.speed_x = 0
            self.speed_y = 0


    def set_direction(self, direction):
        if self.status != JUMP:
            self.direction = direction


    # 把屏幕坐标转换为世界坐标
    def get_world_point(self):
        return level.start_x + self.X, self.Y


    def get_grid(self, x, y):
        return int(y / 40), int(x / 40)


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



