import pygame
import os


def load_image(directory, colorkey=(255, 0, 255), accept=('.jpg', '.bmp', '.png')):
    images = {}
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(directory, filename))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img.set_colorkey(colorkey)
                img = img.convert()
            images[name] = img

    return images


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
    font = pygame.font.Font('./res/font/geteshi.ttf', size)
    start_game = font.render(word, False, color)
    screen.blit(start_game, position)