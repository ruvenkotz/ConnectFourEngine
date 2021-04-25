import BoardFunctions
import Board
import HeuristicFunctions

class Engine5:
    # This engine tests out a new heuristic function

    def __init__(self):
        nextmove = 0

    def choose_a_move(self, player, b):
        moves_played = BoardFunctions.moves_played(b)
        moves = BoardFunctions.legal_moves(b)
        opp = 0
        if player == 1:
            opp == -1
        else:
            opp = 1
        if (moves_played == 0):
            return (5,3)
        elif (moves_played == 1):
            if (5,3) in moves:
                return (5,3)
            else:
                return (4,3)
        elif (moves_played == 2):
            x = b[5].index(opp)
            if (5, x+1) in moves:
                return (5,x+1)
            elif (5, x-1) in moves:
                return (5, x-1)

        #Checks for instant win
        for move in moves:
            if BoardFunctions.four_in_a_row(b, move[0], move[1], player):
               return move

        #Checks for instant loss
        for move in moves:
            if BoardFunctions.four_in_a_row(b, move[0], move[1], 0-player):
               return move

        next_move = HeuristicFunctions.in_a_row_heur3(b, player, moves)
        next_move.sort(reverse=True)
        #print(next_move[0])
        for i in next_move:
            try:
                if i[1][0] - 1 < 0:
                    return i[1]
                else:
                    bool = BoardFunctions.four_in_a_row(b, i[1][0]-1, i[1][1], 0-player)
                    if bool == False:
                        return i[1]
            except:
                pass
        if next_move == []:
            for i in moves:
                if i[1] > 1 and i[1] < 5:
                    next_move.append(i)




