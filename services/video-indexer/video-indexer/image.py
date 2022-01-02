import cv2
import numpy as np

class Image:
    def __init__(self, image, image_HSV=None, image_GreyScale=None, image_BW=None):
        self.image = image

        if image_HSV is None:
            self.image_HSV = self._convertImageToHSV()
        else:
            self.image_HSV = image_HSV

        if image_GreyScale is None:
            self.image_GreyScale = self._imageToGreyscale()
        else:
            self.image_GreyScale = image_GreyScale

        if image_BW is None:
            self.image_BW = self._imageToBlackWhite()
        else:
            self.image_BW = image_BW

    def _imageToGreyscale(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def _imageToBlackWhite(self):
        return cv2.threshold(self.image_GreyScale, 180, 255, cv2.THRESH_BINARY)[1]
        # return cv2.threshold(self._greyscale, 146, 100, cv2.THRESH_BINARY)[1]

    def _convertImageToHSV(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

    def removePreviousAndCurrentMoveAssistanceSquares(self, black_assist_square_lower, black_assist_square_upper, white_assist_square_lower, white_assist_square_upper):
        black_assist_square_mask = cv2.inRange(self.image_HSV, black_assist_square_lower, black_assist_square_upper)
        white_assist_square_mask = cv2.inRange(self.image_HSV, white_assist_square_lower, white_assist_square_upper)
        self.image_BW[np.where(black_assist_square_mask!=0)] = [0]
        self.image_BW[np.where(white_assist_square_mask!=0)] = [255]

    def _cropImage(self, y, h, x, w):
        image = self.image[y:y+h, x:x+w]
        image_HSV = self.image_HSV[y:y+h, x:x+w]
        image_GreyScale = self.image_GreyScale[y:y+h, x:x+w]
        image_BW = self.image_BW[y:y+h, x:x+w]

        return {'image' : image, 'image_HSV' : image_HSV, 'image_GreyScale' : image_GreyScale, 'image_BW': image_BW}

    def cropCurrentImage(self, y, h, x, w):
        cropped_image_obj = self._cropImage(y, h, x, w)
        self.image = cropped_image_obj['image']
        self.image_HSV = cropped_image_obj['image_HSV']
        self.image_GreyScale = cropped_image_obj['image_GreyScale']
        self.image_BW = cropped_image_obj['image_BW']

    def getCroppedImage(self, y,h,x,w):
        return self._cropImage(y, h, x, w)

    def _displayImage(self, name, image, destroy_windows):
        cv2.imshow(name, image)

        if destroy_windows is not True:
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def displayHSVImage(self, name, **kwargs):
        self._displayImage(name, self.image_HSV, kwargs.get('destroy_windows'))

    def displayBGRImage(self, name, **kwargs):
        self._displayImage(name, self.image, kwargs.get('destroy_windows'))

    def displayBWImage(self, name, **kwargs):
        self._displayImage(name, self.image_BW, kwargs.get('destroy_windows'))
