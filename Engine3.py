import BoardFunctions
import HeuristicFunctions
from Engine1 import Engine1
import copy
class Engine3:
    # This is my first iteration of an engine, it will find a win in one move and will block a win in one move,otherwise
    # it will play a random move

    def __init__(self):
        nextmove = 0


    def choose_a_move(self, player, b):
       # print(self.minimax(player, b))
        return self.minimax(player,b)

    def minimax(self, player, b):
        move_value = self.max_value(player, b)
        return move_value

    def max_value(self, player, b):
        moves = BoardFunctions.legal_moves(b)
        best_move = ((0,0), -100001)
        for move in moves:
            board_copy = copy.deepcopy(b)
            board_copy[move[0]][move[1]] = player
            move_value = self.min_value(player, board_copy)
            if move_value[1] > best_move[1]:
                best_move = (move, move_value[1])

        return best_move[0]

    def min_value(self, player, b):
        moves = BoardFunctions.legal_moves(b)
        best_move = ((0,0), 100001)
        for move in moves:
            board_copy = copy.deepcopy(b)
            board_copy[move[0]][move[1]] = 0 - player
            move_value = self.get_value(player, board_copy, move)
            if(move_value < best_move[1]):
                best_move = (move, move_value)

        return best_move


    def get_value(self, player, b, move):
        if BoardFunctions.four_in_a_row(b, move[0], move[1], player):
            return 100000
        if BoardFunctions.four_in_a_row(b, move[0], move[1], 0 - player):
            return -100000

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





    # def choose_a_move(self, player, b):
    #     moves = BoardFunctions.legal_moves(b)
    #     possibilities = []
    #
    #     random_move = Engine1()
    #     random_testing = True
    #     num_of_random_moves = 3
    #     moves_played = BoardFunctions.moves_played(b)
    #
    #     threes = 0
    #     twos = 0
    #     ones = 0
    #     best_move = ((0, 0), 0)
    #
    #     #Checks for instant win
    #     for move in moves:
    #         if BoardFunctions.four_in_a_row(b, move[0], move[1], player):
    #            return move
    #
    #     #Checks for instant loss
    #     for move in moves:
    #         if BoardFunctions.four_in_a_row(b, move[0], move[1], 0-player):
    #            return move
    #
    #
    #     #Random moves in the opening
    #     if random_testing and moves_played < num_of_random_moves:
    #         rand_move = random_move.choose_a_move(1, b)
    #         best_move = (rand_move, 100000)
    #
    #     #Adds moves and scores to a list
    #     for move in moves:
    #         board_copy = copy.deepcopy(b)
    #         board_copy[move[0]][move[1]] = player
    #         threes += HeuristicFunctions.in_a_rows(board_copy, player, 3)
    #         threes -= HeuristicFunctions.in_a_rows(board_copy, 0 - player, 3)
    #         twos += HeuristicFunctions.in_a_rows(board_copy, player, 2)
    #         twos -= HeuristicFunctions.in_a_rows(board_copy, 0 - player, 2)
    #         ones += HeuristicFunctions.in_a_rows(board_copy, player, 1)
    #         ones -= HeuristicFunctions.in_a_rows(board_copy, 0 - player, 1)
    #         total_score = 100*threes + 10*twos + 1*ones
    #        # print(total_score)
    #         threes = 0
    #         twos = 0
    #         ones = 0
    #         possibilities.append((move, total_score))
    #
    #     #Picks out the move with the highest score
    #     for pos in possibilities:
    #         if pos[1] > best_move[1]:
    #             best_move = pos
    #
    #
    #
    #     return best_move[0]




