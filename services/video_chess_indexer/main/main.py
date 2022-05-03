from yolov5.detect import run

run(weights='./model/best.pt', source='./files/images/test10.png', name='../../../files/results/result', imgsz=(400,400))
