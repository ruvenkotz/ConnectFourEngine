from Board import Board
import random
import BoardFunctions
import HeuristicFunctions
import copy
class Engine2:
    # This is my first iteration of an engine, it will find a win in one move and will block a win in one move,otherwise
    # it will play a random move

    def __init__(self):
        nextmove = 0

    def choose_a_move(self, player, b):
        moves = BoardFunctions.legal_moves(b)
        possibilities = []

        threes = 0
        # for r in range(0,5):
        #     for c in range(0,6):
        #         if b[r][c] == player:
        #             threes += HeuristicFunctions.in_a_rows(b, r, c, player, 3)
        # print(threes)

        for move in moves:
            if BoardFunctions.four_in_a_row(b, move[0], move[1], player):
               return move

        #print()
        for move in moves:
            if BoardFunctions.four_in_a_row(b, move[0], move[1], 0-player):
               return move

        for move in moves:
            board_copy = copy.deepcopy(b)
            board_copy[move[0]][move[1]] = player
            threes += HeuristicFunctions.in_a_rows(board_copy, player, 3)
            print(str(move[1]) + " " + str(threes))
            threes = 0
            possibilities.append(move)


        return random.choice(possibilities)




