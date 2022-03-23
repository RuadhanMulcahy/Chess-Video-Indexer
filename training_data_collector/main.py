from selenium import webdriver

from chessdotcom import actions
from chessdotcom.labelgame import label_game

driver_location = "/snap/bin/chromium.chromedriver"
binary_location = "/usr/bin/chromium-browser"

options = webdriver.ChromeOptions()
options.binary_location = binary_location
options.add_argument("--user-data-dir=./user_data")

driver = webdriver.Chrome(executable_path=driver_location, options=options)
# driver.set_window_size(1280,720)
game_id = "40420840437"
driver.get("https://www.chess.com/game/live/" + str(game_id))
# driver.get('https://www.chess.com/game/live/39383330409')

actions.close_end_game_pop_up(driver)
actions.go_to_game_start(driver)

label_game(driver, game_id)
