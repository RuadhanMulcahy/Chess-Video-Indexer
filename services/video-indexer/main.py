from board_extractor import BoardExtractor
from image import Image
import cv2

def main():
    image = Image(cv2.imread('./images/test_image.jpg'))
    image.displayImage("original")
    board_extractor = BoardExtractor(image)
    board = Image(board_extractor.extract())
    board.displayImage("cropped")
    
if __name__ == "__main__":
    main()