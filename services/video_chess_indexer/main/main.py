from yolov5.detect import run

from file_handler import read_label_file, remove_old_label_file
from convert import Convert

image_name = 'test5'

remove_old_label_file()
run(weights='./files/model/best.pt', source=f'./files/images/{image_name}.png', name='../../../files/results/result', conf_thres=0.2 ,save_txt=True ,imgsz=(400,400))

convert = Convert(read_label_file(f"./files/results/result/labels/{image_name}.txt"))
convert.go()
convert.board.show()
