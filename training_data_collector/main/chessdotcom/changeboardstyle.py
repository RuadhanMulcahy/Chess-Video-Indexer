from chessdotcom.actions import _click_element

def change_board_style(driver, option):
    url = 'https://www.chess.com/settings/board'
    driver.get(url)

    _click_element(driver, f'//*[@id="board_pieces_gameBoardColor"]/option[{option}]')
    _click_element(driver, f'//*[@id="board_pieces_save"]')
