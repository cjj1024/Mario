
from src.tool.init import *
from src.tool.globaldata import *

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mario_small_right_img[0][6]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.shape = SMALL
        self.status = STAND
        self.direction = RIGHT
        self.animationNum = 0
        self.speed = 10
        self.jump_hori_speed = JUMP_HORI_SPEED
        self.jump_vert_speed = JUMP_VERT_SPEED
        self.gravity = GRAVITY

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
        if self.status == DEATH:
            return (0, 0)
        for enemy in group:
            if enemy.get_status() == DEATH:
                continue
            if pygame.Rect.colliderect(self.rect, enemy.rect):
                # 踩在敌人的头上, 杀死敌人
                # print(self.rect)
                # print(enemy.rect)
                if self.rect.y + 30 > enemy.rect.y:
                    self.set_status(DEATH)
                # 其他位置碰到敌人, 死亡
                else:
                    enemy.set_status(DEATH)


    def check_move_scene(self):
        return self.move_scene



    def update(self):
        if self.status != DEATH and level.map[int((self.rect.y + self.rect.height + 5) / 40)][int((self.rect.x + level.start) / 40)] == 0:
            self.rect.y += 10
        if self.status == STAND:
            self.stand()
        elif self.status == WALK:
            self.walk()
        elif self.status == JUMP:
            self.jump()
        elif self.status == DEATH:
            self.death()

        if self.rect.x > 400 and level.start + 840 < level.length:
            self.rect.x -= 10
            self.move_scene = True
        else:
            self.move_scene = False

    def death(self):
        if self.rect.y > 600:
            self.kill()
        self.image = self.small_dead_img
        self.rect.y += self.jump_vert_speed
        self.jump_vert_speed += self.gravity


    def jump(self):
        if self.direction == LEFT:
            # 到达屏幕左边界
            if self.rect.x - self.jump_hori_speed < 0:
                self.rect.x = 0
            else:
                self.rect.x -= self.jump_hori_speed
            self.image = self.jump_left
        else:
            # 到达屏幕右边界
            if self.rect.x + self.jump_hori_speed > 780:
                self.rect.x = 760
            else:
                self.rect.x += self.jump_hori_speed
            self.image = self.jump_right

        # 计算当前坐标在二维数组中的映射
        # 加横坐标, 纵坐标都加20为Mario的中心
        # i_head 为头顶上一格
        # i_foot 为脚底下一格
        i_head = int((self.rect.y + self.jump_vert_speed) / 40)
        i_foot = int((self.rect.y + self.rect.height + self.jump_vert_speed) / 40)
        j = int((self.rect.x + level.start + 20) / 40)

        # 跳跃上升时头上有物体
        if level.map[i_head][j] != 0 and self.jump_vert_speed < 0:
            brick_manager.bump(i_head, j)
            self.jump_vert_speed = JUMP_VERT_SPEED
            self.status = STAND
        # 跳跃下降时脚下有物体

        elif level.map[i_foot][j] != 0 and self.jump_vert_speed > 0:
            self.rect.y = i_head * 40
            self.jump_vert_speed = JUMP_VERT_SPEED
            self.status = STAND
        else:
            self.rect.y += self.jump_vert_speed
            self.jump_vert_speed += self.gravity


    def walk(self):
        if self.direction == LEFT:
            # 到达屏幕左边界
            if self.rect.x - self.speed < 0:
                return

            self.rect.x -= self.speed

            # 循环播放walk动画
            if self.animationNum < len(self.walk_left) - 1:
                self.animationNum += 1
            else:
                self.animationNum = 0
            self.image = self.walk_left[self.animationNum]
        else:
            # 到达屏幕右边界
            if self.rect.x + self.speed > 780:
                return

            self.rect.x += self.speed

            # 循环播放walk动画
            if self.animationNum < len(self.walk_right) - 1:
                self.animationNum += 1
            else:
                self.animationNum = 0
            self.image = self.walk_right[self.animationNum]


    def stand(self):
        if self.direction == LEFT:
            self.image = self.stand_left
        else:
            self.image = self.stand_right


    def set_status(self, status):
        if self.status == DEATH:
            return
        if status == DEATH:
            self.status = DEATH
            pygame.mixer.Sound.play(sound['death'])
            return
        if self.status != JUMP:
            self.status = status
        if status == JUMP:
            pygame.mixer.Sound.play(sound['small_jump'])


    def set_direction(self, direction):
        if self.status != JUMP:
            self.direction = direction


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
            self.rect.y = 520
        elif self.shape == BIG:
            self.stand_left = self.big_stand_left_img
            self.stand_right = self.big_stand_right_img
            self.walk_left = self.big_walk_left_img
            self.walk_right = self.big_walk_right_img
            self.jump_left = self.big_jump_left_img
            self.jump_right = self.big_jump_right_img
            self.rect.width = self.stand_left.get_rect().width
            self.rect.height = self.stand_left.get_rect().height
            self.rect.y = 480


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



