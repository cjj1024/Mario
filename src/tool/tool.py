import pygame
import os

def load_image(directory, colorkey=(255, 0, 255), accept=('.jpg', '.bmp', '.png')):
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


# pygame不能直接一次性加载全部music
# 此函数只加载了music的文件名
def load_music(directory, accept=('.mp3', '.wav', '.ogg')):
    music_dir = {}
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() in accept:
            music = os.path.join(directory, filename)
            music_dir[name] = music

    return music_dir


def load_sound(directory, accept=('.mp3', '.wav', '.ogg')):
    sounds = {}
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() in accept:
            sound = pygame.mixer.Sound(os.path.join(directory, filename))
            sounds[name] = sound

    return sounds


def write_word(screen, word, size, color, position):
    # 加载字体并设置字体大小
    font = pygame.font.Font('./res/font/geteshi.ttf', size)
    # 把文字画在一个Surface上
    word_image = font.render(word, False, color)
    # 把得到的文字Surface画在屏幕Surface上
    screen.blit(word_image, position)