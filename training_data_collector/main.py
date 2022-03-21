from selenium import webdriver
from chessdotcom import actions
import time

driver_location = "/snap/bin/chromium.chromedriver"
binary_location = "/usr/bin/chromium-browser"

options = webdriver.ChromeOptions()
options.binary_location = binary_location
options.add_argument("--user-data-dir=./user_data")

driver = webdriver.Chrome(executable_path=driver_location, options=options)
# driver.set_window_size(1280,720)
driver.get("https://www.chess.com/game/live/40420840437")

actions.closeEndGamePopUp(driver)
actions.goToGameStart(driver)

for i in range(0, 4):
    actions.nextMove(driver)

time.sleep(1)
actions.takeScreenShot(driver)

i = 1
while(True):
    try:
        actions.findLocateElement(driver, '//*[@id="board-dailyGame-40420840437"]/div[' + str(i) + ']')
    except:
        print(i)
        break
    i += 1

