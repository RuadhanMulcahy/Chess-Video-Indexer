class Game:
    def __init__(self):
        self.moves = []
        self.moves_ahead = []
        self.move_count = 0

    def add_move(self, move):
        self.moves.append(move)
        if self.reverse_move_check():
            self.moves.pop()
            self.moves_ahead.append(move)

    def show_game(self):
        print("Moves")
        for move in self.moves:
            move.show()

        print("Moves ahead")
        for move in self.moves_ahead:
            move.show()

    def reverse_move_check(self):
        if len(self.moves) < 2:
            return False
        prev_move = self.moves[-2]
        curr_move = self.moves[-1]
        if curr_move.board.squares[prev_move.prev_square.y][prev_move.prev_square.x].piece_short == prev_move.new_square.piece_short:
            return True
        return False