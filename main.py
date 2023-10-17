import pygame
import numpy as np
import random
from sys import exit

class Grid():
    def __init__(self, columns, rows, background=(0,0,0)):
        self.cell = np.array(columns, rows, 0)
        self.columns = columns
        self.rows = rows
        self.background = background

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

columns = 16
rows = 10

cell_width = width//columns
cell_height = height//rows

cell_size = cell_width if cell_width < cell_height else cell_height
border_size = cell_size//30

pygame.init()
pygame.display.set_caption(game_name)
# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

for r in range(rows):
        for c in range(columns):
            pos = cell_position(c,r,cell_size)
            rect = pygame.Rect(pos[0], pos[1], cell_size, cell_size)
            pygame.draw.rect(screen, "Gray", rect, border_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(60)