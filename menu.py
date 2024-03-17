import numpy as np
from utils import *
import pygame

def menu_logic(mode: Mode, input):
    point = input[0]
    mode_selector = 0
    if point:
        if point[0] > 12:
            mode_selector += 1
        elif point[0] < 5:
            mode_selector -= 1
        else:
            pass
    return mode.frame

#Menu mode set up
menu_image = pygame.image.load('menu_thumb.png')
menu_map = pygame.surfarray.pixels3d(menu_image)
menu = Mode("Menu", menu_map, menu_logic, frame = menu_map[0:16])