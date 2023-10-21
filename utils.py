import numpy as np

class Display():
    def __init__(self, columns, rows, position = (0,0), map_size = (32, 32), wall = 3):
        self.cols = columns
        self.rows = rows
        self.c = position[0]
        self.r = position[1]
        self.wall = wall
        self.map_size = map_size

    def update_pos(self, p_x, p_y):
        if p_x > self.cols/4*3 and self.c < self.map_size[0] - 1:
            self.c += 1
        elif p_x < self.cols/4 and self.c > 0:
            self.c -= 1

        if p_y > self.rows/4*3 and self.r < self.map_size[1] - 1:
            self.r += 1
        elif p_y < self.rows/4 and self.r > 0:
            self.r -= 1

class Player():
    def __init__(self, position = (0,0), color = (0,0,255)):
        self.c = position[0]
        self.r = position[1]
        self.color = color

class Mode():
    def __init__(self, name, map: np.array, display, logic, players = None, frame = None):
        self.name = name
        self.map = map
        self.cols = map.shape[0]
        self.rows = map.shape[1]
        self.p = players
        self.logic = logic
        self.display = display
        self.frame = frame 

def coords2pixels(c,r,buffer):
    x = c*buffer
    y = r*buffer
    return (x,y)

def pixels2coords(x,y,buffer):
    c = x//buffer
    r = y//buffer
    return (c,r)
