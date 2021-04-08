from Board import Board
import random
class Engine1:
    # This is my first iteration of an engine, it will find a win in one move and will block a win in one move,otherwise
    # it will play a random move

    def __init__(self):
        nextmove = 0

    def make_a_move(self,player):
        b = Board()
        moves = b.legal_moves()
        possibilities = []
        for move in moves:
            if b.four_in_a_row(move, player) == True:
                print("You can win")
            player = 1
            if b.four_in_a_row(move, player) == True:
                print("You're gonna lose")

            possibilities.append(move[1])
        return random.choice(possibilities)




