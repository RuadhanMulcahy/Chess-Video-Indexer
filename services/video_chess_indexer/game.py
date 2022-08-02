from game_start import GameStart

class Game:
    def __init__(self, game_start=None):
        self.moves = []
        self.reverse_moves = []

    """
    Method for adding move to game
    """
    def add_move(self, move):
        if self._is_new_move(move):
            if self._is_reverse_move(move):
                reverse_move = self.moves[-1]
                self.reverse_moves.append(reverse_move)
                self.moves.pop()
            elif self._is_catch_up_move(move):
                self.moves.append(move)
                self.reverse_moves.pop()   
            elif self._is_catch_up_move(move) == False and len(self.reverse_moves) >= 1:
                self.show()
                return False
            else:
                self.moves.append(move)

        if len(self.moves) == 20:
            # self.show()
            return False

    """
    Method for checking if move is a reverse move
    """
    def _is_reverse_move(self, curr_move):
        if len(self.moves) == 0:
            return False
        prev_move = self.moves[-1]
        if curr_move.board.squares[prev_move.prev_square.y][prev_move.prev_square.x].piece_short == prev_move.new_square.piece_short:
            return True
        return False
    
    """
    Method for checking if move is a catch up move
    """

    def _is_catch_up_move(self, curr_move):
        if len(self.reverse_moves) == 0:
            return False

        if curr_move.is_match(self.reverse_moves[-1]):
            return True
        else:
            return False

    """
    Method for checking if move is different from previous move
    """
    def _is_new_move(self, move):
        if len(self.moves) < 1:
            return True
        if move.is_match(self.moves[-1]) == False:
            return True
        return False

    """
    Method that returns all moves in game
    """
    def get_game(self):
        return self.moves + self.reverse_moves

    """
    Method that returns moves for next game
    """
    def get_moves_for_next_game(self):
        return self.moves

    """
    Method for displaying all moves in game
    """
    def show(self):
        # for move in self.moves:
        #     move.show()
        moves = self.get_game()

        for index in range(0, 10):
            moves[index].show()


        
    