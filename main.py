# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Board import Board
from Engine1 import Engine1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    b = Board()
    opp = Engine1()
    print(b.legal_moves())
    player = 1
    while True:
        b.print()
        print()
        print()
        if player == 1:
            new_move = input("Make a move: (1-7)")
            move = int(new_move) - 1
            b.make_a_move(move, player)
            if(b.four_in_a_row(move,player) == True):
                print("PLayer 1 wins")
                break;
            player = 2
        else:
            new_move = opp.make_a_move(player)
            b.make_a_move(int(new_move) - 1, player)
            if (b.four_in_a_row(int(new_move), player) == True):
                print("PLayer 2 wins")
                break;
            player = 1




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
