from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import cv2

def closeEndGamePopUp(driver):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="board-layout-chessboard"]/div[3]/div/div[1]/button'))).click()

def _clickElement(driver, path):
    driver.find_element(By.XPATH, path).click()

def goToGameStart(driver):
    _clickElement(driver, '//*[@id="board-layout-sidebar"]/div/div[2]/div[1]/div[4]/div[3]/div/div[2]/button[1]')

def nextMove(driver):
    _clickElement(driver, '//*[@id="board-layout-sidebar"]/div/div[2]/div[1]/div[4]/div[3]/div/div[2]/button[3]')

def findLocateElement(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    size = element.size
    w, h = size['width'], size['height']
    print(element.get_attribute("class"))
    screenshot = cv2.imread("screenshot.png")
    cv2.rectangle(screenshot,  (element.location['x'] + w, element.location['y'] + h), (element.location['x'], element.location['y']), (0,255,0), 2)
    cv2.imwrite('screenshot.png', screenshot)
    
def takeScreenShot(driver, fname):
    driver.save_screenshot(fname)