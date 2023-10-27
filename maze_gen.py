import numpy as np
import random

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

if __name__ == "__main__":
    width = 15
    height = 15
    maze = generate_maze(15, 15)
    for y in range(height):
            for x in range(width):
                print(chr(9608) if maze[x,y] == 1 else ' ', end='')
            print()
