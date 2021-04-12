class Board:


    def __init__(self):
        rows, cols = (6, 7)
        self.arr = [[0 for i in range(cols)] for j in range(rows)]
        self.moves_played = 0

    # Prints the board
    def print(self):
        for row in self.arr:
            print(row)

    def get_board(self):
        return self.arr

    def set_board(self, row, col, ply):
        self.arr[row][col] = ply
        self.moves_played += 1

    def get_moves_played(self):
        return self.moves_played

    # Finds the list of all legal moves



        # Check in the diagonal direction

