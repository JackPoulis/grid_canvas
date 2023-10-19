import pygame
import numpy as np
import random
from sys import exit

class Level():
    def __init__(self, map: np.array):
        self.map = map
        self.x = map.shape[0]
        self.y = map.shape[1]

class Display():
    def __init__(self, columns, rows, background=(0,0,0), frames_color = (255,255,255), position = (0,0), cell_size = 50, frames_size = 5):
        self.cell = np.full((columns, rows, 3), (0,0,0), dtype=tuple)
        self.columns = columns
        self.rows = rows
        self.background = background
        self.frames_color = frames_color
        self.position = position
        self.cell_size = cell_size
        self.frames_size = frames_size

def cell_position(c,r,buffer):
    x = c*buffer
    y = r*buffer
    return (x,y)

def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))

game_name = "LED grid"

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

player_c = 4
player_r = 5
player_color = (255, 0, 0)

map = pygame.image.load('maze.png')
map_bitarray = pygame.surfarray.array2d(map)
level = Level(map_bitarray)
display = Display(display_cols, display_rows, cell_size = cell_size, frames_size = frames_size,  frames_color = (0,0,0))

pygame.init()
pygame.display.set_caption(game_name)
# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
            
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and level.map[player_c, player_r - 1] == 1:
        player_r -= 1
    if keys[pygame.K_s] and level.map[player_c, player_r + 1] == 1:
        player_r += 1
    if keys[pygame.K_a] and level.map[player_c - 1, player_r] == 1:
        player_c -= 1
    if keys[pygame.K_d] and level.map[player_c + 1, player_r] == 1:
        player_c += 1

    for c in range(display.columns):
        for r in range(display.rows):
            pos = cell_position(c,r,display.cell_size)
            x, y = pos[0], pos[1]
            frame_rect = pygame.Rect(x, y, display.cell_size, display.cell_size)
            cell = pygame.Rect(x, y, display.cell_size, display.cell_size)
            cell_color = "gray90" if level.map[c + display.position[0], r + display.position[1]] == 0 else "gray5"
            pygame.draw.rect(screen, cell_color, cell)
            pygame.draw.rect(screen, display.frames_color, frame_rect, display.frames_size)

    player_x, player_y = cell_position(player_c,player_r,display.cell_size)
    player_rect = pygame.Rect(player_x, player_y, display.cell_size, display.cell_size)
    pygame.draw.rect(screen, player_color, player_rect)

    pygame.display.update()
    clock.tick(30)