import pygame
from sys import exit

game_name = "LED grid"
width = 1000
height = 1000

pygame.init()
pygame.display.set_caption(game_name)
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)