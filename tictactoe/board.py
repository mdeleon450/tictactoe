import pygame
from .constants import *
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.empty_spaces = 9
        self.create_board()

    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 4)

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def move(self, row, col, color):
        if(self.board[row][col] == 0):
            self.board[row][col] = Piece(row,col, color)
            self.empty_spaces = self.empty_spaces - 1
            return True
        else:
            return False

    def check_winner(self, win):
        for row in range(ROWS):
            if str(self.board[row][0]) == str(self.board[row][1]) == str(self.board[row][2]) and self.board[row][0] != 0:
                if str(self.board[row][0].color) == "BLUE":
                    return 'O'
                elif str(self.board[row][0]) == "RED":
                    return 'X'
        for col in range(COLS):
            if str(self.board[0][col]) == str(self.board[1][col]) == str(self.board[2][col]) and self.board[0][col] != 0:
                if str(self.board[0][col]) == "BLUE":
                    return 'O'
                elif str(self.board[0][col]) == "RED":
                    return 'X'
        if str(self.board[0][0]) == str(self.board[1][1]) == str(self.board[2][2]) and self.board[0][0] != 0:
            if str(self.board[0][0]) == "BLUE":
                return 'O'
            elif str(self.board[0][0]) == "RED":
                return 'X'
        if self.empty_spaces == 0:
            return "Draw"