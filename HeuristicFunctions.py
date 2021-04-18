
def in_a_rows(board, player, target):


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
