from board import Board
from move import Move

class Game:
    def __init__(self):
        self.board = Board()
        self.last_valid_move = Move()
        self.last_valid_board = Board()
        self.last_color = None
        self.flipped = None
        self.create_game_starts()
        self.move_count = 0
        self.same_count = 0   
        self.moves = []
        self.prev_valid_time_stamp = 0

    def read_position(self, board, time_stamp):
        self.check_for_game_start(board)

        if self.prev_valid_time_stamp is None:
            self.prev_valid_time_stamp = time_stamp

        if self.move_count < 200:
            if self.valid_highlight_squares(board): 
                if board.compare(self.last_valid_board, True) == False and self.same_count >= 10:    
                    self.last_valid_board.show_highlighted()
                    move = self.get_move(self.last_valid_board, self.prev_valid_time_stamp)
                    move.show()
                    self.move_count+=1
                    self.same_count = 0
                    self.prev_valid_time_stamp = time_stamp
                self.last_valid_board = board
                self.same_count += 1
            return True     
        return False

    def get_move(self, board, time_stamp):
        move = Move(self.flipped)
        move.time_stamp = time_stamp
        for row in board.squares:
            for square in row:
                if square.highlighted and square.piece_short != '':
                    move.new_square = square
                    move.color = square.color
                elif square.highlighted and square.piece_short == '':
                    move.prev_square = square
        return move

    def valid_highlight_squares(self, board):
        highlighted_piece_count = 0
        highlighted_empty_count = 0
        for x, row in enumerate(board.squares):
            for y, square in enumerate(row):
                if square.highlighted == True and square.piece_short != '':
                    highlighted_piece_count += 1
                elif square.highlighted == True and square.piece_short == '':
                    highlighted_empty_count += 1
                if highlighted_piece_count > 1 or highlighted_empty_count > 1:
                    return False
        if highlighted_empty_count == 1 and highlighted_piece_count == 1:
            return True
        return False

    def check_for_position_change(self):
        if self.board_prev is None and self.board is not None:
            return True
        if self.board.compare(self.board_prev, False) == False:
            return True
        return False

    def check_for_highlight_change(self):
        if self.board.compare(self.last_valid_board, True) == False:
            return True
        return False

    def get_move_redun(self):
        move = Move(self.board.flipped)
        highlight_count = 0
        for x, row in enumerate(self.board_prev.squares):
            for y, square in enumerate(row):
                    if square.highlighted == True and square.piece_short != '':
                        move.new_square = square
                        highlight_count += 1
                        print(f"highlighted full {x} {y}")
                    elif square.highlighted == True and square.piece_short == '':
                        move.prev_square = square
                        highlight_count += 1
                        print(f"highlighted empty {x} {y}")

        print(f"count: {highlight_count}")
        # self.board.show_highlighted()
        if move.new_square is not None and move.prev_square is not None and move.flipped is not None and highlight_count == 2:
            self.board_prev.show()
            self.board_prev.show_highlighted()
            print(highlight_count)
            # self.board.show_highlighted()
            move.show()
            print(f"Move: {self.move_count}")
            self.move_count+=1

    def create_game_starts(self):
        self.board_normal = Board()
        self.board_flipped = Board()

        self.board_normal.create_game_start(False)
        self.board_flipped.create_game_start(True)

    def check_for_game_start(self, board):
        if board.compare(self.board_normal, False):
            self.flipped = False
        elif self.board.compare(self.board_flipped, False):
            self.flipped = True


# from square import Square
# move1 = None
# move2 = Move(True)

# move1.new_square = Square(0,1)
# move1.prev_square = Square(0,2)

# move2.new_square = Square(0,2)
# move2.prev_square = Square(0,2)


# if move1 is None and move2 is not None or move1.new_square.compare(move2.new_square):
#     print("yes")
