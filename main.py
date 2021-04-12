# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Board import Board
from GUI import draw_board
from Engine1 import Engine1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    b = Board()
    player = 1
    opp = Engine1()

    # Player 1 Moves
    draw_board(b)

    # print(b.legal_moves())

    #     move_col = int(new_move) - 1
    #     moves = b.legal_moves()
    #     if b.four_in_a_row(move_col,player) == True :
    #         print("Player 1 wins")
    #         b.print()
    #         break;
    #     b.make_a_move(move_col, player)
    #     player = 2
    #
    #     #Player 2 Moves
    #     new_move = opp.choose_a_move(player, b)
    #     moves = b.legal_moves()
    #     if b.four_in_a_row(new_move, player) == True :
    #         print("Player 2 wins")
    #         b.print()
    #         break;
    #     b.make_a_move(new_move, player)
    #     player = 1






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
