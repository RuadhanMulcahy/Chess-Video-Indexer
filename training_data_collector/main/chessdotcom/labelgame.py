from selenium.webdriver.common.by import By
import cv2

from chessdotcom import actions
from darknetconvert import convert_co_ords_to_darknet
from flags import flags
from image_enrichment import enrich_image

def label_game(driver):
    gameName = flags['game_id']
    moveCount = actions.get_move_count(driver)
    board_size = flags['min_board_size']

    for x in range(1, moveCount + 1):
        if board_size != flags['max_board_size']:
            board_size += flags['board_size_increment']
            # actions.change_board_size(driver, board_size)
        else:
            board_size = flags['min_board_size']
        label_board(driver, x, gameName)
        actions.next_move(driver)  
    label_board(driver, x + 1, gameName)

def label_board(driver, move_number, game_name):
    move_name = 'move_' + str(move_number)
    full_name = game_name + '_' + move_name
    print(f"training_data/images/{flags['train_or_val']}/{full_name}.png")
    actions.take_screenshot(driver, f"training_data/images/{flags['train_or_val']}/{full_name}.png")
    label_element(driver, f"//*[@id='board-dailyGame-{flags['game_id']}']", full_name)
    i = 1 
    while(True):
        try:
            label_element(driver, f"//*[@id='board-dailyGame-{flags['game_id']}']/div[{str(i)}]", full_name)
        except:
            break
        i += 1

def label_element(driver, xpath, file_name):
    element = driver.find_element(By.XPATH, xpath)
    size = element.size
    w, h = size['width'], size['height']

    screenshot = cv2.imread(f"training_data/images/{flags['train_or_val']}/{file_name}.png")
    
    if element.get_attribute('class') == 'board':
        enrich_image(element, screenshot)
        pass

    # convert_co_ords_to_darknet(element, len(screenshot[0]), len(screenshot), f'training_data/labels/{flags.train_or_val}', file_name)

    # if flags.highlight is True:
    #     cv2.rectangle(screenshot,  (element.location['x'] + w, element.location['y'] + h), (element.location['x'], element.location['y']), (0,255,0), 2)
    #     cv2.imwrite(f'training_data/images/{flags.train_or_val}/{file_name}.png', screenshot)
    
    