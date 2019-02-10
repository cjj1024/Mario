
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

        self.score = 0
        self.life = 3

        self.init_image()
        self.set_shape(SMALL)


    def update(self):
        if abs(self.speed_y + GRAVITY_Y) < MAX_SPEED_Y:
            self.speed_y += GRAVITY_Y

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


    def death(self):
        self.image = self.small_dead_img
        self.kill()


    def jump(self):
        if self.direction == LEFT:
            self.speed_x = -10
            self.image = self.jump_left
        elif self.direction == RIGHT:
            self.speed_x = 10
            self.image = self.jump_right

        self.status = FALL


    def fall(self):
        self.speed_y += GRAVITY_Y


    def walk(self):
        # 循环播放动画
        self.animationNum = (self.animationNum + 1) % (len(self.walk_left) - 1)

        if self.direction == LEFT:
            self.speed_x = -10
            self.image = self.walk_left[self.animationNum]
        else:
            self.speed_x = 10
            self.image = self.walk_right[self.animationNum]


    def stand(self):
        if self.direction == LEFT:
            self.image = self.stand_left
        else:
            self.image = self.stand_right


    def set_status(self, status):
        # 当前状态已经是死亡
        if self.status == DEATH:
            return

        if self.status == FALL and status == JUMP:
            return

        # 要变成死亡状态
        if status == DEATH:
            self.status = DEATH
            pygame.mixer.Sound.play(sound['death'])
            return

        if self.status != JUMP:
            self.status = status

        if status == JUMP:
            self.speed_y = INIT_JUMP_SPEED_Y
            pygame.mixer.Sound.play(sound['small_jump'])
        elif status == STAND:
            self.speed_x = 0
            self.speed_y = 0


    def set_direction(self, direction):
        if self.status != JUMP:
            self.direction = direction




    def get_grid(self, x, y):
        if y < 0:
            y = 0
        elif y > 560:
            y = 560
        elif x < 0:
            x = 0
        elif x >= level.length:
            x = level.length - 10
        return int(y / 40), int(x / 40)


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
            self.rect.y += 40
        elif self.shape == BIG:
            self.stand_left = self.big_stand_left_img
            self.stand_right = self.big_stand_right_img
            self.walk_left = self.big_walk_left_img
            self.walk_right = self.big_walk_right_img
            self.jump_left = self.big_jump_left_img
            self.jump_right = self.big_jump_right_img

            self.rect.width = self.stand_left.get_rect().width
            self.rect.height = self.stand_left.get_rect().height
            self.rect.y -= 40


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



