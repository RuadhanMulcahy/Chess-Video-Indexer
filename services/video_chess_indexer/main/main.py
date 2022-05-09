from yolov5.detect import run

from file_handler import read_label_file, remove_old_label_file
from convert import Convert

remove_old_label_file()
run(weights='./files/model/best.pt', source='./files/images/test8.png', name='../../../files/results/result', save_txt=True ,imgsz=(400,400))

convert = Convert(read_label_file("./files/results/result/labels/test8.txt"))
convert.go()
convert.board.show()
