from Board import Board
import random
import BoardFunctions
class Engine1:
    # This is my first iteration of an engine, it will find a win in one move and will block a win in one move,otherwise
    # it will play a random move

    def __init__(self):
        nextmove = 0

    def choose_a_move(self, player, b):
        moves = BoardFunctions.legal_moves(b)
        possibilities = []

        for move in moves:
            if BoardFunctions.four_in_a_row(b, move[0], move[1], player):
               return move

        for move in moves:
            if BoardFunctions.four_in_a_row(b, move[0], move[1], 0-player):
               return move

        for move in moves:
            possibilities.append(move)

        return random.choice(possibilities)




