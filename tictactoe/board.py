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
        self.board[row][col] = Piece(row,col, color)

    def check_winner(self):
        for row in range(ROWS):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] != 0:
                if self.board[row][0] == "BLUE":
                    print("O Wins!")
                elif self.board[row][0] == "RED":
                    print("X Wins!")
        for col in range(COLS):
            if self.board[0][col] == self.board[1][col] == self.board[0][col] and self.board[0][col] != 0:
                if self.board[0][col] == "BLUE":
                    print("O Wins!")
                elif self.board[0][col] == "RED":
                    print("X Wins!")
        if self.board[0][0]==self.board[1][1]==self.board[2][2] and self.board[0][2]!=0:
            if self.board[0][0] == "BLUE":
                print("O Wins!")
            elif self.board[0][0] == "RED":
                print("X Wins!")
    def print_board(self):
        print(self.board)
