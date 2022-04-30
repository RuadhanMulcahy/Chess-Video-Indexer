import cv2
import random
import os

def enrich_image(element, original_image_path):
    image = cv2.imread(original_image_path)
    enriched_image = get_random_background()

    x, y = element.location['x'], element.location['y']
    w, h = element.size['width'], element.size['height']

    remaining_height = len(enriched_image) - h

    upper_limit = int(((remaining_height / h) * 100) + 100)

    lower_limit = 50
    scale = random.randint(lower_limit, upper_limit) / 100
    cropped_image = image[y:y+h, x:x+w]
    scaled_image = cv2.resize(cropped_image, (0,0), fx=scale, fy=scale) 
    
    scaled_size = len(scaled_image)

    w = int(w * scale)
    h = int(h * scale)

    x_background_image_size = len(enriched_image[0])
    y_background_image_size = len(enriched_image)

    max_x_offset = x_background_image_size - scaled_size
    max_y_offset = y_background_image_size - scaled_size
    x_offset = random.randint(0, max_x_offset)
    y_offset = random.randint(0, max_y_offset)

    enriched_image[y_offset:y_offset+scaled_image.shape[0], x_offset:x_offset+scaled_image.shape[1]] = scaled_image

    enriched_image_w = len(enriched_image[0])
    enriched_image_h = len(enriched_image)
    cv2.imwrite(original_image_path, enriched_image)

    return (scale, enriched_image_w, enriched_image_h, x_offset, y_offset, x, y)

def blur_image(image):
    blurred_image = cv2.GaussianBlur(image, (5,5), 0)
    return blurred_image

def get_random_background():
    background_images_folder = '../background_images'
    files = os.listdir(background_images_folder)
    index = random.randint(0, len(files) - 1)
    return cv2.imread(f'{background_images_folder}/{files[index]}')