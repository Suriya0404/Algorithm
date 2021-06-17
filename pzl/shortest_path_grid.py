
from collections import OrderedDict

class GridShortestPath:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.seen = {}

    def shortest_path(self, grid):

        if len(grid) == 0:
            return -1

        self.rows = len(grid)
        self.cols = len(grid[0])

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 'S':
                    return self.bfs_grid(grid, row, col)

    def bfs_grid(self, grid, row, col):

        steps = OrderedDict()
        steps[(row, col)] = 0

        for row, col in steps:

            left = None
            right = None
            top = None
            bottom = None

            if grid[row][col] == 'E':
                return steps[(row, col)]

            if row - 1 >= 0:
                left = (row - 1, col)
            if row + 1 < self.rows:
                right = (row + 1, col)
            if col - 1 >= 0:
                top = (row, col - 1)
            if col + 1 < self.cols:
                bottom = (row, col + 1)

            if left and left not in steps and grid[row - 1][col] != '#':
                steps[left] = steps[(row, col)] + 1
            if right and right not in steps and grid[row + 1][col] != '#':
                steps[right] = steps[(row, col)] + 1
            if top and top not in steps and grid[row][col - 1] != '#':
                steps[top] = steps[(row, col)] + 1
            if bottom and bottom not in steps and grid[row][col + 1] != '#':
                steps[bottom] = steps[(row, col)] + 1


if __name__ == '__main__':

    grid = [["S", ".", ".", "#", ".", ".", "."],
            [".", "#", ".", ".", ".", "#", "."],
            [".", "#", ".", ".", ".", ".", "."],
            [".", ".", "#", "#", ".", ".", "."],
            ["#", ".", "#", "E", ".", "#", "."]]


    sol = GridShortestPath()
    print(sol.shortest_path(grid))
