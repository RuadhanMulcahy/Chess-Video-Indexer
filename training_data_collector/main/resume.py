import os
from flags import flags

def get_style_value(filename):
    return int(filename.split('_')[-1].split('.')[-2])

def get_last_board_style(files):
    max_option = 0

    for i in files:
        current_option = get_style_value(i)

        if current_option > max_option:
            max_option = current_option
    return max_option

def get_files_for_deletion(files, last_board_style):
    images_for_deletion = []
    labels_for_deletion = []

    for i in files:
        if get_style_value(i) == last_board_style:
            base_file_name = i.split('.')[-2]
            os.remove(base_file_name + '.png')
            images_for_deletion.append(base_file_name + '.png')
            labels_for_deletion.append(base_file_name + '.txt')
    return images_for_deletion, labels_for_deletion

# flags['train_or_val'] = 'train'
path = f"./training_data/images/{flags['train_or_val']}"

files = os.listdir(path)

last_option = get_last_board_style(files)

files_for_deletion, labels_for_deletion = get_files_for_deletion(files, last_option)

# print(files_for_deletion)
# print(labels_for_deletion)