import cv2

from board_extractor import BoardExtractor
from image import Image
    
if __name__ == "__main__":
    # image = Image(cv2.imread('../images/no_board.png'))
    image = Image(cv2.imread('../images/arrow_test_image.png'))
    image.displayImage("original")
    board_extractor = BoardExtractor(image)
    
    board = board_extractor.extract()
    if(board is not None):
        board = Image(board)
        board.displayImage("cropped")
    else:
        print("No board found")