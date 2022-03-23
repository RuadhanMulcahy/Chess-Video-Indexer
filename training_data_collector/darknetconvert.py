def write_label_to_file(fileName, label):
    f = open(fileName, "a")
    f.write(label)
    f.close()

def convert_co_ords_to_darknet(element, image_width, image_height):
    size = element.size
    w, h = size['width'], size['height']
    className = element.get_attribute("class")
    percentage_x_center = (element.location['x'] + (w/2))/ image_width
    percentage_y_center = (element.location['y'] + (h/2))/ image_height
    percentage_width = w/image_width
    percentage_height = h/image_height

    label = str(className) + " " + str(percentage_x_center) + " " + str(percentage_y_center) + " " + str(percentage_width) + " " + str(percentage_height)
    if className != "element-pool" and className != "hover-square":
        write_label_to_file('test.txt', label+"\n")
    else:
        pass
