from square import Square

class Board:
    squares = []

    def __init__(self):
        self.create()

    def create(self):
        for row in range(8):
            row = []
            for square in range(8):
                row.append(Square())
            self.squares.append(row)

    def show(self):
        print("_________________________")
        for row in self.squares:
            for square in row:
                if square.piece_short != '':
                    print(f" {square.piece_short} ", end='')
                else:
                    print('[  ]', end='')
            print(end='\n')

    def show_highlighted(self):
        print("_________________________")
        for row in self.squares:
            for square in row:
                print(square.highlighted, end='')
            print(end='\n')
