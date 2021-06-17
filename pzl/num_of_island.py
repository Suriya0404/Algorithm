
class Solution(object):

    def __init__(self):
        self.row = 0
        self.cols = 0

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return -1

        num_island = 0
        self.rows = len(grid)
        self.cols = len(grid[0])

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == '1':
                    print('Outer - row : ' + str(row) + ' col: ' + str(col) + ' Matrix:' + grid[row][col])
                    num_island += self.dfs_sink_island(grid, row, col)

        return num_island

    def dfs_sink_island(self, grid, row, col):

        if row < 0 or col < 0 or row >= self.rows or col >= self.cols or grid[row][col] == '0':
            return 0

        print('\tDFS - row : ' + str(row) + ' col: ' + str(col) + ' Matrix:' + grid[row][col])
        grid[row][col] = '0'

        self.dfs_sink_island(grid, row - 1, col)
        self.dfs_sink_island(grid, row + 1, col)
        self.dfs_sink_island(grid, row, col - 1)
        self.dfs_sink_island(grid, row, col + 1)

        return 1


if __name__ == '__main__':
    # grid = [["1", "1", "1", "1", "0"],
    #         ["1", "1", "0", "1", "0"],
    #         ["1", "1", "0", "0", "0"],
    #         ["0", "0", "0", "0", "0"]]

    grid = [["1", "1", "0", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]

    sol = Solution()
    num_island = sol.numIslands(grid)

    print('Number of island is ' + str(num_island))