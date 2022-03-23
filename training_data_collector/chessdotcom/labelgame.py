from selenium.webdriver.common.by import By
import cv2
import os
import shutil

from chessdotcom import actions
from darknetconvert import convert_co_ords_to_darknet

def label_game(driver, game_id):
    gameName = 'images/game1/'
    moveCount = actions.get_move_count(driver)

    try:
        shutil.rmtree('images/game1')
    except:
        pass
    os.mkdir(gameName)
    # for x in range(1, moveCount + 1):
    #     labelBoard(driver, x, gameName, game_id)
    #     actions.nextMove(driver)  
    # labelBoard(driver, x + 1, gameName, game_id)
    label_board(driver, 1, gameName, game_id)

def label_board(driver, move, gameName, game_id):
    fileName = 'move_' + str(move) + '.png'
    actions.take_screenshot(driver, gameName + fileName)
    label_element(driver, '//*[@id="board-dailyGame-' + game_id + '"]', gameName, fileName)
    i = 1 
    while(True):
        try:
            label_element(driver, '//*[@id="board-dailyGame-' + game_id + '"]/div[' + str(i) + ']', gameName, fileName)
        except:
            break
        i += 1

def label_element(driver, xpath, gameName, fileName):
    element = driver.find_element(By.XPATH, xpath)
    size = element.size
    w, h = size['width'], size['height']

    screenshot = cv2.imread(gameName + fileName)

    convert_co_ords_to_darknet(element, len(screenshot[0]), len(screenshot[0]))

    cv2.rectangle(screenshot,  (element.location['x'] + w, element.location['y'] + h), (element.location['x'], element.location['y']), (0,255,0), 2)
    cv2.imwrite(gameName + fileName, screenshot)
    