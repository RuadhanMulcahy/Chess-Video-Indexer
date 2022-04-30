from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import cv2

from chessdotcom import actions
from darknetconvert import convert_co_ords_to_darknet
from flags import flags
from image_enrichment import enrich_image
from chessdotcom.xpaths import xpaths

def label_game(driver, option):
    gameName = flags['game_id_with_username']
    moveCount = actions.get_move_count(driver)

    for x in range(1, moveCount + 1):
        label_board(driver, x, gameName, option)
        actions.click_element(driver, xpaths['next_move'])
    label_board(driver, x + 1, gameName, option)

def label_board(driver, move_number, game_name, option):
    move_name = f'move_{str(move_number)}'
    full_name = f'{game_name}_{move_name}_{option}'
    image_path = f"training_data/images/{flags['train_or_val']}/{full_name}.png"
    actions.take_screenshot(driver, image_path)

    board = driver.find_element(By.XPATH, f"//*[@id='board-dailyGame-{flags['game_id']}']")
    scale, image_w, image_h, x_offset, y_offset, old_x, old_y = enrich_image(board, image_path)
    label_element(driver, f"//*[@id='board-dailyGame-{flags['game_id']}']", image_path, image_w, image_h, full_name, scale, x_offset, y_offset, old_x, old_y)

    i = 1
    while(True):
        try:
            label_element(driver, f"//*[@id='board-dailyGame-{flags['game_id']}']/div[{str(i)}]", image_path, image_w, image_h, full_name, scale, x_offset, y_offset, old_x, old_y)
        except NoSuchElementException:
            break
        i += 1

def label_element(driver, xpath, image_path, image_w, image_h, file_name, scale, x_offset, y_offset, old_x, old_y):
    element = driver.find_element(By.XPATH, xpath)
    class_name = element.get_attribute("class")
    size = element.size
    w, h = size['width'], size['height']
    x, y = element.location['x'], element.location['y']

    distance_from_bord_corner_x = round((x - old_x) * scale)
    distance_from_bord_corner_y = round((y - old_y) * scale)

    scaled_w = round(w * scale)
    scaled_h = round(h * scale)

    transformed_x = x_offset + distance_from_bord_corner_x
    transformed_y = y_offset + distance_from_bord_corner_y
    convert_co_ords_to_darknet(image_w, image_h, scaled_w, scaled_h, transformed_x, transformed_y, class_name, f"training_data/labels/{flags['train_or_val']}", file_name)

    if flags['highlight'] is True:
        screenshot = cv2.imread(image_path)
        cv2.rectangle(screenshot, (transformed_x, transformed_y), (transformed_x + scaled_w ,transformed_y + scaled_h), (0,255,0), 2)
        cv2.imwrite(image_path, screenshot)
    
    