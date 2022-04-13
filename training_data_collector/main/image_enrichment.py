import cv2

def enrich_image(element, image):
    x, y = element.location['x'], element.location['y']
    w, h = element.size['width'], element.size['height']

    cropped_image = image[y:y+h, x:x+w]
    small = cv2.resize(cropped_image, (0,0), fx=0.2, fy=0.2) 

    background_image = cv2.imread('../background_images/2.png')

    x_offset=y_offset=50
    background_image[y_offset:y_offset+small.shape[0], x_offset:x_offset+small.shape[1]] = small

    cv2.imshow('', background_image)
    cv2.waitKey()
    cv2.destroyAllWindows()