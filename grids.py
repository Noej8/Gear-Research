import numpy as np
from random import randint

class Grids():
    def __init__(self):
        self.grid = 0

    def createGrid(self):
        grid = np.array([
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]])
        row = 12
        col = 6
        sizeOb = 3
        for x in range(row-1, row+(sizeOb-1)):
            for y in range(col-1, col+(sizeOb-1)):
                if x < len(grid):
                    grid[x][y] = 1
        #for y in range(col-1, col+(sizeOb-1)):
            #if y < len(grid):
                #grid[row][y] = 1
        return grid

    def inputGrid(self):
        length = input("Input length: ")
        width = input("Input width: ")
        grid1 = np.zeros((int(length), int(width)))
        return grid1

    def placeObstacle(self, row, col, grid):
        sizeOb = randint(10, 40)
        row_min = row - 1
        row_max = min(len(grid), row + sizeOb - 1)
        col_min = col - 1
        col_max = min(len(grid), col + sizeOb - 1)
        grid[row_min:row_max, col_min:col_max] = np.array([128, 0, 128])


    def randomGrid(self):
        size = randint(5, 20)
        self.grid = np.zeros((size, size))
        obstacles = (2*size/5)
        numObstacles = randint(1, int(obstacles))
        print(numObstacles)
        for x in range(numObstacles):
            col = randint(0,size)
            row = randint(0, size)
            self.placeObstacle(row, col, self.grid)
        return self.grid

g = Grids()
grid = g.randomGrid()
print(grid)

