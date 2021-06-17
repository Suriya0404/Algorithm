
# Input:
# x x - - x x
# x - - - x x
# - - - x - -
#
# Output:
# x x - - x x
# x x - x - x
# - - - - x -


# - If an alive cell has fewer than 2 alive neighbors (orthogonally or diagonally adjacent), the cell dies of isolation.
# - If an alive cell has more than 3 alive neighbors, the cell dies of overcrowding.
# - If a dead cell has exactly 3 alive neighbors, the cell becomes alive.
# - All other cells stay in the same state.


class GameOfLife(object):
    def __init__(self, mat):
        self.row = len(mat)
        self.col = len(mat[0])
        self.mat = mat

    def _is_valid_state(self, cell_row, cell_col):
        return (0 <= cell_row < self.row) and (0 <= cell_col < self.col)

    def _next_state(self, curr_row, curr_col):
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        alive_count = 0
        curr_val = self.mat[curr_row][curr_col]

        for row, col in neighbors:
            nbr_row = curr_row + row
            nbr_col = curr_col + col
            if self._is_valid_state(nbr_row, nbr_col):
                alive_count += self.mat[nbr_row][nbr_col]

        if curr_val == 1:
            return 1 if alive_count in (2, 3) else 0
        else:
            return 1 if alive_count == 3 else 0

    def get_result(self):
        new_board = []
        for row in range(self.row):
            new_row = []
            for col in range(self.col):
                new_row.append(self._next_state(row, col))

            new_board.append(new_row)
        return new_board

    # Handling large files
    def read_three_lines(self):
        # read three lines from file
        # Use generator and return list of numbers
        # call the next state
        pass



if __name__ == '__main__':

    test_input = [[1, 1, 0, 0, 1, 1],
                  [1, 0, 0, 0, 1, 1],
                  [0, 0, 0, 1, 0, 0]]

    gol = GameOfLife(test_input)
    result = gol.get_result()
    print(result)
