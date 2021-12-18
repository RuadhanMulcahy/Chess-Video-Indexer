import cv2

from board_extractor import BoardExtractor
from image import Image
    
if __name__ == "__main__":
    image = Image(cv2.imread('../images/test_image2.png'))
    image.displayImage("original")
    board_extractor = BoardExtractor(image)

    if (board := board_extractor.extract() != None):
        board = Image(board)
        board.displayImage("cropped")
    else:
        print("No board found")