from board import Board
import time

class Game:
    def __init__(self):
        self.board = None
        self.board_prev = None
        self.create_game_starts()

    def read_position(self, board):
        self.board_prev = self.board
        self.board = board

        if self.check_for_position_change():
            return self.check_for_game_start()
        return False

    def check_for_position_change(self):
        if self.board_prev is None:
            return True
        if self.board.compare(self.board_prev) is False:
            return True
        return False

    def create_game_starts(self):
        self.board_normal = Board()
        self.board_flipped = Board()

        self.board_normal.create_game_start(False)
        self.board_flipped.create_game_start(True)

    def check_for_game_start(self):
        if self.board.compare(self.board_normal) or self.board.compare(self.board_flipped):
            print("here")
            return True
        return False



