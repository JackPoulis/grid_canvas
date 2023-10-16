import pygame
from sys import exit

game_name = "LED grid"
width = 1000
height = 1000

pygame.init()
pygame.display.set_caption(game_name)
screen = pygame.display.set_mode((width,height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    pygame.display.update()