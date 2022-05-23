import heapq
from MapGen import Grids
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


class Algorithm:

    def __init__(self):
        self.g = Grids()
        self.placedShapes = self.g.placedShapes
        self.rc = self.g.rc
        self.planeSize = self.g.sizePlane
        self.map = None
        self.path = []

    def hValue(self, x, y):
        return abs(x[0] - y[0]) + abs((x[1] - y[1]))

    def createPath(self, parent, node, grid):
        while parent[node] is not None:
            self.path.append(node)
            node = parent[node]
        self.path.append(node)
        self.path.reverse()
        return self.path

    def astar(self, grid, start, goal):
        epsilon = 1  # when epsilon = 0, it is A*, the path is optimal when epsilon > 0, it is epsilon-A*
        closedList = set()
        openList = [(0, start)]
        heapq.heapify(openList)
        dist = {start: 0}
        parent = {start: None}

        cnt = 0
        self.map = np.ones([self.g.sizePlane, self.g.sizePlane, 3]) * 0.5

        img_idx = 0
        while openList:
            p, curnode = heapq.heappop(openList)

            self.map[curnode[0], curnode[1], 0] = 1.
            self.map[curnode[0], curnode[1], 1] = .5
            if cnt % 10 == 0:
                plt.imshow(self.map)
                plt.axis('off')
                plt.tight_layout()
                plt.savefig(f'./img/{img_idx}.png')
                img_idx += 1
                plt.pause(.00001)

            closedList.add(curnode)
            if curnode == goal:
                break
            for n, cost in self.g.getNeighbors(curnode):
                if n not in closedList:
                    if n not in dist or dist[n] > dist[curnode] + cost:
                        dist[n] = dist[curnode] + cost
                        heapq.heappush(openList, (dist[n] + epsilon * self.hValue(n, goal), n))
                        parent[n] = curnode
                        self.map[n[0], n[1], 1] = 1.
            cnt += 1

        path = self.createPath(parent, curnode, grid)
        solution = grid
        for x, y in path:
            solution[x][y] = 255, 0, 0
        img = Image.fromarray(solution, 'RGB')
        img.show()

    def main(self):
        grid = self.g.getGrid(1)
        start = (0, 0)
        goal = (len(grid)-1, len(grid)-1)
        goalVal = grid[len(grid)-1][len(grid)-1]

        if goalVal[0] == 0 & goalVal[1] == 0 & goalVal[2] == 0:
            self.astar(grid, start, goal)
        else:
            print("Error, goal is blocked")
            exit(0)

