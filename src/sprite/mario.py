from src.tool.init import *

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mario_big_right_img['stand']
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.shape = SMALL
        self.status = STAND
        self.direction = RIGHT
        self.animationNum = 0
        self.speed = 10
        self.speed_up = -15
        self.gravity = 1

        self.init_animation()
        self.set_shape(SMALL)


    def update(self):
        if self.status == STAND:
            self.stand()
        elif self.status == WALK:
            self.walk()
        elif self.status == JUMP:
            self.jump()


    def jump(self):
        if self.rect.y + self.speed_up > 520:
            self.speed_up = -15
            self.status = STAND
        else:
            self.rect.y += self.speed_up
            self.speed_up += self.gravity
        if self.direction == LEFT:
            if self.rect.x - self.speed < 0:
                return
            self.rect.x -= self.speed
            self.image = self.small_jump_left
        else:
            if self.rect.x + self.speed > 780:
                return
            self.rect.x += self.speed
            self.image = self.small_jump_right

    def walk(self):
        if self.direction == LEFT:
            if self.rect.x - self.speed < 0:
                return
            self.rect.x -= self.speed
            if self.animationNum < len(self.small_walk_left) - 1:
                self.animationNum += 1
            else:
                self.animationNum = 0
            self.image = self.small_walk_left[self.animationNum]
        else:
            if self.rect.x + self.speed > 780:
                return
            self.rect.x += self.speed
            if self.animationNum < len(self.small_walk_right) - 1:
                self.animationNum += 1
            else:
                self.animationNum = 0
            self.image = self.small_walk_right[self.animationNum]


    def stand(self):
        if self.direction == LEFT:
            self.image = self.small_stand_left
        else:
            self.image = self.small_stand_right



    def set_status(self, status):
        if self.status != JUMP:
            self.status = status


    def set_direction(self, direction):
        if self.status != JUMP:
            self.direction = direction


    def set_shape(self, shape):
        self.shape = shape
        if self.shape == SMALL:
            self.rect.y = 520
        elif self.shape == BIG:
            self.rect.y = 480


    def init_animation(self):
        self.big_stand_left = mario_big_left_img['stand']
        self.big_stand_right = mario_big_right_img['stand']

        self.big_walk_left = [mario_big_left_img['walk1'], mario_big_left_img['walk2'],
                              mario_big_left_img['walk3']]
        self.big_walk_right = [mario_big_right_img['walk1'], mario_big_right_img['walk2'],
                               mario_big_right_img['walk3']]

        self.big_jump_left = mario_big_left_img['jump']
        self.big_jump_right = mario_big_right_img['jump']

        self.small_stand_left = mario_small_left_img['stand']
        self.small_stand_right = mario_small_right_img['stand']

        self.small_walk_left = [mario_small_left_img['walk1'], mario_small_left_img['walk2'],
                                mario_small_left_img['walk3']]
        self.small_walk_right = [mario_small_right_img['walk1'], mario_small_right_img['walk2'],
                                 mario_small_right_img['walk3']]

        self.small_jump_left = mario_small_left_img['jump']
        self.small_jump_right = mario_small_right_img['jump']