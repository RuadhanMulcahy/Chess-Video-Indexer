from selenium import webdriver
import time

from chessdotcom import actions
from chessdotcom.label_game import label_game
from darknetconvert import create_training_data_file_structure
from chessdotcom.changeboardstyle import change_board_style
from chessdotcom.actions import get_game_ids
from flags import flags
from chessdotcom.xpaths import xpaths

driver_location = "/snap/bin/chromium.chromedriver"
binary_location = "/usr/bin/chromium-browser"

options = webdriver.ChromeOptions()
options.binary_location = binary_location
options.add_argument("--user-data-dir=./user_data")

driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.maximize_window()

create_training_data_file_structure()

game_ids, game_ids_with_username = get_game_ids(driver, '2016ratman2016')

flags['highlight'] = False

game_index = 0

board_styles_to_use = [1, 2, 3, 4, 6, 7, 8, 11, 12, 22, 23, 28, 30]

for style in board_styles_to_use:
    flags['train_or_val'] = "train"

    change_board_style(driver, style)
    
    for index in range(10):   
        flags['game_id'] = game_ids[game_index]
        flags['game_id_with_username'] = game_ids_with_username[game_index]
        if index == 7:
            flags['train_or_val'] = "val"
        if game_index == len(game_ids) - 1:
            game_index = 0

        driver.get(f"https://www.chess.com/game/live/{flags['game_id_with_username']}")
        time.sleep(2)
        actions.click_element(driver, xpaths['end_game_pop_up'])
        actions.click_element(driver, xpaths['game_start'])
        label_game(driver, str(style))
        game_index += 1