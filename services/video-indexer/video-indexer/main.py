import cv2
import numpy as np

from board_extractor import BoardExtractor
from image import Image
from board_arrow_detection import BoardArrowDetection
from board import Board
    
if __name__ == "__main__":
    # image = Image(cv2.imread('../images/no_board.png'))
    image = Image(cv2.imread('../images/arrow_test_image3.png'))
    image.displayBGRImage("Original")
    image.removePreviousAndCurrentMoveAssistanceSquares(black_assist_square_lower=np.array([25, 150, 70]), black_assist_square_upper=np.array([28, 255, 255]), white_assist_square_lower=np.array([25, 120, 70]),white_assist_square_upper=np.array([40, 140, 255]))
    image.displayBWImage("BW")
    board_Extractor = BoardExtractor(image)
    board_Image = board_Extractor.extract()

    if(board_Image is not None):
        board_Arrow_Detector = BoardArrowDetection(board_Image)
        board_Arrow_Detector.boardArrowDetect()
        board = Board(board_Image)
    else:
        print("No board found")