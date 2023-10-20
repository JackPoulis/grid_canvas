import numpy as np

class Display():
    def __init__(self, columns, rows, position = (0,0), map_size = (32, 32), wall = 3):
        self.columns = columns
        self.rows = rows
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
