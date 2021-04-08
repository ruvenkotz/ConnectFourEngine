from Board import Board
import random
class Engine1:
    # This is my first iteration of an engine, it will find a win in one move and will block a win in one move,otherwise
    # it will play a random move

    def __init__(self):
        nextmove = 0

    def choose_a_move(self, player, board):
        b = board
        moves = b.legal_moves()
        print(moves)
        possibilities = []
        for move in moves:
            possibilities.append(move[1])
            if b.four_in_a_row(move[1], player) == True:
               return move[1]

        for move in moves:
            if b.four_in_a_row(move[1], player-1) == True:
               print(move[1])
               return move[1]

        return random.choice(possibilities)




