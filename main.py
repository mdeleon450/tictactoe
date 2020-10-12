import pygame
import pygame.freetype
from tictactoe.constants import *
from tictactoe.game import *

pygame.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    turn = "BLUE"
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if turn == "BLUE" and board.move(row, col, "BLUE"):
                    turn = "RED"
                    board.check_winner(WIN, font)
                elif board.move(row, col, "RED"):
                    turn = "BLUE"
                    board.check_winner(WIN, font)
        game.update()

    pygame.quit()
main()
