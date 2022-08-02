class Move:
    def __init__(self, board, time_stamp, flipped):
        self.create(board, time_stamp, flipped)
        self.taken_piece = None

    def create(self, board, time_stamp, flipped):
        self.time_stamp = time_stamp
        self.board = board
        for row in board.squares:
            for square in row:
                if square.highlighted and square.piece_short != '':
                    self.new_square = square
                    self.new_square.set_pgn(flipped)
                    self.color = square.color
                elif square.highlighted and square.piece_short == '':
                    self.prev_square = square
                    self.prev_square.set_pgn(flipped)

    def is_match(self, move):
        if self.prev_square.compare(move.prev_square) and self.new_square.compare(move.new_square):
            return True
        return False

    def show(self):
        print(self.new_square.piece_verbose)
        # print(self.taken_piece)
        if self.prev_square is not None:
            print(f"{self.prev_square.pgn_x} {self.prev_square.pgn_y}")
        else:
            print(f"Prev Square: None")
        if self.new_square is not None:
            print(f"{self.new_square.pgn_x} {self.new_square.pgn_y}")
        else:
            print(f"New Square: None")

        print(self.time_stamp)