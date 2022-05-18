from square import Square

class Board:
    _board_start = [
                    ['0','1','2','4','3','2','1','0'], 
                    ['5','5','5','5','5','5','5','5'],
                    ['11','11','11','11','11','11','11','11'],
                    ['6','7','8','10','9','8','7','6']
                ]

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

    def create_game_start(self, flipped):
        """
        Populates board with starting position - for either unflipped or flipped
        """
        starting_indexes = [0,1,6,7]

        if flipped:
            starting_indexes = list(reversed(starting_indexes))
            self._board_start[0] = list(reversed(self._board_start[0]))
            self._board_start[3] = list(reversed(self._board_start[3]))

        for index, row in enumerate(starting_indexes):
            for square in range(8):
                self.squares[row][square].set(self._board_start[index][square], 0)          

    def compare(self, board_to_compare):
        """
        Compares current board with another board
        """
        for row in range(8):
            for square in range(8):
                if self.squares[row][square].piece_short != board_to_compare.squares[row][square].piece_short:
                    return False
        return True

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
            