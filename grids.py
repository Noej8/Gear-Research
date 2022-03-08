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
        return grid

    def inputGrid(self):
        length = input("Input length: ")
        width = input("Input width: ")
        grid1 = np.zeros((int(length), int(width)))
        return grid1

    def placeObstacle(self, row, col, grid):
        sizeOb = randint(1,3)
        r = row
        c = col
        for x in range(sizeOb*2):
            grid[r][c] = 1
            r = row+1


    def randomGrid(self):
        size = randint(0, 20)
        self.grid = np.zeros((size, size))
        obstacles = (2*size/5)
        numObstacles = randint(1, int(obstacles))
        print(numObstacles)
        for x in range(numObstacles):
            col = randint(0,size)
            row = randint(0, size)
            placeObstacles(row, col, self.grid)


        return self.grid

g = Grids()
grid = g.randomGrid()
print(grid)

