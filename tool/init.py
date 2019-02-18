import pygame

from .tool import *
from .globaldata import *



pygame.init()
pygame.display.set_mode((800, 600))

mario_img = load_image('./res/image/mario.png')

# big 40x80px
# small 40x40px
mario_small_right_img = []
mario_small_left_img = []
mario_big_right_img_img = []
mario_big_left = []
for j in range(19):
    small_right = []
    small_left = []
    big_right = []
    big_left = []

    for i in range(11):
        big = get_image(mario_img, i * 16, j * 48, 16, 32)
        small = get_image(mario_img, i * 16, j * 48 + 32, 16, 16)

        big_right.append(big)
        small_right.append(small)

        big_left.append(pygame.transform.flip(big, True, False))
        small_left.append(pygame.transform.flip(small, True, False))

    mario_small_right_img.append(small_right)
    mario_small_left_img.append(small_left)
    mario_big_right_img_img.append(big_right)
    mario_big_left.append(big_left)


enemy_img = load_image('./res/image/enemy.png')

goomba_img = []
# 40x40px
for i in range(3):
    goomba_img.append(get_image(enemy_img, i * 16, 16, 16, 16))

koopa_left_img = []
koopa_right_img = []
# 40x60px
for i in range(6):
    img = get_image(enemy_img, i * 16 + 96, 8, 16, 24)
    koopa_left_img.append(img)
    koopa_right_img.append(pygame.transform.flip(img, True, False))

piranha_img = []
# 40x60px
for i in range(2):
    piranha_img.append(get_image(enemy_img, i * 16 + 192, 8, 16, 24))


background_img = load_image('./res/image/background.png')

# 0 地面
# 1 不可摧毁的砖块
# 2 可摧毁的砖块
# 6 奖励出现后的砖块
brick_img = []
# 40x40px
for i in range(4):
    brick_img.append(get_image(background_img, i * 16, 0, 16, 16))
    brick_img.append(get_image(background_img, i * 16, 16, 16, 16))

castle_brick_img = []
# 40x40px
for i in range(4):
    castle_brick_img.append(get_image(background_img, i * 16 + 176, 0, 16, 16))
    castle_brick_img.append(get_image(background_img, i * 16 + 176, 16, 16, 16))

# 0 小云
# 1 大云
cloud_img = []
# 80x60px
cloud_img.append(get_image(background_img, 8, 320, 32, 24))
# 120x40px
cloud_img.append(get_image(background_img, 126, 320, 48, 16))
cloud_img[1] = pygame.transform.flip(cloud_img[1], False, True)

# 0 小灌木
# 1 大灌木
brushwood_img = []
# 80x40px
brushwood_img.append(get_image(background_img, 184, 144, 32, 16))
# 120x80px
brushwood_img.append(get_image(background_img, 352, 128, 48, 32))

# 管道
pipe_img = []
# 80x80
pipe_img.append(get_image(background_img, 0, 160, 32, 32))


item_img = load_image('./res/image/item.png')

# 0 变大蘑菇
# 2 生命蘑菇
# 4 死亡蘑菇
mushroom_img = []
# 40x40px
for i in range(3):
    mushroom_img.append(get_image(item_img, i * 16, 0, 16, 16))
    mushroom_img.append(get_image(item_img, i * 16, 16, 16, 16))

# 有奖励的砖块
bonus_brick_img = []
# 40x40px
for i in range(4):
    bonus_brick_img.append(get_image(item_img, i * 16, 80, 16, 16))

# 硬币
coin_img = []
# 40x40px
for i in range(4):
    coin_img.append(get_image(item_img, i * 16, 96, 16, 16))


music =     load_musics('./res/music')
sound =     load_sounds('./res/sound')

font =      pygame.font.Font('./res/font/minicanton.TTF', FONT_SIZE)


pygame.display.set_caption('超级玛丽')
icon = load_image('./res/image/icon.png')
pygame.display.set_icon(icon)

print('init completed')