from piece_id_lookups import id_to_short
from piece_id_lookups import id_to_verbose

class Square:
    def __init__(self):
        self.highlighted = False
        self.confidence = 0.0
        self.piece_short = ''
        self.piece_verbose = ''

    def set(self, piece_id, current_confidence):
        """
        Takes in label id and sets appropriate values
        """
        if piece_id == '12':
            self.highlighted = True
        else:
            if float(current_confidence) >= self.confidence:
                self.piece_short = id_to_short[piece_id]
                self.piece_verbose = id_to_verbose[piece_id]
            


