import pygame
import random
import pygame.freetype
from tictactoe.constants import *
from tictactoe.board import Board


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    turn = 1
    winner = None
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if (turn == -1):
                choice = random.choice(board.get_legal_moves())
                board.move(choice[0], choice[1], -1)
                turn = 1
                winner = board.check_winner(WIN)

            if event.type == pygame.MOUSEBUTTONDOWN and winner == None:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if turn == 1 and board.move(row, col, 1):
                    turn = -1
                    winner = board.check_winner(WIN)
                if winner == "Draw":
                    print("It is a Draw!")
                elif winner != None:
                    print(str(winner) + " wins!")
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()
main()
