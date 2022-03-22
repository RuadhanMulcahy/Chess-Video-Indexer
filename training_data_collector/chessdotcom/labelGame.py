from selenium.webdriver.common.by import By
import cv2
import os

from chessdotcom import actions

def labelGame(driver, game_id):
    gameName = 'images/game1/'
    moveCount = len(driver.find_elements(By.XPATH, '//*[@id="move-list"]/vertical-move-list/div'))
    endMove = len(driver.find_elements(By.XPATH, '//*[@id="move-list"]/vertical-move-list/div[' + str(moveCount) +']/div'))
    if(endMove < 3):
        moveCount = (moveCount * 2) - 2
    else:
        moveCount = (moveCount * 2) - 1      

    os.mkdir(gameName)
    for x in range(1, moveCount + 1):
        labelBoard(driver, x, gameName, game_id)
        actions.nextMove(driver)  
    labelBoard(driver, x + 1, gameName, game_id)
    # labelBoard(driver, 1, gameName, game_id)

def labelBoard(driver, move, gameName, game_id):
    fileName = 'move_' + str(move) + '.png'
    actions.takeScreenShot(driver, gameName + fileName)
    labelElement(driver, '//*[@id="board-dailyGame-' + game_id + '"]', gameName, fileName)
    i = 1 
    while(True):
        try:
            labelElement(driver, '//*[@id="board-dailyGame-' + game_id + '"]/div[' + str(i) + ']', gameName, fileName)
        except:
            break
        i += 1

def labelElement(driver, xpath, gameName, fileName):
    element = driver.find_element(By.XPATH, xpath)
    size = element.size
    w, h = size['width'], size['height']
    # print("width: " + str(w))
    # print("height: " + str(h))
    # print("x: " + str(element.location['x']))
    # print("y: " + str(element.location['y']))
    # print(element.get_attribute("class"))
    screenshot = cv2.imread(gameName + fileName)
    cv2.rectangle(screenshot,  (element.location['x'] + w, element.location['y'] + h), (element.location['x'], element.location['y']), (0,255,0), 2)
    cv2.imwrite(gameName + fileName, screenshot)