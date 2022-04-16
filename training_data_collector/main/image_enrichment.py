import cv2
import random

def enrich_image(element, image):

    for i in range(0, 5):
        x, y = element.location['x'], element.location['y']
        w, h = element.size['width'], element.size['height']

        scale = random.randint(0, 100) / 100
        print("scale: " + str(scale))
        cropped_image = image[y:y+h, x:x+w]
        # print("cropped_image_size: " + str(len(cropped_image)))
        scaled = cv2.resize(cropped_image, (0,0), fx=scale, fy=scale) 
        
        scaled_size = len(scaled)
        print("scaled_size: " + str(scaled_size))

        w = int(w * scale)
        h = int(h * scale)
        
        background_image = cv2.imread('../background_images/2.png')

        x_background_image_size = len(background_image[0])
        y_background_image_size = len(background_image)

        max_x_offset = x_background_image_size - scaled_size
        max_y_offset = y_background_image_size - scaled_size

        print("x_background_image_size: " + str(x_background_image_size))
        print("y_background_image_size: " + str(y_background_image_size))
        print("max_x_offset: " + str(max_x_offset))
        print("max_y_offset: " + str(max_y_offset))
        x_offset = random.randint(0, max_x_offset)
        y_offset = random.randint(0, max_y_offset)

        background_image[y_offset:y_offset+scaled.shape[0], x_offset:x_offset+scaled.shape[1]] = scaled

        cv2.rectangle(background_image,  (max_x_offset + w, max_y_offset + h), (max_x_offset, max_y_offset), (0,255,0), 2)
        cv2.imshow('test', background_image)
        cv2.waitKey()
        cv2.destroyAllWindows()