

from src.tool.tool import *
from src.scene.level import *



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


# 获得一个800x600的矩形表面
background_img['background'] =  pygame.Surface((800, 600))
# 给矩形表面填充颜色
background_img['background'].fill((100, 150, 250))

# 把得到的图片大小调为原来的2.5倍
# 把向右的图片翻转得到向左的图片
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
icon = pygame.image.load('./res/image/Mario.png')
icon.set_colorkey((255, 0, 255))
pygame.display.set_icon(icon)


level = Level(1)

# 防止循环import
# 必须放在sound的声明后
from src.sprite.brick import *
brick_manager = BrickManager()