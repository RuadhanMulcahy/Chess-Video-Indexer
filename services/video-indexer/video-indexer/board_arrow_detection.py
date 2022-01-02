import cv2
import numpy as np

class BoardArrowDetection:
    def __init__(self, image):
        self.image = image

    def _convertImageToColorMask(self, lower, upper):
        mask = cv2.inRange(self.image.image_HSV, lower, upper)
        return mask

    def boardArrowDetect(self):
        orange_lower_HSV = np.array([20, 190, 50])
        orange_upper_HSV = np.array([21, 255, 255])
        mask = self._convertImageToColorMask(orange_lower_HSV, orange_upper_HSV)
        for i in mask:
            if 255 in i:
                print("Contains arrow")
                break