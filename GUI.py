import numpy as np
import pygame
import sys
from Engine1 import Engine1
from Engine2 import Engine2
from Engine3 import Engine3
from Engine4 import Engine4


import BoardFunctions
from Engine5 import Engine5

BLUE = (0, 0, 200)
BLACK = (0, 0, 0)
RED = (240, 0, 0)
YELLOW = (250, 240, 10)

SQUARE = 100
width = SQUARE * 7
height = SQUARE * 7
RADIUS = int(SQUARE / 2 - 5)
pygame.init()
screen = pygame.display.set_mode((width, height))
opp = Engine5()


def drop(col, ply, board):
    """
    this picks the col and drops a piece into it
    :param col:
    :return:
    """
    #pass
    for i in reversed(range(0, 6)):
        if board.get_board()[i][col] == 0:
            board.set_board(i, col, ply)
            return i


def draw_board(board):
    for col in range(0, 7):
        pygame.display.update()
        for row in range(0, 7):
            pygame.draw.rect(screen, BLUE, (row * SQUARE, col * SQUARE + SQUARE, SQUARE, SQUARE))
            pygame.draw.circle(screen, BLACK,
                               (int(row * SQUARE + SQUARE / 2), int(col * SQUARE + SQUARE + SQUARE / 2)), RADIUS)
    ply = 1
    color = RED

    pygame.display.update()
    GAME_OVER = False
    while not GAME_OVER:
        move = (0,0)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            if events.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE))
                pygame.draw.circle(screen, color, (events.pos[0], 50), RADIUS)
            if events.type == pygame.MOUSEBUTTONDOWN:
                if ply == 1:
                    col = (int(np.floor(events.pos[0] / 100)))
                    row = drop(col, ply, board)
                if ply == -1:
                    tup = opp.choose_a_move(ply, board.get_board())
                    col = tup[1]
                    row = drop(col, ply, board)

                #move = (row, col)
                try:
                    pygame.draw.circle(screen, color,
                                       (int(col * SQUARE + SQUARE / 2), int((row) * SQUARE + SQUARE + SQUARE / 2)),
                                       RADIUS)


                    if BoardFunctions.four_in_a_row2(board.get_board(), row, col, ply):
                        print("Player " + str(ply) + " wins")
                        GAME_OVER = True



                    ply = 0 - ply
                    if color == RED:
                        color = YELLOW
                    else:
                        color = RED
                except:
                    pass
        pygame.display.update()
    while GAME_OVER:
        move = 1










