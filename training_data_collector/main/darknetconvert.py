import pathlib

def create_folder(dir_name):
    path = pathlib.Path(dir_name)
    path.mkdir(parents=True, exist_ok=True)

def create_training_data_file_structure():
    folders = [
        'training_data',
        'training_data/images/train',
        'training_data/images/val',
        'training_data/labels/train',
        'training_data/labels/val'
    ]

    for folder in folders:
        create_folder(folder)

def write_label_to_file(file_name, label):
    f = open(file_name, "a")
    f.write(label)
    f.close()

def element_name_to_class_name(element_name):
    class_names = {
        'br' : 0,
        'bn' : 1,
        'bb' : 2,
        'bk' : 3,
        'bq' : 4, 
        'bp' : 5, 
        'wr' : 6,
        'wn' : 7,
        'wb' : 8,
        'wk' : 9,
        'wq' : 10,
        'wp' : 11,
        'highlight square' : 12,
        'board flipped' : 13,
        'board' : 13
    }

    for class_name in class_names:
        if class_name in element_name:
            return class_names[class_name]

def convert_co_ords_to_darknet(image_w, image_h, element_w, element_h, element_x, element_y, class_name, path, game_name):
    percentage_x_center = (element_x + (element_w/2))/ image_w
    percentage_y_center = (element_y + (element_h/2))/ image_h
    percentage_width = element_w/image_w
    percentage_height = element_h/image_h

    if class_name != "element-pool" and class_name != "hover-square" and class_name != "board-images":
        label = f"{str(element_name_to_class_name(class_name))} {str(percentage_x_center)} {str(percentage_y_center)} {str(percentage_width)} {str(percentage_height)}"
        write_label_to_file(f"{path}/{game_name}.txt", label+"\n")
    else:
        pass
