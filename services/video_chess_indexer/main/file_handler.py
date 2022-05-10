import os
import shutil

def remove_old_label_file():
    """
    Removes and existing detection results
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
            labels.append(split_line)
    return labels