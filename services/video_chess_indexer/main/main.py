from yolov5.detect import run

run(weights='./files/model/best.pt', source='./files/images/test10.png', name='../../../files/results/result', save_txt=True ,imgsz=(400,400))


