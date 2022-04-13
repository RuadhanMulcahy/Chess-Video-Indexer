from selenium import webdriver

from chessdotcom import actions
from chessdotcom.labelgame import label_game
from darknetconvert import create_training_data_file_structure
from flags import flags
import time

flags['highlight'] = False
flags['train_or_val'] = "train"
flags['game_id'] = "39267621487"

driver_location = "/snap/bin/chromium.chromedriver"
binary_location = "/usr/bin/chromium-browser"

options = webdriver.ChromeOptions()
options.binary_location = binary_location
options.add_argument("--user-data-dir=./user_data")

driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.set_window_position(-1000, 0)
driver.maximize_window()
create_training_data_file_structure()
driver.get(f"https://www.chess.com/game/live/{flags['game_id']}")

actions.close_end_game_pop_up(driver)
actions.go_to_game_start(driver)

label_game(driver)
