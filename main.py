import pygame
import numpy as np
from sys import exit

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

class Player():
    def __init__(self, position = (0,0), color = (0,0,255)):
        self.c = position[0]
        self.r = position[1]
        self.color = color

class Mode():
    def __init__(self, name, map: np.array, display, logic, players = None):
        self.name = name
        self.map = map
        self.cols = map.shape[0]
        self.rows = map.shape[1]
        self.p = players
        self.logic = logic
        self.display = display
        self.frame = np.full((display.columns, display.rows, 3), (0,0,0))

def maze_logic(mode, input):
    point = input[0]
    player_dc = mode.p[0].c - mode.display.c
    player_dr = mode.p[0].r - mode.display.r
    p_c = mode.p[0].c
    p_r = mode.p[0].r
    if point:
        if point[1] == player_dr:
            if point[0] < player_dc and mode.map[p_c - 1, p_r] == 1:
                mode.p[0].c -= 1
            elif point[0] > player_dc and mode.map[p_c + 1, p_r] == 1:
                mode.p[0].c += 1
        if point[0] == player_dc:
            if point[1] < player_dr and mode.map[p_c, p_r - 1] == 1:
                mode.p[0].r -= 1
            elif point[1] > player_dr and mode.map[p_c, p_r + 1] == 1:
                mode.p[0].r += 1

    mode.display.update_pos(mode.p[0].c, mode.p[0].r)

    for c in range(mode.display.columns):
        for r in range(mode.display.rows):
            mode.frame[c, r] = (26, 26, 26) if mode.map[c + mode.display.c, r + mode.display.r] == 0 else (229, 229, 229)
    
    mode.frame[mode.p[0].c - mode.display.c, mode.p[0].r - mode.display.r] = (255,0,0)

    return mode.frame

def coords2pixels(c,r,buffer):
    x = c*buffer
    y = r*buffer
    return (x,y)

def pixels2coords(x,y,buffer):
    c = x//buffer
    r = y//buffer
    return (c,r)

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

display = Display(display_cols, display_rows)
#Menu mode set up
menu_map = np.zeros((16,10))
menu = Mode("Menu", menu_map, display, None)

#Maze mode set up
player = Player((1, 1), (200, 0, 0))
map_image = pygame.image.load('maze.png')
maze_map = pygame.surfarray.array2d(map_image)
maze = Mode("Maze", maze_map, display, maze_logic, players=[player])

#Snake mode set up
player = Player((8, 5), (255, 255, 0))
snake_map = np.zeros((16,10))
snake = Mode("Snake", snake_map, display, None, players=[player])

mode = maze

pygame.init()
pygame.display.set_caption(mode.name)
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
            
while True:
    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            clicked_cell = pixels2coords(mouse_pos[0], mouse_pos[1], cell_size)
        else: 
            clicked_cell = None

    frame = mode.logic(mode, [clicked_cell])

    for c in range(display_cols):
        for r in range(display_rows):
            x, y = coords2pixels(c,r, cell_size)
            frame_rect = pygame.Rect(x, y, cell_size, cell_size)
            cell = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, frame[c, r], cell)
            pygame.draw.rect(screen, frames_color, frame_rect, frames_size)

    pygame.display.update()
    clock.tick(8)
