import pygame
import os
from .globaldata import *

def load_images(directory, colorkey=MAGENTA, accept=('.jpg', '.bmp', '.png')):
    images = {}
    for filename in os.listdir(directory):
        # 把文件名分成名字和扩展名
        name, ext = os.path.splitext(filename)
        # 判断文件是否为可接受的文件类型
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(directory, filename))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img.set_colorkey(colorkey)
                img = img.convert()
            images[name] = img

    return images


def load_image(filename, colorkey=MAGENTA, accept=('.jpg', '.bmp', '.png')):
    _, ext = os.path.splitext(filename)
    # 判断文件是否为可接受的文件类型
    if ext.lower() in accept:
        img = pygame.image.load(filename)
        if img.get_alpha():
            img = img.convert_alpha()
        else:
            img.set_colorkey(colorkey)
            img = img.convert()

    return img


# pygame不能直接一次性加载全部music
# 此函数只加载了music的文件名
def load_musics(directory, accept=('.mp3', '.wav', '.ogg')):
    music_dir = {}
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() in accept:
            music = os.path.join(directory, filename)
            music_dir[name] = music

    return music_dir


def load_sounds(directory, accept=('.mp3', '.wav', '.ogg')):
    sounds = {}
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() in accept:
            sound = pygame.mixer.Sound(os.path.join(directory, filename))
            sounds[name] = sound

    return sounds


# # 把文字转化为图片, 显示在屏幕上
# def write_word(screen, word, size, color, position):
#     # 加载字体并设置字体大小
#     font = pygame.font.Font('./res/font/geteshi.ttf', size)
#     # 把文字画在一个Surface上
#     word_image = font.render(word, False, color)
#     # 把得到的文字Surface画在屏幕Surface上
#     screen.blit(word_image, position)


# 从一张大的图片上获得一块小的图片
# surface 为源图片
# x, y 为要获得图片的左上角坐标
# width, height 为要获得图片的长宽
def get_image(surface, x, y, width, height):
    # 获取一块与要截取图片一样大小的表面
    image = pygame.Surface([width, height]).convert()
    image.fill(MAGENTA)
    rect = image.get_rect()
    # 把图片从源表面复制到image
    image.blit(surface, (0, 0), (x, y, width, height))
    # 设置色键, 默认的surface是黑色的
    image.set_colorkey(MAGENTA)
    # 把图片放大2.5倍
    image = pygame.transform.scale(image, (int(rect.width * 2.5), int(rect.height * 2.5)))

    return image