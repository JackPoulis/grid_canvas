import numpy as np

class Player():
    def __init__(self, position = (0,0), color = (0,0,255)):
        self.c = position[0]
        self.r = position[1]
        self.color = color

class Object():
    obj_id = 0
    def __init__(self, name, position, color = (128,0,128)) -> None:
        self.name = name
        self.id = Object.obj_id
        Object.obj_id += 1
        self.x, self.y = position
        self.color = color

class Mode():
    def __init__(self, name, map, players = None, objects = None, thumbnail = None):
        self.name = name
        self.map = map
        self.cols = map.shape[0]
        self.rows = map.shape[1]
        self.p = players
        self.objects = {}
        if objects:
            for obj in objects:
                self.objects[obj.name] = obj
        self.d_cols = 16
        self.d_rows = 10
        self.d_c = 0
        self.d_r = 0
        self.thumbnail = thumbnail

    #Overwrite
    def logic(self, input):
        #template
        # if input[0]:
        #     x, y = input[0]
        return 0
    
    #Overwrite
    def next_frame(self) -> np.array:
        frame = np.full((self.cols, self.rows), (0,0,0))
        return frame
    
def coords2pixels(c,r,buffer):
    x = c*buffer
    y = r*buffer
    return (x,y)

def pixels2coords(x,y,buffer):
    c = x//buffer
    r = y//buffer
    return (c,r)
