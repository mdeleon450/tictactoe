import pygame
from .board import *
from .constants import *
class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col, turn):
        if self.selected:
            result = self.move(row, col, turn)
            if not result:
                self.selected = None
                self.select(row, col, turn)
        else:
            piece = self.board[row][col]
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True

        return False

    def _move(self, row, col, turn):
        piece = self.board[row][col]
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(row, col, turn)
        else:
            return False

        return True

    def change_turn(self):
        if self.turn == RED:
            self.turn = BLUE
        else
            self.turn = RED
