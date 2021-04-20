import BoardFunctions
import HeuristicFunctions
from Engine1 import Engine1
import copy
class Engine4:
    # This is my first iteration of an engine, it will find a win in one move and will block a win in one move,otherwise
    # it will play a random move

    def __init__(self):
        nextmove = 0


    def choose_a_move(self, player, b):
        random_move = Engine1()
        random_testing = False
        num_of_random_moves = 2
        moves_played = BoardFunctions.moves_played(b)
        if random_testing and moves_played <= num_of_random_moves:
            return random_move.choose_a_move(player, b)
        return self.minimax(player,b, 2)




    def minimax(self, player, b, depth):
        move_value = self.max_value(player, b, depth)
        # print(BoardFunctions.legal_moves(b))
        # print(move_value[0])
        # # print(move_value[1])
        return move_value[0]

    def max_value(self, player, b, depth):
        moves = BoardFunctions.legal_moves(b)
        best_move = ((0,0), -100001)
        for move in moves:
            if BoardFunctions.four_in_a_row(b, move[0], move[1], player):
                return (move, 100000)
            board_copy = copy.deepcopy(b)
            board_copy[move[0]][move[1]] = player
            move_value = self.min_value(player, board_copy, depth - 1)
            if move_value[1] > best_move[1]:
                best_move = (move, move_value[1])
        return best_move


    def min_value(self, player, b,depth):
        moves = BoardFunctions.legal_moves(b)
        best_move = ((0,0), 100001)

        if depth <= 0:
            for move in moves:
                if BoardFunctions.four_in_a_row(b, move[0], move[1], 0 - player):
                    return (move, -100000)
                board_copy = copy.deepcopy(b)
                board_copy[move[0]][move[1]] = 0 - player
                move_value = self.get_value(player, board_copy, move)
                if (move_value < best_move[1]):
                    best_move = (move, move_value)
            return best_move

        for move in moves:
            if BoardFunctions.four_in_a_row(b, move[0], move[1], 0-player):
                return (move, -100000)
            board_copy = copy.deepcopy(b)
            board_copy[move[0]][move[1]] = 0 - player
            move_value = self.max_value(player, board_copy, depth - 1)
            if move_value[1] < best_move[1]:
                best_move = (move, move_value[1])
        return best_move


    def get_value(self, player, b, move):

        threes = 0
        twos = 0
        ones = 0
        threes += HeuristicFunctions.in_a_rows(b, player, 3)
        threes -= HeuristicFunctions.in_a_rows(b, 0 - player, 3)
        twos += HeuristicFunctions.in_a_rows(b, player, 2)
        twos -= HeuristicFunctions.in_a_rows(b, 0 - player, 2)
        ones += HeuristicFunctions.in_a_rows(b, player, 1)
        ones -= HeuristicFunctions.in_a_rows(b, 0 - player, 1)
        total_score = 100*threes + 10*twos + 1*ones
        return total_score





