class Board:

    def __init__(self):
        rows, cols = (6, 7)
        self.arr = [[0 for i in range(cols)] for j in range(rows)]

    # Prints the board
    def print(self):
        for row in self.arr:
            print(row)

    # Finds the list of all legal moves
    def legal_moves(self):
        moves = []
        col = 0
        row = 5
        while col <= 6:
            while row >= 0:
                if self.arr[row][col] == 0:
                    moves.append((row, col))

                    break
                row = row - 1
            row = 5
            col = col + 1
        return moves

    # Makes a move. Places 1 on the board if it's player 1, -1 if it's player Two.
    # Precondition: Must be a legal move
    def make_a_move(self, move, player):
        moves = self.legal_moves()
        for pos in moves:
            row = pos[0]
            col = pos[1]
            if col == move:
                self.arr[row][col] = player
                new_move = (row,col)
                if self.four_in_a_row(new_move, player) == True:
                    print("You win")


    # Checks if the most recent move makes a four in a row
    def four_in_a_row(self, move, player):
        row = move[0]
        col = move[1]
        depth = 1
        r = row
        c = col
        while r != 0 and self.arr[r-1][c] == player:
            r = r-1
            depth = depth + 1
            if depth == 4:
                return True
        depth = 1
        r = row
        c = col
        while r != 5 and self.arr[r+1][c] == player:
            r = r+1
            depth = depth + 1
            if depth == 4:
                return True
        depth = 1
        r = row
        c = col
        while c != 0 and self.arr[r][c-1] == player:
            c = c-1
            depth = depth + 1
            if depth == 4:
                return True
        depth = 1
        r = row
        c = col
        while c != 6 and self.arr[r][c+1] == player:
            c = c+1
            depth = depth + 1
            if depth == 4:
                return True
        depth = 1
        r = row
        c = col
        while r != 0 and c != 0 and self.arr[r-1][c-1] == player:
            r = r-1
            c = c-1
            depth = depth + 1
            if depth == 4:
                return True
        depth = 1
        r = row
        c = col
        while r != 5 and c != 0 and self.arr[r+1][c-1] == player:
            r = r+1
            c = c-1
            depth = depth + 1
            if depth == 4:
                return True
        depth = 1
        r = row
        c = col
        while r != 0 and c != 6 and self.arr[r-1][c+1] == player:
            r = r-1
            c = c+1
            depth = depth + 1
            if depth == 4:
                return True
        depth = 1
        r = row
        c = col
        while r != 5 and c != 6 and self.arr[r+1][c+1] == player:
            r = r+1
            c = c+1
            depth = depth + 1
            if depth == 4:
                return True
        return False

   # def winning_move(self, move, player):


        # Check in the horizontal direction
 #        print(r)
 #        print(c)
 # #       print(player)
 #        if c >= 3:
 #            print("yes")
 #            if self.arr[r][3] == player and \
 #                    self.arr[r][4] == player and self.arr[r][5] == player and self.arr[r][6] == player:
 #                print("Winner")
 #                return
 #        if c <= 3:
 #            if self.arr[r][0] == player and \
 #                    self.arr[r][1] == player and self.arr[r][2] == player and self.arr[r][3] == player:
 #                print("Winner")
 #                return
 #        # Check in the vertical direction
 #        if r <= 3:
 #            if self.arr[0][c] == player and \
 #                    self.arr[1][c] == player and self.arr[2][c] == player and self.arr[3][c] == player:
 #                return
 #        if r >= 2:
 #            if self.arr[5][c] == player and \
 #                    self.arr[4][c] == player and self.arr[3][c] == player and self.arr[2][c] == player:
 #                print("Winner")
 #                return

        # Check in the diagonal direction

