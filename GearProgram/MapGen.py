import numpy as np
import random

class Grids():
    def __init__(self):
        self.grid = None
        self.grid_collid = None
        self.planes = [20, 30, 40, 50, 60]
        self.boxes = [1, 2, 3, 4, 5]
        self.placedShapes = []
        self.rc = []
        self.sizePlane = 0
        self.grids = []

    def placeObstacle(self, row, col, grid):
        sizeOb = random.choice(self.boxes)
        row_min = row - 1
        row_max = min(len(grid), row + sizeOb - 1)
        col_min = col - 1
        col_max = min(len(grid), col + sizeOb - 1)
        grid[row_min:row_max, col_min:col_max] = np.array([128, 0, 128])
        self.placedShapes.append(sizeOb)

    def placeObstacleDef(self, row, col, size):
        sizeOb = size
        row_min = row - int(sizeOb/2)
        row_max = min(len(self.grid), row_min + sizeOb - 1)
        col_min = col - int(size/2)
        col_max = min(len(self.grid), col_min + sizeOb - 1)
        self.grid[row_min:row_max, col_min:col_max] = np.array([128, 0, 128])
        self.placedShapes.append(sizeOb)

        sizeOb_collid = size + 2
        row_min = row - int(sizeOb_collid / 2)
        row_max = min(len(self.grid_collid), row_min + sizeOb_collid - 1)
        col_min = col - int(sizeOb_collid / 2)
        col_max = min(len(self.grid_collid), col_min + sizeOb_collid - 1)
        self.grid_collid[row_min:row_max, col_min:col_max] = np.array([128, 0, 128])

    def randomGrid(self):
        self.sizePlane = random.choice(self.planes)
        self.grid = np.zeros((self.sizePlane, self.sizePlane,3), dtype=np.uint8)
        obstacles = self.sizePlane/5
        numObstacles = random.randint(5, int(obstacles) + 5)
        for x in range(numObstacles):
            col = random.randint(0, self.sizePlane)
            row = random.randint(0, self.sizePlane)
            self.rc.append([col, row])
            self.placeObstacle(col, row, self.grid)
        return self.grid

    def definiteGrid(self):
        self.sizePlane = 30
        self.grid = np.zeros((self.sizePlane, self.sizePlane, 3), dtype=np.uint8)
        self.grid_collid = np.zeros((self.sizePlane, self.sizePlane, 3), dtype=np.uint8)
        self.placeObstacleDef(7, 5, 5)
        self.placeObstacleDef(10, 15, 7)
        self.placeObstacleDef(26, 22, 5)
        self.rc.append([5, 7])
        self.rc.append([15, 10])
        self.rc.append([22, 26])
        return self.grid

    def getGrid(self, x):
        if x == 0:
            self.grids = self.randomGrid()
        else:
            self.grids = self.definiteGrid()
        return self.grids

    def getGridLength(self):
        length = len(self.grids)
        return length

    def getGridWidth(self):
        width = len(self.grids[0])
        return width

    def getNeighbors(self, current):
        neighbors = []
        x, y = current
        for nx, ny in [[x, y+1], [x, y-1], [x+1, y], [x-1, y], [x-1, y+1], [x+1, y-1], [x+1, y+1], [x-1, y-1]]:
            if self.isInRange(nx, ny) and self.unBlocked(nx, ny):
                neighbors.append([(nx, ny), ((nx - x) ** 2 + (ny - y) ** 2) ** 0.5])
        return neighbors

    def isInRange(self, row, col):
        if (row < self.getGridLength()) and (row >= 0) and (col < self.getGridWidth()) and (col >= 0):
            return True
        else:
            return False

    def unBlocked(self, row, col):
        if self.grid_collid[row][col][0] == 0:
            return True
        else:
            return False
