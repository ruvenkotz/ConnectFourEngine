def in_a_rows(board, row, col , player, target):
    depth = 1
    r = row
    c = col
    desired = player
    count = 0


    while r != 0 and board[r - 1][c] == desired:
        r = r - 1
        depth = depth + 1
        if depth == target:
            desired = 0
        if depth == 4:
            count+=1

    depth = 1
    r = row
    c = col
    desired = player
    while r != 5 and board[r + 1][c] == desired:
        r = r + 1
        depth = depth + 1
        if depth == target:
            desired = 0
        if depth == 4:
            count+=1
    depth = 1
    r = row
    c = col
    desired = player
    while c != 0 and board[r][c - 1] == desired:
        c = c - 1
        depth = depth + 1
        if depth == target:
            desired = 0
        if depth == 4:
            count+=1
    depth = 1
    r = row
    c = col
    desired = player
    while c != 6 and board[r][c + 1] == desired:
        c = c + 1
        depth = depth + 1
        if depth == target:
            desired = 0
        if depth == 4:
            count+=1
    depth = 1
    r = row
    c = col
    desired = player
    while r != 0 and c != 0 and board[r - 1][c - 1] == desired:
        r = r - 1
        c = c - 1
        depth = depth + 1
        if depth == target:
            desired = 0
        if depth == 4:
            count+=1
    depth = 1
    r = row
    c = col
    desired = player
    while r != 5 and c != 0 and board[r + 1][c - 1] == desired:
        r = r + 1
        c = c - 1
        depth = depth + 1
        if depth == target:
            desired = 0
        if depth == 4:
            count+=1
    depth = 1
    r = row
    c = col
    desired = player
    while r != 0 and c != 6 and board[r - 1][c + 1] == desired:
        r = r - 1
        c = c + 1
        depth = depth + 1
        if depth == target:
            desired = 0
        if depth == 4:
            count+=1
    depth = 1
    r = row
    c = col
    desired = player
    while r != 5 and c != 6 and board[r + 1][c + 1] == desired:
        r = r + 1
        c = c + 1
        depth = depth + 1
        if depth == target:
            desired = 0
        if depth == 4:
            count+=1

    return count
