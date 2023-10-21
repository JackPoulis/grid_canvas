import pygame
import numpy as np
from sys import exit
from utils import *

def menu_logic(mode: Mode, input):
    point = input[0]
    if point:
        if point[0] > 12:
            mode.frame = menu_map[16:]
        elif point[0] < 5:
            mode.frame = menu_map[0:16]
        else:
            pass
    return mode.frame

def maze_logic(mode: Mode, input):
    p_c = mode.p[0].c
    p_r = mode.p[0].r
    p_dc = p_c - mode.d_c
    p_dr = p_r - mode.d_r
    if input[0]:
        x, y = input[0]
        if y == p_dr:
            if x < p_dc and mode.map[p_c - 1, p_r] == 1:
                mode.p[0].c -= 1
                if mode.p[0].c - mode.d_c < mode.d_cols/4 and mode.d_c > 0:
                    mode.d_c -= 1
            elif x > p_dc and mode.map[p_c + 1, p_r] == 1:
                mode.p[0].c += 1
                if mode.p[0].c - mode.d_c > mode.d_cols/4*3 and mode.d_c < mode.cols - 1:
                    mode.d_c += 1
        if x == p_dc:
            if y < p_dr and mode.map[p_c, p_r - 1] == 1:
                mode.p[0].r -= 1
                if mode.p[0].r - mode.d_r < mode.d_rows/4 and mode.d_r > 0:
                    mode.d_r -= 1
            elif y > p_dr and mode.map[p_c, p_r + 1] == 1:
                mode.p[0].r += 1
                if mode.p[0].r - mode.d_r > mode.d_rows/4*3 and mode.d_r < mode.rows - 1:
                    mode.d_r += 1
    
    to_rgb = lambda x: np.array([229, 229, 229]) if x == 0 else np.array([26, 26, 26])
    frame_bits = mode.map[mode.d_c:mode.d_c+mode.d_cols, mode.d_r:mode.d_r+mode.d_rows]
    mode.frame = np.array([np.fromiter(map(to_rgb, x), dtype=np.ndarray) for x in frame_bits])
    
    mode.frame[mode.p[0].c - mode.d_c, mode.p[0].r - mode.d_r] = mode.p[0].color

    return mode.frame

width = 800
height = 500

display_cols = 16
display_rows = 10

cell_width = width//display_cols
cell_height = height//display_rows

cell_size = cell_width if cell_width < cell_height else cell_height
# frames_size = cell_size//50
frames_size = 1 
if frames_size < 1: frames_size = 1
frames_color = (0,0,0)

#Menu mode set up
menu_image = pygame.image.load('menu_thumb.png')
menu_map = pygame.surfarray.pixels3d(menu_image)
menu = Mode("Menu", menu_map, menu_logic, frame = menu_map[0:16])

#Maze mode set up
player = Player((1, 1), (255, 0, 0))
map_image = pygame.image.load('maze.png')
maze_map = pygame.surfarray.array2d(map_image)
maze = Mode("Maze", maze_map, maze_logic, players=[player])

#Snake mode set up
player = Player((8, 5), (255, 255, 0))
snake_map = np.zeros((16,10))
snake = Mode("Snake", snake_map, None, players=[player])

mode = maze

pygame.init()
pygame.display.set_caption(mode.name)
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
            
while True:
    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            clicked_cell = pixels2coords(mouse_pos[0], mouse_pos[1], cell_size)
        else: 
            clicked_cell = None

    #Update frame
    frame = mode.logic(mode, [clicked_cell])

    #Draw frame
    for c in range(display_cols):
        for r in range(display_rows):
            x, y = coords2pixels(c,r, cell_size)
            frame_rect = pygame.Rect(x, y, cell_size, cell_size)
            cell = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, frame[c, r], cell)
            pygame.draw.rect(screen, frames_color, frame_rect, frames_size)

    pygame.display.update()
    clock.tick(8)
