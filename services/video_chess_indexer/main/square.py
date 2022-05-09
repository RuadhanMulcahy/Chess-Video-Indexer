from piece_id_lookups import id_to_short
from piece_id_lookups import id_to_verbose

class Square:
    highlighted = False
    piece_short = ''
    piece_verbose = ''

    def set(self, piece_id):
        if piece_id == '12':
            self.highlighted = True
        else:
            self.piece_short = id_to_short[piece_id]
            self.piece_verbose = id_to_verbose[piece_id]
            


