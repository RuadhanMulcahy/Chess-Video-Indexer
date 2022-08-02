class HighlightSquares:
    def valid(self, board):
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

    def check_for_highlight_change(self, current_board, last_valid_board):
        if current_board.compare(last_valid_board, True) == False:
            return True
        return False