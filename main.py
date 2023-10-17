import pygame
import numpy as np
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

game_name = "LED grid"

width = 1000
height = 1000

columns = 16
rows = 16

cell_width = width//columns
cell_height = height//rows

cell_size = cell_width if cell_width < cell_height else cell_height

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
    
    pygame.display.update()
    clock.tick(60)