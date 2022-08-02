class Validate:
    def __init__(self):
        self.same_position_count = 0
        self.move_is_valid = False

    def position(self, board):
        if self.highlight_squares(board):
            if self.not_anomaly():
                self.move_is_valid = True
                self.same_position_count = 0

                return True
            self.same_position_count += 1                                                               
        return False

    def not_anomaly(self):
        anomaly_threshold = 15
        if self.same_position_count == anomaly_threshold:
            return True
        return False

    def for_new_position(self, last_valid_board, board):
        self.move_is_valid = False
        if last_valid_board is None and board is not None:
            return True
        if board.is_match(last_valid_board, True) == False:
            self.same_position_count = 0
            return True
        return False

    def highlight_squares(self, board):
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

    
