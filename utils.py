import numpy as np

class Player():
    def __init__(self, position = (0,0), color = (0,0,255)):
        self.c = position[0]
        self.r = position[1]
        self.color = color

class Mode():
    def __init__(self, name, map: np.array, players = None, frame = None, thumbnail = None, f_logic = None):
        self.name = name
        self.map = map
        self.cols = map.shape[0]
        self.rows = map.shape[1]
        self.p = players
        self.frame = frame 
        self.frame_logic = f_logic
        self.d_cols = 16
        self.d_rows = 10
        self.d_c = 0
        self.d_r = 0
        self.thumbnail = thumbnail
        self.mode = 0

    def logic(input):
        if input[0]:
            x, y = input[0]
            output = 0
        return output
    
    def next_frame():
        pass
    
def coords2pixels(c,r,buffer):
    x = c*buffer
    y = r*buffer
    return (x,y)

def pixels2coords(x,y,buffer):
    c = x//buffer
    r = y//buffer
    return (c,r)
