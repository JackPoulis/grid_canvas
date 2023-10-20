import pygame
import numpy as np
import random
from sys import exit

class Game():
    def __init__(self, name, map: np.array):
        self.name = name
        self.map = map
        self.x = map.shape[0]
        self.y = map.shape[1]

class Display():
    def __init__(self, columns, rows, background=(0,0,0), position = (0,0), map_size = (32, 32), wall = 3):
        self.cell = np.full((columns, rows, 3), (0,0,0), dtype=tuple)
        self.columns = columns
        self.rows = rows
        self.background = background
        self.c = position[0]
        self.r = position[1]
        self.wall = wall
        self.map_size = map_size

    def update_pos(self, player_x, player_y):
        if (self.c + self.columns - self.wall - 1) < player_x:
            self.c = player_x - self.columns + self.wall + 1
            if self.c + self.columns > self.map_size[0]: self.c = self.map_size[0] - self.columns
        if (self.c + self.wall) > player_x:
            self.c = player_x - self.wall
            if self.c < 0: self.c = 0
        if (self.r + self.rows - self.wall - 1) < player_y:
            self.r = player_y - self.rows + self.wall + 1 
            if self.r + self.rows > self.map_size[1]: self.r = self.map_size[1] - self.rows
        if (self.r + self.wall) > player_y:
            self.r = player_y - self.wall
            if self.r < 0: self.r = 0

def coords2pixels(c,r,buffer):
    x = c*buffer
    y = r*buffer
    return (x,y)

def pixels2coords(x,y,buffer):
    c = x//buffer
    r = y//buffer
    return (c,r)

# def random_color():
#     levels = range(32,256,32)
#     return tuple(random.choice(levels) for _ in range(3))

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
frames_color = (0,0,0)

player_c = 3
player_r = 5
player_color = (128, 0, 0)
player_move = "idle"

map = pygame.image.load('maze.png')
map_bitarray = pygame.surfarray.array2d(map)
level = Level(map_bitarray)
display = Display(display_cols, display_rows)

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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            clicked_cell = pixels2coords(mouse_pos[0], mouse_pos[1], cell_size)
        else: 
            clicked_cell = None

    player_dc = player_c - display.c
    player_dr = player_r - display.r
    if clicked_cell:
        if clicked_cell[1] == player_dr:
            if clicked_cell[0] < player_dc:
                player_move = "left"
            elif clicked_cell[0] > player_dc:
                player_move = "right"
        if clicked_cell[0] == player_dc:
            if clicked_cell[1] < player_dr:
                player_move = "up"
            elif clicked_cell[1] > player_dr:
                player_move = "down"
    else:
        player_move = "idle"

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or player_move == "up") and level.map[player_c, player_r - 1] == 1:
        player_r -= 1
    if (keys[pygame.K_s] or player_move == "down") and level.map[player_c, player_r + 1] == 1:
        player_r += 1
    if (keys[pygame.K_a] or player_move == "left") and level.map[player_c - 1, player_r] == 1:
        player_c -= 1
    if (keys[pygame.K_d] or player_move == "right") and level.map[player_c + 1, player_r] == 1:
        player_c += 1
    display.update_pos(player_c, player_r)

    for c in range(display.columns):
        for r in range(display.rows):
            pos = coords2pixels(c,r, cell_size)
            x, y = pos[0], pos[1]
            frame_rect = pygame.Rect(x, y, cell_size, cell_size)
            cell = pygame.Rect(x, y, cell_size, cell_size)
            cell_color = "gray90" if level.map[c + display.c, r + display.r] == 0 else "gray5"
            pygame.draw.rect(screen, cell_color, cell)
            pygame.draw.rect(screen, frames_color, frame_rect, frames_size)

    player_x, player_y = coords2pixels(player_c - display.c,player_r - display.r, cell_size)
    player_rect = pygame.Rect(player_x, player_y, cell_size, cell_size)
    pygame.draw.rect(screen, player_color, player_rect)

    pygame.display.update()
    clock.tick(16)