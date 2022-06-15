import os
import datetime
import time
from video_handler import download_youtube_video

from yolov5.detect import run

from file_handler import read_label_file, remove_old_label_file
from convert import Convert
from game_handler import GameHandler

video_name = '0'

# download_youtube_video('https://www.youtube.com/watch?v=zFViSKSOgs0')
# remove_old_label_file()
# run(weights='./files/model/best.pt', source=f'./files/videos/{video_name}.mp4', name='../../../files/results/result', conf_thres=0.2 ,save_txt=True ,imgsz=(400,400), save_conf=True)

def extract_integer(filename):
    return int(filename.split('_')[1].split('.')[0])

file_names = sorted(os.listdir('./files/results/result/labels'), key=extract_integer)
game_handler = GameHandler()

for file_name in file_names:
    convert = Convert(read_label_file(f"./files/results/result/labels/{file_name}"))
    board = convert.go()
    if board:
        # board.show_highlighted()
        # board.show()
        # time.sleep(1)
        # print(file_name)
        seconds = extract_integer(file_name) / 30
        # print(str(datetime.timedelta(seconds=seconds)))
        if game_handler.read_position(board, datetime.timedelta(seconds=seconds)) is False:
            break

# # print("NOT IN SCOPE")
# # print(i)