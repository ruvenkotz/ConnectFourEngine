def legal_moves(board):
    moves = []
    col = 0
    row = 5
    while col <= 6:
        while row >= 0:
            if board[row][col] == 0:
                moves.append((row, col))

                break
            row = row - 1
        row = 5
        col = col + 1
    return moves


def moves_played(board):
    moves = 0
    for row in range(0, 6):
        for col in range(0, 7):
            if board[row][col] == 1:
                moves += 1
    return moves

def player_spots(board, player):
    moves = []
    for row in range(0, 6):
        for col in range(0, 7):
            if board[row][col] == player:
                moves.append((row, col))
    return moves


# Makes a move. Places 1 on the board if it's player 1, -1 if it's player Two.
# Precondition: Must be a legal move
def make_a_move(board, move, player):
    moves = legal_moves()
    for pos in moves:
        row = pos[0]
        col = pos[1]
        if col == move:
            board[row][col] = player
            new_move = (row, col)
    #  if self.four_in_a_row(new_move, player) == True:
    #      print("You win")

# Checks if the most recent move makes a four in a row
#needs work, glitches in the vertical four in the row
def four_in_a_row2(board, r, c, player):
    #right
    try:
        if board[r][c+1] == player and board[r][c+2] == player and (board[r][c+3] == player or board[r][c-1] == player):
            return True
    except:
        pass

        # left
    try:
        if board[r][c - 1] == player and board[r][c - 2] == player and (board[r][c - 3] == player or board[r][c+1] == player):
            print(board[r][c])
            return True
    except:
        pass

    # bottom
    try:
        if board[r-1][c] == player and board[r-2][c] == player and (board[r-3][c] == player or board[r+1][c] == player):
            return True
    except:
        pass

    # top
    try:
        if board[r + 1][c] == player and board[r + 2][c] == player and (board[r + 3][c] == player or board[r-1][c] == player):
            return True
    except:
        pass

    # top_left
    try:
        if board[r-1][c-1] == player and board[r-2][c-2] == player and (board[r-3][c-3] == player or board[r+1][c+1] == player):
            return True
    except:
        pass

    # top_right
    try:
        if board[r - 1][c + 1] == player and board[r - 2][c + 2] == player and (board[r - 3][c + 3] == player or board[r+1][c-1] == player):
            return True
    except:
        pass

    # bottom_left
    try:
        if board[r + 1][c - 1] == player and board[r + 2][c - 2] == player and (board[r + 3][c - 3] == player or board[r-1][c+1] == player):
            return True
    except:
        pass

    # bottom_right
    try:
        if board[r+1][c+1] == player and board[r+2][c+2] == player and (board[r+3][c+3] == player or board[r-1][c-1] == player):
            return True
    except:
        pass

    return False


def four_in_a_row(board, row, col , player):
    depth = 1
    r = row
    c = col

    #Checking downward
    while r != 0 and board[r - 1][c] == player :
        r = r - 1
        depth = depth + 1
        if depth == 4:
            return True
    depth = 1
    r = row
    c = col

    #Checking upward
    while r != 5 and board[r + 1][c] == player:
        r = r + 1
        depth = depth + 1
        if depth == 4:
            return True
    depth = 1
    r = row
    c = col

    #Checking to the left
    while c != 0 and board[r][c - 1] == player or (depth == 3 and c <=3 and board[r][c+3] == player):
        c = c - 1
        depth = depth + 1
        if depth == 4:
            return True
    depth = 1
    r = row
    c = col

    #Checking to the right
    while c != 6 and board[r][c + 1] == player or (depth == 3 and c >=3 and board[r][c-3] == player):
        c = c + 1
        depth = depth + 1
        if depth == 4:
            return True
    depth = 1
    r = row
    c = col

    #Checking diagonally down and to the left
    while r != 0 and c != 0 and board[r - 1][c - 1] == player or (depth == 3 and r <= 2 and c <=3 and board[r+3][c+3] == player):
        r = r - 1
        c = c - 1
        depth = depth + 1
        if depth == 4:
            return True
    depth = 1
    r = row
    c = col

    #Checking diagonally up and to the left
    while r != 5 and c != 0 and board[r + 1][c - 1] == player or (depth == 3 and r >= 3 and c <=3 and board[r-3][c+3] == player):
        r = r + 1
        c = c - 1
        depth = depth + 1
        if depth == 4:
            return True
    depth = 1
    r = row
    c = col

    #Checking diagonally down and to the right
    while r != 0 and c != 6 and board[r - 1][c + 1] == player or (depth == 3 and r <= 2  and c >=3  and board[r+3][c-3] == player):
        r = r - 1
        c = c + 1
        depth = depth + 1
        if depth == 4:
            return True
    depth = 1
    r = row
    c = col

    #Checking diagonally up and to the right
    while r != 5 and c != 6 and board[r + 1][c + 1] == player or (depth == 3 and r >= 3 and c >=3 and board[r-3][c-3] == player):
        r = r + 1
        c = c + 1
        depth = depth + 1
        if depth == 4:
            return True


    return False
