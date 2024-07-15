import numpy as np
from utils import *
import pygame
import random

class Maze(Mode):

    def __init__(self, name, map, players, objects, thumbnail):
        super().__init__(name, map, players = players, objects = objects, thumbnail = thumbnail)

    def logic(self, input):
        p_c = self.p[0].c
        p_r = self.p[0].r
        p_dc = p_c - self.d_c
        p_dr = p_r - self.d_r
        if input[0]:
            x, y = input[0]
            if y == p_dr:
                if x < p_dc and self.map[p_c - 1, p_r] == 0:
                    self.p[0].c -= 1
                    if self.p[0].c - self.d_c < self.d_cols//4 and self.d_c > 0:
                        self.d_c -= 1
                elif x > p_dc and self.map[p_c + 1, p_r] == 0:
                    self.p[0].c += 1
                    if self.p[0].c - self.d_c > self.d_cols//4*3 and self.d_c < self.cols - 1:
                        self.d_c += 1
            if x == p_dc:
                if y < p_dr and self.map[p_c, p_r - 1] == 0:
                    self.p[0].r -= 1
                    if self.p[0].r - self.d_r < self.d_rows//4 and self.d_r > 0:
                        self.d_r -= 1
                elif y > p_dr and self.map[p_c, p_r + 1] == 0:
                    self.p[0].r += 1
                    if self.p[0].r - self.d_r > self.d_rows//4*3 and self.d_r < self.rows - 1:
                        self.d_r += 1
        return None

    def next_frame(self):
        to_rgb = lambda x: np.array([229, 229, 229]) if x == 0 else np.array([26, 26, 26])
        frame_bits = self.map[self.d_c:self.d_c+self.d_cols, self.d_r:self.d_r+self.d_rows]
        frame = np.array([np.fromiter(map(to_rgb, x), dtype=np.ndarray) for x in frame_bits])
        end = self.objects["end"]
        player = self.p[0]
        frame[end.x - self.d_c, end.y - self.d_r] = end.color      
        frame[player.c - self.d_c, player.r - self.d_r] = player.color
        
        return frame

def generate_maze(width,height):
    maze = np.full((width, height), 1)

    def visit(x, y):
        maze[x, y] = 0

        while True:
            unvisited_neighbors = []
            if y > 1 and (x, y - 2) not in visited:
                unvisited_neighbors.append((x, y - 2))

            if y < height - 2 and (x, y + 2) not in visited:
                unvisited_neighbors.append((x, y + 2))

            if x > 1 and (x - 2, y) not in visited:
                unvisited_neighbors.append((x - 2, y))

            if x < width - 2 and (x + 2, y) not in visited:
                unvisited_neighbors.append((x + 2, y))

            if len(unvisited_neighbors) == 0:
                return
            else:
                next = random.choice(unvisited_neighbors)
                maze[(next[0]+x)//2,(next[1]+y)//2] = 0

                visited.append(next)
                visit(next[0],next[1])
                
    visited = [(1,1)]
    visit(1,1)
    return maze

#Maze mode set up
maze_player = Player((1, 1), (255, 0, 0))
maze_end = Object("end", (3, 3), (0, 255, 0))
maze_thumbnail_image = pygame.image.load('thumbnails/maze.png')
maze_thumbnail = pygame.surfarray.array3d(maze_thumbnail_image)
maze_map = generate_maze(31,31)
maze = Maze("Maze", maze_map, players=[maze_player], objects = [maze_end], thumbnail=maze_thumbnail)

if __name__ == "__main__":
    width = 51   
    height = 51
    maze = generate_maze(width, height)
    for y in range(height):
            for x in range(width):
                print(chr(9608) if maze[x,y] == 1 else ' ', end='')
            print()
