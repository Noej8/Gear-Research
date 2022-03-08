import heapq
import numpy as np
import matplotlib as plt
from grids import Grids


class Grid():

    def __init__(self):
        self.g = Grids()

    def getGrid(self):
        grids = self.g.createGrid()
        return grids

    def getGridLength(self):
        grid = self.getGrid()
        length = len(grid)
        return length

    def getGridWidth(self):
        grid = self.getGrid()
        width = len(grid[0])
        return width

    def getNeighbors(self, current):
        neighbors = []
        x, y = current
        for nx, ny in [[x, y+1], [x, y-1], [x+1, y], [x-1, y], [x-1, y+1], [x+1, y-1], [x+1, y+1], [x-1, y-1]]:
            if isInRange(nx, ny) and unBlocked(nx, ny):
                neighbors.append([(nx, ny), 1])
        return neighbors


def isInRange(row, col):
    if (row < g.getGridLength()) and (row >= 0) and (col < g.getGridWidth()) and (col >= 0):
        return True
    else:
        return False


def unBlocked(row, col):
    grid = g.getGrid()
    if grid[row][col] == 0:
        return True
    else:
        return False


def hValue(x, y):
    return abs(x[0] - y[0]) + abs((x[1] - y[1]))


def createPath(parent, node):
    path = []
    while parent[node] is not None:
        path.append(node)
        node = parent[node]
    path.append(node)
    path.reverse()
    return path

def astar(grid, start, goal):
    epsilon = 1
    closedList = set()
    openList = [(0, start)]
    heapq.heapify(openList)
    dist = {start: 0}
    parent = {start: None}

    while openList:
        p, curnode = heapq.heappop(openList)
        closedList.add(curnode)
        if curnode == goal:
            break
        for n, cost in g.getNeighbors(curnode):
            if n not in closedList:
                if n not in dist or dist[n] > dist[curnode] + cost:
                    dist[n] = dist[curnode] + cost
                    heapq.heappush(openList, (dist[n] + epsilon * hValue(n, goal), n))
                    parent[n] = curnode

    path = createPath(parent, curnode)
    solution = grid
    for x, y in path:
        solution[x][y] = 2
    print(solution)

g = Grid()
start = (0,0)
goal = (14,14)
astar(g.getGrid(), start, goal)
