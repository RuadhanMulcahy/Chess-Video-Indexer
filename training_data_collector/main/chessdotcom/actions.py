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

def change_board_size(driver, width_height):
    board_style = driver.find_element(By.XPATH, XPaths.chess_board).get_attribute("style")
    print(board_style.split())
    board_style = board_style.split()
    width_height_formatted = f"{str(width_height)}px;"
    board_style[1] = width_height_formatted
    board_style[3] = width_height_formatted
    board_style = ' '.join(board_style)
    driver.execute_script(f"arguments[0].setAttribute('style','{board_style}')", driver.find_element(By.XPATH, XPaths.chess_board))


    