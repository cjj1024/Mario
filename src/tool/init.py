from .load import *


pygame.init()
screen = pygame.display.set_mode((800, 600))

ground_img =                load_image('./res/image/tile/ground')
background_img =            load_image('./res/image/background')
mario_big_right_img =       load_image('./res/image/character/mario/big')
mario_small_right_img =   load_image('./res/image/character/mario/small')
goomba_img =                load_image('./res/image/character/goomba')
turtle_img =                load_image('./res/image/character/turtle')
bonus_img =                 load_image('./res/image/bonus')
fire_img =                  load_image('./res/image/fire')
music =                     load_music('./res/music')
sound =                     load_sound('./res/sound')

LEFT =      1
RIGHT =     2

STAND =     1
WALK =      2
RUN =       3
JUMP =      4
DEATH =      5

SMALL =     1
BIG =       2

JUMP_VERT_SPEED =   -20
JUMP_HORI_SPEED =   4
GRAVITY         =   2

background_img['background'] =  pygame.Surface((800, 600))
background_img['background'].fill((100, 150, 250))

mario_big_left_img = {}
for key in mario_big_right_img.keys():
    mario = mario_big_right_img[key]
    mario_big_right_img[key] = pygame.transform.scale(mario, (int(mario.get_rect().width * 2.5),
                                                              int(mario.get_rect().height * 2.5)))
    mario_big_left_img[key] = pygame.transform.flip(mario_big_right_img[key], True, False)

mario_small_left_img = {}
for key in mario_small_right_img.keys():
    mario = mario_small_right_img[key]
    mario_small_right_img[key] = pygame.transform.scale(mario, (int(mario.get_rect().width * 2.5),
                                                              int(mario.get_rect().height * 2.5)))
    mario_small_left_img[key] = pygame.transform.flip(mario_small_right_img[key], True, False)

pygame.display.set_caption('超级玛丽')
icon = pygame.image.load('./res/image/icon.bmp')
icon.set_colorkey((255, 0, 255))
pygame.display.set_icon(icon)
