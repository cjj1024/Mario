from src.tool.init import *

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mario_right['slice_0_7']
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.shape = SMALL
        self.status = STAND
        self.direction = RIGHT
        self.animationNum = 0

        self.init_animation()
        self.set_shape(SMALL)


    def update(self):
        if self.status == WALK:
            if self.direction == LEFT:
                self.rect.x -= 10
                if self.animationNum < len(self.small_walk_left) - 1:
                    self.animationNum += 1
                else:
                    self.animationNum = 0
                self.image = self.small_walk_left[self.animationNum]
            else:
                self.rect.x += 10
                if self.animationNum < len(self.small_walk_right) - 1:
                    self.animationNum += 1
                else:
                    self.animationNum = 0
                self.image = self.small_walk_right[self.animationNum]
        elif self.status == STAND:
            if self.direction == LEFT:
                self.image = self.small_stand_left
            else:
                self.image = self.small_stand_right



    def set_status(self, status):
        self.status = status


    def set_direction(self, direction):
        self.direction = direction


    def get_rect(self):
        return self.rect

    def set_shape(self, shape):
        self.shape = shape
        if self.shape == SMALL:
            self.rect.y = 520
        elif self.shape == BIG:
            self.rect.y = 480

    def init_animation(self):
        self.big_stand_right = mario_right['slice_0_7']
        self.big_stand_left = mario_left['slice_0_7']
        self.big_walk_left = [mario_left['slice_0_1'], mario_left['slice_0_2']]
        self.big_walk_right = [mario_right['slice_0_1'], mario_right['slice_0_2']]

        self.small_stand_right = pygame.transform.scale(self.big_stand_right,
                                                        (int(self.big_stand_right.get_rect().width / 2),
                                                        int(self.big_stand_right.get_rect().height / 2)))
        self.small_stand_left = pygame.transform.scale(self.big_stand_left,
                                                        (int(self.big_stand_left.get_rect().width / 2),
                                                        int(self.big_stand_left.get_rect().height / 2)))
        self.small_walk_left = []
        for mario in self.big_walk_left:
            self.small_walk_left.append(pygame.transform.scale(mario, (int(mario.get_rect().width / 2),
                                                                       int(mario.get_rect().height / 2))))
        self.small_walk_right = []
        for mario in self.big_walk_right:
            self.small_walk_right.append(pygame.transform.scale(mario, (int(mario.get_rect().width / 2),
                                                                       int(mario.get_rect().height / 2))))