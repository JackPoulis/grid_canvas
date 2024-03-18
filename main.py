import pygame
import numpy as np
from sys import exit
from utils import *
from maze_gen import *
from menu import *
from maze import *

width = 800
height = 500

display_cols = 16
display_rows = 10

cell_width = width//display_cols
cell_height = height//display_rows

cell_size = cell_width if cell_width < cell_height else cell_height
frames_size = 1 
frames_color = (0,0,0)

mode = menu
output = None

pygame.init()
pygame.display.set_caption("Grid display")
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#Main loop         
while True:
    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            mode = menu
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            clicked_cell = pixels2coords(mouse_pos[0], mouse_pos[1], cell_size)
        else: 
            clicked_cell = None

    #Next frame logic
    output = mode.logic([clicked_cell])
    frame = mode.next_frame()
    if output:
        if output == "Exit":
            print("Mode exited")
            mode = menu
        elif output == "Maze":
            mode = maze

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
