import os
import shutil

def remove_old_label_file():
    shutil.rmtree('./files/results/result', ignore_errors=True)
    
def read_label_file(path):
    labels = []
    with open(path) as file:
        for line in file:
            split_line = line.rstrip().split(" ")
            labels.append(split_line)

    return labels