import numpy as np
from utils import *

def snake_logic(mode: Mode, input):
    mode.frame = np.zeros((16,10))
    return mode.frame

#Snake mode set up
snake_player = Player((8, 5), (255, 255, 0))
snake_map = np.zeros((16,10))
snake = Mode("Snake", snake_map, snake_logic, players=[snake_player])

