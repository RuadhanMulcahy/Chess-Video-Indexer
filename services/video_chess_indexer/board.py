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
                self.squares[row][square].set(self._board_start[index][square], 0)     

    def compare(self, board_to_compare, highlighted):
        """
        Compares current board with another board
        """
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

    def compare_exact(self, board_to_compare):
        if board_to_compare is None and self.board is not None:
            return True
        elif self.compare(board_to_compare, False) and self.compare(board_to_compare, True):
            return True
        return False 

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

# board1 = Board()
# board2 = Board()

# board1.squares[0][1].piece_short = 'bn'
# board1.squares[0][1].highlighted = True

# board2.squares[0][1].piece_short = 'bn'
# board2.squares[0][1].highlighted = True

# print(board1.compare(board2, True))
