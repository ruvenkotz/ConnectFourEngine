from Engine1 import Engine1
from Board import Board
import BoardFunctions


def play_games(n):
    player = Engine1()
    player_1_wins = 0
    player_2_wins = 0
    drawn_games = 0
    for i in range(0, n):
        game_not_over = True
        b = Board()
        while game_not_over:
            move_1 = player.choose_a_move(1, b.get_board())
            b.set_board(move_1[0], move_1[1], 1)
            if BoardFunctions.four_in_a_row(b.get_board(), move_1[0], move_1[1], 1):
                game_not_over = False
                player_1_wins += 1

            if game_not_over:
                move_2 = player.choose_a_move(-1, b.get_board())
                b.set_board(move_2[0], move_2[1], -1)
                if BoardFunctions.four_in_a_row(b.get_board(), move_2[0], move_2[1], -1):
                    game_not_over = False
                    player_2_wins += 1
                elif b.get_moves_played() == 42:
                    game_not_over = False
                    drawn_games += 1

    print("Player 1 won: " + str(player_1_wins) + " games")
    print("Player 2 won: " + str(player_2_wins) + " games")
    print("Games Drawn " + str(drawn_games) + " games")





