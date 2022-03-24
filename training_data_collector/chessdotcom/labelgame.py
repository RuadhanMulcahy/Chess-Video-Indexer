from selenium.webdriver.common.by import By
import cv2
import os
import shutil

from chessdotcom import actions
from darknetconvert import convert_co_ords_to_darknet

def label_game(driver, game_id):
    gameName = game_id
    moveCount = actions.get_move_count(driver)

    for x in range(1, moveCount + 1):
        label_board(driver, x, gameName, game_id)
        actions.next_move(driver)  
    label_board(driver, x + 1, gameName, game_id)
    # label_board(driver, 1, gameName, game_id)

def label_board(driver, move, gameName, game_id):
    moveName = 'move_' + str(move)
    fullName = gameName + '_' + moveName
    print('training_data/images/train/' + fullName + '.png')
    actions.take_screenshot(driver, 'training_data/images/train/' + fullName + '.png')
    label_element(driver, '//*[@id="board-dailyGame-' + game_id + '"]', fullName)
    i = 1 
    while(True):
        try:
            label_element(driver, '//*[@id="board-dailyGame-' + game_id + '"]/div[' + str(i) + ']', fullName)
        except:
            break
        i += 1

def label_element(driver, xpath, file_name):
    element = driver.find_element(By.XPATH, xpath)
    size = element.size
    w, h = size['width'], size['height']

    screenshot = cv2.imread('training_data/images/train/' + file_name + '.png')

    convert_co_ords_to_darknet(element, len(screenshot[0]), len(screenshot), 'training_data/labels/train', file_name)

    cv2.rectangle(screenshot,  (element.location['x'] + w, element.location['y'] + h), (element.location['x'], element.location['y']), (0,255,0), 2)
    cv2.imwrite('training_data/images/train/' + file_name + '.png', screenshot)
    