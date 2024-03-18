import numpy as np
from utils import *
from maze import *

class Menu(Mode):
    def __init__(self, name, modes, map: np.array, players = None, frame = None, thumbnail = None):
        self.modes = modes
        self.mode = 0

    def logic(self, input):
        point = input[0]
        if point:
            if point[0] > 12:
                self.mode += 1
            elif point[0] < 5:
                self.mode -= 1
            else:
                return self.modes[self.mode].name
        return 0

    def next_frame(self):
        frame = self.modes[self.mode].thumbnail
        return frame

#Menu mode set up
menu = Menu("Menu", modes = [maze], map = None)