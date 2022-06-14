class Move:
    def __init__(self):
        self.prev_square = None
        self.new_square = None
        self.board = None
        self.color = None
        self.time_stamp = None

    def compare(self, move):
        if self.prev_square.compare(move.prev_square) and self.new_square.compare(move.new_square):
            return True
        return False

    def show(self):
        if self.prev_square is not None:
            print(f"{self.prev_square.pgn_x} {self.prev_square.pgn_y}")
        else:
            print(f"Prev Square: None")
        if self.new_square is not None:
            print(f"{self.new_square.pgn_x} {self.new_square.pgn_y}")
        else:
            print(f"New Square: None")

        print(self.time_stamp)
