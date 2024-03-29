from board import Board
from move import Move
from game import Game

class GameHandler:
    def __init__(self):
        self.create_game_starts()
        self.last_valid_board = Board()
        self.move_count = 0
        self.same_count = 0   
        self.prev_valid_time_stamp = 0
        self.moves = []
        self.games = []
        self.game = Game()
        self.flipped = None

    def read_position(self, board, time_stamp):
        if self.check_for_game_start(board):
            if len(self.game.moves) > 0:
                self.games.append(self.game)
                self.game = Game()    
            if self.game.on_game_start == False:
                print(f"Gamestart: {str(time_stamp)}")
                self.game.game_start = time_stamp
            self.game.on_game_start = True
        else:
            self.game.on_game_start = False    

        # if self.prev_valid_time_stamp is None:
        #     self.prev_valid_time_stamp = time_stamp

        if self.move_count < 1000:
            if self.valid_highlight_squares(board): 
                if board.compare(self.last_valid_board, True) == False and self.same_count >= 10:    
                    move = self.get_move(self.last_valid_board, self.prev_valid_time_stamp)
                    self.game.add_move(move)
                    self.move_count += 1
                    self.same_count = 0
                    self.prev_valid_time_stamp = time_stamp
                self.last_valid_board = board
                self.same_count += 1
            return True     
        else:
            pass
            # self.game.show_game()
        return False


    def get_move(self, board, time_stamp):
        move = Move()
        move.time_stamp = time_stamp
        move.board = board
        for row in board.squares:
            for square in row:
                if square.highlighted and square.piece_short != '':
                    move.new_square = square
                    move.new_square.set_pgn(self.flipped)
                    move.color = square.color
                elif square.highlighted and square.piece_short == '':
                    move.prev_square = square
                    move.prev_square.set_pgn(self.flipped)
        return move

    def reverse_move_check(self):
        if self.move_count <= 1:
            return False
        prev_move = self.moves[self.move_count - 2]
        curr_move = self.moves[self.move_count -  1]
        if curr_move.board.squares[prev_move.prev_square.y][prev_move.prev_square.x].piece_short == prev_move.new_square.piece_short:
            return True
        return False
        
    def valid_highlight_squares(self, board):
        highlighted_piece_count = 0
        highlighted_empty_count = 0
        for row in board.squares:
            for square in row:
                if square.highlighted == True and square.piece_short != '':
                    highlighted_piece_count += 1
                elif square.highlighted == True and square.piece_short == '':
                    highlighted_empty_count += 1
                if highlighted_piece_count > 1 or highlighted_empty_count > 1:
                    return False
        if highlighted_empty_count == 1 and highlighted_piece_count == 1:
            return True
        return False

    def check_for_highlight_change(self):
        if self.board.compare(self.last_valid_board, True) == False:
            return True
        return False

    def create_game_starts(self):
        self.board_normal = Board()
        self.board_flipped = Board()
        self.board_normal.create_game_start(False)
        self.board_flipped.create_game_start(True)      

    def check_for_game_start(self, board):
        if board.compare(self.board_normal, False):
            self.flipped = False
            return True
        elif board.compare(self.board_flipped, False):
            self.flipped = True
            return True
        return False

    def end_game(self):
        self.games.append(self.game)
