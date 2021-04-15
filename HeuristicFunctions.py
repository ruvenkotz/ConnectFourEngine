def in_a_rows(board, player, target):
    count = 0
    for row in range(0, 6):
        for col in range(0, 7):
            if board[row][col] == player:
                depth = 1
                r = row
                c = col
                desired = player

                #Checking downward
                while r != 0 and board[r - 1][c] == desired:
                    r = r - 1
                    depth = depth + 1
                    if depth == target:
                        desired = 0
                    if depth == 4:
                        count+=1
                        #print("D")


                depth = 1
                r = row
                c = col
                desired = player
                #Checking upward
                while r != 5 and board[r + 1][c] == desired:
                    r = r + 1
                    depth = depth + 1
                    if depth == target:
                        desired = 0
                    if depth == 4:
                        count+=1
                        #print("U")

                depth = 1
                r = row
                c = col
                desired = player
                #Checking to the left
                while c != 0 and board[r][c - 1] == desired or (depth == 3 and c <=3 and board[r][c+3] == desired):
                    c = c - 1
                    depth = depth + 1
                    if depth == target:
                        desired = 0
                    if depth == 4:
                        count+=1
                        #print("L")

                depth = 1
                r = row
                c = col
                desired = player
                #Checking to the right
                while c != 6 and board[r][c + 1] == desired or (depth == 3 and c >=3 and board[r][c-3] == desired):
                    c = c + 1
                    depth = depth + 1
                    if depth == target:
                        desired = 0
                    if depth == 4:
                        count+=1
                        #print("R")

                depth = 1
                r = row
                c = col
                desired = player

                #Checking diagonally down and to the left
                while r != 0 and c != 0 and board[r - 1][c - 1] == desired or (depth == 3 and r <= 2 and c <=3 and board[r+3][c+3] == desired):
                    r = r - 1
                    c = c - 1
                    depth = depth + 1
                    if depth == target:
                        desired = 0
                    if depth == 4:
                        count+=1
                        #print("DL")


                depth = 1
                r = row
                c = col
                desired = player

                #Checking diagonally up and to the left
                while r != 5 and c != 0 and board[r + 1][c - 1] == desired or (depth == 3 and r >= 3 and c <=3 and board[r-3][c+3] == desired):
                    r = r + 1
                    c = c - 1
                    depth = depth + 1
                    if depth == target:
                        desired = 0
                    if depth == 4:
                        count+=1
                        #print("UL")

                depth = 1
                r = row
                c = col
                desired = player

                #Checking diagonally down and to the right
                while r != 0 and c != 6 and board[r - 1][c + 1] == desired or (depth == 3 and r <= 2  and c >=3  and board[r+3][c-3] == desired):
                    r = r - 1
                    c = c + 1
                    depth = depth + 1
                    if depth == target:
                        desired = 0
                    if depth == 4:
                        count+=1
                        #print("DR")

                depth = 1
                r = row
                c = col
                desired = player
                #Checking diagonally up and to the right
                while r != 5 and c != 6 and board[r + 1][c + 1] == desired or (depth == 3 and r >= 3 and c >=3 and board[r-3][c-3] == desired):
                    r = r + 1
                    c = c + 1
                    depth = depth + 1
                    if depth == target:
                        desired = 0
                    if depth == 4:
                        count+=1
                        #print("UR")


    return count
