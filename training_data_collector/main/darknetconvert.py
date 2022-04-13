import pathlib

def create_folder(dir_name):
    path = pathlib.Path(dir_name)
    path.mkdir(parents=True, exist_ok=True)

def create_training_data_file_structure():
    create_folder('training_data')
    create_folder('training_data/images/train')
    create_folder('training_data/images/val')
    create_folder('training_data/labels/train')
    create_folder('training_data/labels/val')

def write_label_to_file(fileName, label):
    f = open(fileName, "a")
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
        'board' : 14
    }

    for class_name in class_names:
        if class_name in element_name:
            return class_names[class_name]

def convert_co_ords_to_darknet(element, image_width, image_height, path, gameName):
    size = element.size
    w, h = size['width'], size['height']
    className = element.get_attribute("class")
    percentage_x_center = (element.location['x'] + (w/2))/ image_width
    percentage_y_center = (element.location['y'] + (h/2))/ image_height
    percentage_width = w/image_width
    percentage_height = h/image_height

    if className != "element-pool" and className != "hover-square":
        label = str(element_name_to_class_name(className)) + " " + str(percentage_x_center) + " " + str(percentage_y_center) + " " + str(percentage_width) + " " + str(percentage_height)
        write_label_to_file(path + '/' + gameName + '.txt', label+"\n")
    else:
        pass
