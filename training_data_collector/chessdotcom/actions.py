from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from chessdotcom.xpaths import XPaths

def _click_element(driver, path):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, path))).click()

def close_end_game_pop_up(driver):
    _click_element(driver, XPaths.end_game_pop_up)

def go_to_game_start(driver):
    _click_element(driver, XPaths.game_start)

def next_move(driver):
    _click_element(driver, XPaths.next_move)
    
def take_screenshot(driver, fname):
    driver.save_screenshot(fname)

def get_move_count(driver):
    moveCount = len(driver.find_elements(By.XPATH, XPaths.move_list))
    endMove = len(driver.find_elements(By.XPATH, XPaths.move_list + '[' + str(moveCount) +']/div'))
    if(endMove < 3):
        moveCount = (moveCount * 2) - 2
    else:
        moveCount = (moveCount * 2) - 1      

    return moveCount
    