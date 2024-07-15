import numpy as np
from utils import *
from maze_gen import *

def maze_logic(mode: Mode, input):
    p_c = mode.p[0].c #player column on the grid
    p_r = mode.p[0].r #player row on the grid
    p_dc = p_c - mode.d_c #player column on the displayed grid
    p_dr = p_r - mode.d_r #player row on the displayed grid
    if input[0]:
        x, y = input[0] #The clicked cell's x,y coordinates
        if y == p_dr:
            if x < p_dc and mode.map[p_c - 1, p_r] == 0:
                mode.p[0].c -= 1
                if mode.p[0].c - mode.d_c < mode.d_cols/4 and mode.d_c > 0:
                    mode.d_c -= 1
            elif x > p_dc and mode.map[p_c + 1, p_r] == 0:
                mode.p[0].c += 1
                if mode.p[0].c - mode.d_c > mode.d_cols/4*3 and mode.d_c < mode.cols - 1:
                    mode.d_c += 1
        if x == p_dc:
            if y < p_dr and mode.map[p_c, p_r - 1] == 0:
                mode.p[0].r -= 1
                if mode.p[0].r - mode.d_r < mode.d_rows/4 and mode.d_r > 0:
                    mode.d_r -= 1
            elif y > p_dr and mode.map[p_c, p_r + 1] == 0:
                mode.p[0].r += 1
                if mode.p[0].r - mode.d_r > mode.d_rows/4*3 and mode.d_r < mode.rows - 1:
                    mode.d_r += 1
    
    to_rgb = lambda x: np.array([229, 229, 229]) if x == 0 else np.array([26, 26, 26])
    frame_bits = mode.map[mode.d_c:mode.d_c+mode.d_cols, mode.d_r:mode.d_r+mode.d_rows]
    mode.frame = np.array([np.fromiter(map(to_rgb, x), dtype=np.ndarray) for x in frame_bits])
    
    mode.frame[mode.p[0].c - mode.d_c, mode.p[0].r - mode.d_r] = mode.p[0].color

    return mode.frame

#Maze mode set up
maze_player = Player((1, 1), (255, 0, 0))
# map_image = pygame.image.load('maze.png')
# maze_map = pygame.surfarray.array2d(map_image)
maze_map = generate_maze(31,31)
maze = Mode("Maze", maze_map, maze_logic, players=[maze_player])
