from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

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

def get_game_ids(driver, profile_name):
    game_ids_with_username = []
    game_ids = []

    base_url = f'https://www.chess.com/games/archive/{str(profile_name)}'
    driver.get(base_url)

    index= 1
    while(True):
        try:
            url = driver.find_element(By.XPATH, f'//*[@id="games-root-index"]/div[2]/table/tbody/tr[{index}]/td[1]/a').get_attribute('href')
            split_url = url.split('/')
            game_id_with_username = split_url[-1]
            game_id = game_id_with_username.split('?')[0]
            game_ids.append(game_id)
            game_ids_with_username.append(game_id_with_username)
        except NoSuchElementException as error:
            break
        index+=1
    return game_ids, game_ids_with_username