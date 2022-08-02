from board import Board

class GameStart:
    def __init__(self):
        self.create()
        self.flipped = None
        self.on_game_start = False

    def create(self):
        self.board_normal = Board()
        self.board_flipped = Board()
        self.board_normal.create_game_start(False)
        self.board_flipped.create_game_start(True)

    def check(self, board):
        if board.is_match(self.board_normal, False):
            self.flipped = False
            if self.on_game_start == False:
                self.on_game_start = True
            self.on_game_start = True
        elif board.is_match(self.board_flipped, False):
            self.flipped = True
            if self.on_game_start == False:
                self.on_game_start = True
                return True
        else:
            self.on_game_start = False
            return False