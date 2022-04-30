from chessdotcom.actions import click_element
from chessdotcom.xpaths import xpaths

def change_board_style(driver, option):
    url = 'https://www.chess.com/settings/board'
    driver.get(url)
    click_element(driver, f"{xpaths['board_style_list']}[{option}]")
    click_element(driver, f"{xpaths['save_board_style']}")
