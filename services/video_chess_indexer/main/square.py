from piece_id_lookups import id_to_short
from piece_id_lookups import id_to_verbose

class Square:
    def __init__(self):
        self.highlighted = False
        self.piece_short = ''
        self.piece_verbose = ''

    def set(self, piece_id):
        """
        Takes in label id and sets appopriate values
        """
        if piece_id == '12':
            self.highlighted = True
        else:
            self.piece_short = id_to_short[piece_id]
            self.piece_verbose = id_to_verbose[piece_id]
            


