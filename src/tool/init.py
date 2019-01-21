from .load import *


pygame.init()
screen = pygame.display.set_mode((800, 600))

ground =        load_image('./res/image/tile/ground')
background =    load_image('./res/image/background')
background['background'] = pygame.Surface((800, 600))
background['background'].fill((100, 150, 250))
mario_right =   load_image('./res/image/character/mario')
goomba =        load_image('./res/image/character/goomba')
turtle =        load_image('./res/image/character/turtle')
bonus =         load_image('./res/image/bonus')
fire =          load_image('./res/image/fire')
music =         load_music('./res/music')
sound =         load_sound('./res/sound')

LEFT =      1
RIGHT =     2
STAND =     0
WALK =      10
RUN =       20

SMALL =     1
BIG =       2

mario_left = {}
for key in mario_right.keys():
    mario = mario_right[key]
    mario_right[key] = pygame.transform.scale(mario, (int(mario.get_rect().width * 2.5),
                                                     int(mario.get_rect().height * 2.5)))
    mario_left[key] = pygame.transform.flip(mario_right[key], True, False)

pygame.display.set_caption('超级玛丽')
pygame.display.set_icon(mario_right['slice_0_1'])