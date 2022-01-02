from square import Square
from image import Image

class Board:
    squares = []

    def __init__(self, board_image):
        self.board_image = board_image
        self.createBoard()
    
    def createBoard(self):
        self.board_image.displayBGRImage("Original")
        square_size = len(self.board_image.image) / 8
        
        for i in range(0, 8):
            square_row = []
            for x in range(0, 8):
                square_image = Image(self.board_image.getCroppedImage(int(square_size*i),int(square_size),int(square_size*x),int(square_size))['image'])
                square = Square(square_image)
                square_row.append(square)
            self.squares.append(square_row)

        self.squares[0][2].square_image.displayBGRImage("Test")