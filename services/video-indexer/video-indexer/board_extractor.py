import numpy as np

class BoardExtractor:
    def __init__(self, image):
        self.image = image

    # Converts binary image row to array of matching pixels ie. [255,255,255,0,0] becomes [3,2]
    def _imageRowToBlackWhiteCountArray(self, image_row):
        white_count = 0
        black_count = 0
        black_white_count_array = np.array([],dtype=int)

        for pixel in image_row:
            if pixel == 0:
                if white_count != 0:
                    black_white_count_array = np.append(black_white_count_array, white_count)
                    white_count = 0
                black_count += 1    
            else:
                if black_count != 0:
                    black_white_count_array = np.append(black_white_count_array,black_count)
                    black_count = 0
                white_count += 1

        if white_count != 0:
            black_white_count_array = np.append(black_white_count_array, white_count)
        else:
            black_white_count_array = np.append(black_white_count_array, black_count)
        return black_white_count_array

    # Detects a board pattern in an image row
    def _horizontalBoardDetect(self, black_white_count_array, min_square_size):
        check = False
        same_count = 0

        for i in range(0, len(black_white_count_array) - 1):
            if self._isNextValueSimilarToCurrentValue(black_white_count_array[i], black_white_count_array[i+1]) == True:
                min = black_white_count_array[i]
                max = black_white_count_array[i]
                check = True

            if check is True:
                if black_white_count_array[i] > max:
                    max = black_white_count_array[i]
                elif black_white_count_array[i] < min:
                    min = black_white_count_array[i]

                if (max - min) <= 2 and min > min_square_size:
                    same_count += 1
                    if same_count == 7 and black_white_count_array[i+1] >= min:
                        avg = min + (max - min)
                        board_compressed = np.append(black_white_count_array[i-6:i+1], avg)
                        x_axis_start = np.sum(black_white_count_array[0:i-6], axis=0)
                        board_size = np.sum(board_compressed, axis=0)
                        return x_axis_start, board_size
                else:
                    min = 0
                    max = 0
                    same_count = 0
                    check = False
        
        return 0,0

    # Check if next value is within the threshhold of the current value    
    def _isNextValueSimilarToCurrentValue(self,current_value, next_value):
        if current_value in (next_value - 1, next_value, next_value + 1):
            return True
        else: 
            return False

    # Extracts board from image if one is found
    def extract(self):
        for y, i in enumerate(self.image.black_white):
            x, board_size = self._horizontalBoardDetect(self._imageRowToBlackWhiteCountArray(i), 20)
            if x != 0 and board_size != 0:
                cropped_image = self.image.cropImage(y,board_size,x,board_size)
                return cropped_image