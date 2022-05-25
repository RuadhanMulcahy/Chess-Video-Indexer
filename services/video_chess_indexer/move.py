# from square import Square


class Move:
    def __init__(self, flipped=None):
        self.prev_square = None
        self.new_square = None
        self.color = None
        self.time_stamp = None
        self.flipped = flipped

    def compare(self, move):
        print(self.flipped)
        if self.prev_square.compare(move.prev_square) and self.new_square.compare(move.new_square):
            return True
        return False

    def show(self):
        if self.prev_square is not None:
            print(f"Prev Square: y: {self.prev_square.y} x: {self.prev_square.x}")
        else:
            print(f"Prev Square: None")
        if self.new_square is not None:
            print(f"New Square: y: {self.new_square.y} x: {self.new_square.x} time_stamp: {self.time_stamp}")
        else:
            print(f"New Square: None")

        print(f"Flipped: {self.flipped}")

move1 = Move(True)
