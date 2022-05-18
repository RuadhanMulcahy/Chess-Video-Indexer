import shutil

from label import Label

def remove_old_label_file():
    """
    Removes any existing detection results
    """
    shutil.rmtree('./files/results/result', ignore_errors=True)
    
def read_label_file(path):
    """
    Reads label file and saves it to a list
    """
    labels = []
    with open(path) as file:
        for line in file:
            split_line = line.rstrip().split(" ")
            labels.append(Label(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5]))
    return labels
