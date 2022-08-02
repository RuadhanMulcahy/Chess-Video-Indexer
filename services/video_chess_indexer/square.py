from re import X
from piece_id_lookups import id_to_short
from piece_id_lookups import id_to_verbose

class Square:
    def __init__(self, y, x):
        self.highlighted = False
        self.confidence = 0.0
        self.color = ''
        self.piece_short = ''
        self.piece_verbose = ''
        self.y = y
        self.x = x

    def compare(self, square):
        if self.x == square.x and self.y == square.y:
            return True
        return False

    def set_pgn(self, flipped):
        """
        Converts 2d array co-ords to pgn co-ords
        """
        x_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        
        if flipped:
            self.pgn_y = self.y + 1
            self.pgn_x = x_axis[(self.x * -1) - 1]
        else:
            self.pgn_y = (8 - self.y)
            self.pgn_x = x_axis[self.x]
        
    def set(self, piece_id, current_confidence):
        """
        Takes in label id and sets appropriate values
        """
        if piece_id == '12' and current_confidence >= 0.2:
            self.highlighted = True
        elif piece_id != '12' and current_confidence >= 0.4:
            if float(current_confidence) >= self.confidence:
                self.piece_short = id_to_short[piece_id]
                self.piece_verbose = id_to_verbose[piece_id]
                self.confidence = current_confidence
                self.color = self.extract_color(self.piece_short)
                
    def extract_color(self, piece_short):
        if piece_short[0] == 'w':
            return 'w'
        elif piece_short[0] == 'b':
            return 'b'
        return ''
    


