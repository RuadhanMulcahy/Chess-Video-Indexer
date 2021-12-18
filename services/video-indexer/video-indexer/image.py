import cv2

class Image:
    def __init__(self, image):
        self.image = image
        self._greyscale = self._imageToGreyscale()
        self.black_white = self._imageToBlackWhite()

    def _imageToGreyscale(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def _imageToBlackWhite(self):
        return cv2.threshold(self._greyscale, 180, 255, cv2.THRESH_BINARY)[1]

    def cropImage(self, y,h,x,w):
        return self.image[y:y+h, x:x+w]

    def displayImage(self, name):
        cv2.imshow(name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
