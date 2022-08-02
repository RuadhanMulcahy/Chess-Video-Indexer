from square import Square

class Board:
    _board_start = [
                    ['0','1','2','4','3','2','1','0'], 
                    ['5','5','5','5','5','5','5','5'],
                    ['11','11','11','11','11','11','11','11'],
                    ['6','7','8','10','9','8','7','6']
                ]

    def __init__(self):
        self.flipped = None
        self.squares = []
        self.create()

    def create(self):
        """
        Creates 8x8 Square list
        """
        for y in range(8):
            row = []
            for x in range(8):
                row.append(Square(y, x))
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
                self.squares[row][square].set(self._board_start[index][square], 1)     

    def is_match(self, board_to_compare, highlighted):
        """
        Checks if current board is the same as board_to_compare
        Returns true if board is match and False if not
        """
        if board_to_compare is None and len(self.squares) > 0:
            print(len(self.squares))
            return False

        for row in range(8):
            for square in range(8):
                if highlighted == False: 
                    if self.squares[row][square].piece_short != board_to_compare.squares[row][square].piece_short:
                        return False
                else:
                    if self.squares[row][square].highlighted != board_to_compare.squares[row][square].highlighted:
                        return False
                    if self.squares[row][square].highlighted and board_to_compare.squares[row][square].highlighted:
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
        count = 0
        print("_________________________")
        for row in self.squares:
            for square in row:
                if square.highlighted and square.piece_short != '':
                    print(f" {square.piece_short} ", end='')
                    count += 1
                elif square.highlighted and square.piece_short == '':
                    print(f" X  ", end='')
                    count += 1
                else:
                    print('[  ]', end='')
            print(end='\n')
        print(count)
