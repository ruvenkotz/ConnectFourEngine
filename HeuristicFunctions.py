
import BoardFunctions


def in_a_row3(board, player, move, opp):
    """
    current_move = [4,1]
    [2,1]. [2,2]. [2,3], [2,4], [2,5]
    [3,1], [3,2], [3,3], [3,4], [3,5]
    [4,1], [4,2] [4,3], [4,4], [4,5]
    [5,1], [5,2] [5,3], [5,4], [5,5]
    """
    move_score = 0
    ply = player
    if opp == False:
        two_amt = 10
        three_amt = 100
    else:
        ply == 0 - player
        two_amt = 9
        three_amt = 101
    y = move[0]
    x= move[1]
    #top right
    try:
        if board[y-1][x+1] == ply:
            move_score += two_amt
            if (board[y-2][x+2] == ply or board[y+1][x-1] == ply):
                move_score += three_amt
    except:
        pass
    # top left
    try:
        if board[y - 1][x - 1] == ply:
            move_score += two_amt
            if (board[y - 2][x - 2] == ply or board[y + 1][x + 1] == ply):
                move_score += three_amt
    except:
        pass

    #right
    try:
        if board[y][x + 1] == ply:
            move_score += two_amt
            if (board[y][x + 2] == ply or board[y][x - 1] == ply):
                move_score += three_amt
    except:
        pass
    # left
    try:
        if board[y][x - 1] == ply:
            move_score += two_amt
            if (board[y][x - 2] == ply or board[y][x + 1] == ply):
                move_score += three_amt
    except:
        pass

    # bottom left
    try:
        if board[y + 1][x - 1] == ply:
            move_score += two_amt
            if (board[y + 2][x - 2] == ply or board[y - 1][x + 1] == ply):
                move_score += three_amt
    except:
        pass

    # bottom
    try:
        if board[y-1][x] == ply:
            move_score += two_amt
            if (board[y-2][x] == ply):
                move_score += three_amt
    except:
        pass

    # bottom right
    try:
        if board[y+1][x + 1] == ply:
            move_score += two_amt
            if (board[y+2][x + 2] == ply or board[y-1][x - 1] == ply):
                move_score += three_amt
    except:
        pass

    return move_score


def in_a_row_heur3(board, player, legal_moves):
    moves = []
    for i in legal_moves:
        move_score = in_a_row3(board, player, legal_moves, False)
        move_score += in_a_row3(board, player, legal_moves, True)
        moves.append((move_score, i))
    return moves





def three_search(board, player, curr, two):
    threez = curr[0] - two[0]
    threeo = curr[1] - two[1]
    if threez > 0 and threeo > 0:
        try:
            if board[two+1][two+1] == player:
                return True
        except:
            pass
    elif threez > 0 and threeo < 0:
        try:
            if board[two+1][two+1] == player:
                return True
        except:
            pass
    elif threez <0 and threeo > 0:
        try:
            if board[two-1][two-1] == player:
                return True
        except:
            pass
    elif threez <0 and threeo < 0:
        try:
            if board[two-1][two+1] == player:
                return True
        except:
            pass
    elif threez == 0 and threeo <0:
        try:
            if board[two][two+1] == player:
                return True
        except:
            pass
    elif threez == 0 and threeo >0:
        try:
            if board[two][two-1] == player:
                return True
        except:
            pass

    elif threez < 0 and threeo == 0:
        try:
            if board[two+1][two] == player:
                return True
        except:
            pass
    else:
        return False

def in_a_row_helper(board, player, current_spot, player_bool):
    """




    current_move = [4,1]
    [3,0], [3,1], [3,2]
    [4,0], [4,1] [4,2]
    [5,0], [5,1] [5,2]
    """
    print (current_spot)
    if player_bool == True:
        spot = player
    else:
        spot = 0 #empty spot
    consec = []
    y = current_spot[0]
    x = current_spot[1]
    skip_tl = False
    skip_t = False
    skip_tr = False
    skip_r = False
    skip_l = False
    skip_bl = False
    skip_b = False
    skip_br = False
    print (x, y)
    if y - 1 <= 1 or x + 1 == 7:
        skip_tr = True
    if y - 1 <= 1 or x -1 == -1:
        skip_tl = True
    if x + 1 >= 5:
        skip_r = True
    if x + 1 >= 5 or y + 1 >= 5:
        skip_br = True
    if x - 1 <1:
        skip_l = True
    if y + 1 >5 or x -1 < 1:
        skip_bl = True

    # above example [5,2]
    if skip_tr !=True:

        if board[y-1][x+1] == spot:
            consec.append((y-1, x+1))

        # above example [3, 2]
    if skip_tl != True:

        if board[y - 1][x - 1] == spot:
            consec.append((y - 1, x - 1))

    # above example [4, 2]
    if skip_r != True:

        if board[y][x+1] == spot:
            consec.append((y, x+1))

    #above example is [4,0]
    if skip_l != True:

        if board[y][x-1] == spot:
            consec.append((y, x-1))

    #above example is [5,0]
    if skip_bl != True:

        if board[y+1][x-1] == spot:
            consec.append((y+1, x-1))

    #above example os [3,0]
    if skip_br != True:

        if board[y+1][x+1] == spot:
            consec.append((y+1, x+1))

    return consec


def in_a_row_heur2(board, player, legal_moves, ply):
    moves = []
    if ply == True:
        threeamt = 100
        twoamt = 10
    else:
        threeamt = 101
        twoamt = 9
    for plymove in legal_moves:
        two_spots = in_a_row_helper(board, player, plymove, ply)
        twos = len(two_spots)
        num_two = len(two_spots)
        if num_two == 0:
            moves.append((1, plymove))
        else:
            for j in two_spots:
                three_spots = three_search(board, player, plymove, j)
                if three_spots == False:
                    moves.append((twoamt * twos, plymove))
                else:
                    moves.append((threeamt, plymove))
    return moves




def in_a_row_heur(board, player, legal_moves, ply):
    moves = []
    twos = []
    threes = []

    #for the move, see if the move has a two in a row with a move
    #the number of conseccutive spaces raises the heuristic
    #for the connected moves see if those moves have a connected move

    for plymove in legal_moves:
        if ply == True:
            threeamt = 100
            twoamt = 10
        else:
            threeamt = 101
            twoamt = 10
        move_pos = []
        twos = 0
        threes = 0
        new_twos = []
        #threes.append(in_a_row_helper(board, player, plymove, True))
        two_spots = in_a_row_helper(board, player, plymove, True)
        for j in two_spots:
            three_spot = in_a_row_helper(board, player, j, True)
            lthree_spot = len(three_spot)
            threes = threes + lthree_spot
            if lthree_spot == 0:
                twos+=1
        moves.append(((threes*threeamt+ twos*twoamt),plymove))


        num_empty = len(new_twos)
    moves.sort()
    return moves





















def in_a_rows1(board, player, target):


    count = 0
    target = target + 1
    for row in range(0, 6):
        for col in range(0, 7):
            if board[row][col] == 0:
                depth = 1
                r = row
                c = col

                #Checking downward
                while depth < target and r != 0 and board[r - 1][c] == player:
                    r = r - 1
                    depth = depth + 1
                    if depth == target:
                        count+=1
                        # print("D")
                        # print("Col: " + str(col))



                depth = 1
                r = row
                c = col
                #Checking upward
                while depth < target and r != 5 and board[r + 1][c] == player:
                    r = r + 1
                    depth = depth + 1
                    if depth == target:
                        count+=1
                        # print("U")
                        # print("Col: " + str(col))


                depth = 1
                r = row
                c = col
                #Checking to the left
                while depth < target and c != 0 and board[r][c - 1] == player or (depth == 3 and c <=3 and board[r][c+3] == player):
                    c = c - 1
                    depth = depth + 1
                    if depth == target:
                        count+=1
                        # print("L")
                        # print("Col: " + str(col))


                depth = 1
                r = row
                c = col
                #Checking to the right
                while depth < target and c != 6 and board[r][c + 1] == player or (depth == 3 and c >=3 and board[r][c-3] == player):
                    c = c + 1
                    depth = depth + 1
                    if depth == target:
                        count+=1
                        # print("R")
                        # print("Col: " + str(col))


                depth = 1
                r = row
                c = col

                #Checking diagonally down and to the left
                while depth < target and r != 0 and c != 0 and board[r - 1][c - 1] == player or (depth == 3 and r <= 2 and c <=3 and board[r+3][c+3] == player):
                    r = r - 1
                    c = c - 1
                    depth = depth + 1
                    if depth == target:
                        count+=1
                        # print("DL")
                        # print("Col: " + str(col))



                depth = 1
                r = row
                c = col

                #Checking diagonally up and to the left
                while depth < target and r != 5 and c != 0 and board[r + 1][c - 1] == player or (depth == 3 and r >= 3 and c <=3 and board[r-3][c+3] == player):
                    r = r + 1
                    c = c - 1
                    depth = depth + 1
                    if depth == target:
                        count+=1
                        # print("UL")
                        # print("Col: " + str(col))


                depth = 1
                r = row
                c = col

                #Checking diagonally down and to the right
                while depth < target and r != 0 and c != 6 and board[r - 1][c + 1] == player or (depth == 3 and r <= 2  and c >=3  and board[r+3][c-3] == player):
                    r = r - 1
                    c = c + 1
                    depth = depth + 1
                    if depth == target:
                        count+=1
                        # print("DR")
                        # print("Col: " + str(col))


                depth = 1
                r = row
                c = col
                #Checking diagonally up and to the right
                while depth < target and r != 5 and c != 6 and board[r + 1][c + 1] == player or (depth == 3 and r >= 3 and c >=3 and board[r-3][c-3] == player):
                    r = r + 1
                    c = c + 1
                    depth = depth + 1
                    if depth == target:
                        count+=1
                        # print("UR")
                        # print("Col: " + str(col))


    return count
