from square import Square

class Board:
    def __init__(self):
        self.squares = []
        self.create()

    def create(self):
        """
        Creates 8x8 Square list
        """
        for row in range(8):
            row = []
            for square in range(8):
                row.append(Square())
            self.squares.append(row)

    def show(self):
        """
        Shows chessboard (For debugging purposes)
        """
        print("_________________________")
        for row in self.squares:
            for square in row:
                if square.piece_short != '':
                    print(f" {square.piece_short} ", end='')
                else:
                    print('[  ]', end='')
            print(end='\n')

    def show_highlighted(self):
        """
        Shows chessboard highlight squares (For debugging purposes)
        """
        print("_________________________")
        for row in self.squares:
            for square in row:
                if square.highlighted is True:
                    print(f"{str(1)}  ", end='')
                else:
                    print(f"{str(0)}  ", end='')
            print(end='\n')
            
