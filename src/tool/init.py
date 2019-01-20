from .load import *


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('超级玛丽')

ground =        load_image('./res/image/tile/ground')
background =    load_image('./res/image/background')
mario_small =   load_image('./res/image/character/small')
mario_big =     load_image('./res/image/character/big')
goomba =        load_image('./res/image/character/goomba')
turtle =        load_image('./res/image/character/turtle')
bonus =         load_image('./res/image/bonus')
fire =          load_image('./res/image/fire')

pygame.display.set_icon(mario_small['stand_right'])

music =         load_music('./res/music')
print(music)
sound =         load_sound('./res/sound')

LEFT =      1
RIGHT =     2
STAND =     0
WALK =      10
RUN =       20