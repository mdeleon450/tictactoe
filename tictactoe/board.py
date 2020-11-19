import pygame
from .constants import *
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.empty_spaces = 9
        self.moves = []
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
            self.moves.append([row,col,color])
            self.empty_spaces = self.empty_spaces - 1
            return True
        else:
            return False

    def check_winner(self, win):
        for row in range(ROWS):
            if str(self.board[row][0]) == str(self.board[row][1]) == str(self.board[row][2]) and self.board[row][0] != 0:
                if str(self.board[row][0]) == "1":
                    return 'O'
                elif str(self.board[row][0]) == "-1":
                    return 'X'
        for col in range(COLS):
            if str(self.board[0][col]) == str(self.board[1][col]) == str(self.board[2][col]) and self.board[0][col] != 0:
                if str(self.board[0][col]) == "1":
                    return 'O'
                elif str(self.board[0][col]) == "-1":
                    return 'X'
        if str(self.board[0][0]) == str(self.board[1][1]) == str(self.board[2][2]) and self.board[0][0] != 0:
            if str(self.board[0][0]) == "1":
                return 'O'
            elif str(self.board[0][0]) == "-1":
                return 'X'
        if str(self.board[2][0]) == str(self.board[1][1]) == str(self.board[0][2]) and self.board[0][2] != 0:
            if str(self.board[0][2]) == "1":
                return 'O'
            elif str(self.board[0][2]) == "-1":
                return 'X'
        if self.empty_spaces == 0:
            return "Draw"

    def get_legal_moves(self):
        choices = []
        for row in range(ROWS):
            for col in range(COLS):
                if(self.is_space_empty(row,col)):
                    choices.append([row,col])
        return choices

    def is_space_empty(self, row, col):
        return self.board[row][col] == 0

    def last_move(self):
        return self.moves[-1]

    def evaluate(self):
        xCount = 0
        oCount = 0
        #print(self.board)
        for row in range(ROWS):
           if((str(self.board[row][0]) == str(self.board[row][1]) and self.board[row][1] != 0) or (str(self.board[row][2]) == str(self.board[row][1]) and self.board[row][2] != 0)):
               if(str(self.board[row][1]) == "1"):
                   oCount = oCount + 1
               elif(str(self.board[row][1]) == "-1"):
                   xCount = xCount + 1
        for col in range(COLS):
            if str(self.board[0][col]) == str(self.board[1][col]) and self.board[1][col] != 0 or str(self.board[2][col]) == str(self.board[1][col]) and self.board[1][col] != 0:
                if str(self.board[1][col]) == "1":
                    oCount = oCount + 1
                elif str(self.board[1][col]) == "-1":
                    xCount = xCount + 1
        if str(self.board[0][0]) == str(self.board[1][1]) and self.board[1][1] != 0 or str(self.board[1][1]) == str(self.board[2][2]) and self.board[1][1] != 0:
            if str(self.board[0][0]) == "1":
                oCount = oCount + 1
            elif str(self.board[0][0]) == "-1":
                xCount = xCount + 1
        if str(self.board[2][0]) == str(self.board[1][1]) and self.board[1][1] != 0 or str(self.board[1][1]) == str(self.board[0][2]) and self.board[1][1] != 0:
            if str(self.board[1][1]) == "1":
                oCount = oCount + 1
            elif str(self.board[1][1]) == "-1":
                xCount = xCount + 1
        return xCount - oCount