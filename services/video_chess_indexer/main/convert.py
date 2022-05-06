from torch import square
import numpy as np
    
class Convert:
    def __init__(self, board_x_center, board_y_center, board_w, board_h, labels):
        self.square_w = board_w / 8
        self.square_h = board_h / 8

        self.top_corner_square_x_center = (board_x_center - (board_w / 2)) + self.square_w / 2
        self.top_corner_square_y_center = (board_y_center - (board_h / 2)) + self.square_h / 2

        self.labels = labels
        self.board = np.zeros((8,8))

    def convert_darknet_to_chess_pos(self, x_center, y_center):
        x_pos = round((x_center - self.top_corner_square_x_center) / self.square_w)
        y_pos = round((y_center - self.top_corner_square_y_center) / self.square_h)
        return x_pos, y_pos

    def go(self):
        for label in self.labels:
            if label[0] != '13':
                x_pos, y_pos = self.convert_darknet_to_chess_pos(float(label[1]), float(label[2]))
                print(label[0])
                self.board[y_pos, x_pos] = int(label[0])

        return self.board

labels = []

with open("./files/results/result/labels/test10.txt") as file:
    for line in file:
        split_line = line.rstrip().split(" ")
        labels.append(split_line)

for label in labels:
    if label[0] == '13':
        convert = Convert(float(label[1]), float(label[2]), float(label[3]), float(label[4]), labels)
        board = convert.go()

print(board)
























# # for row in square_locations:
# #     print(row)

# from torch import square


# def convert(label_x_center, label_y_center, square_locations):
#     smallest_x_dif = 1.0
#     smallest_y_dif = 1.0

#     x_best_match = 0
#     y_best_match = 0

#     y_pos = 0

#     for x_pos, square in enumerate(square_locations[4]):
#         x_center = square[0]
#         y_center = square[1]

#         current_x_dif = label_x_center - x_center
#         current_y_dif = label_y_center - y_center
#         print(current_x_dif)
#         print(current_y_dif)

#         if(current_x_dif < smallest_x_dif and current_x_dif > 0):
#             print("ran")
#             smallest_x_dif = current_x_dif
#             x_best_match = x_pos

#         if(current_y_dif < smallest_y_dif and current_y_dif > 0):
#             smallest_y_dif = current_y_dif
#             y_best_match = y_pos

#     print(f"{x_best_match} {y_best_match}")
    

# def locate_squares(board_x_center, board_y_center, board_w, board_h):
#     square_locations = []

#     square_w = board_w / 8
#     square_h = board_h / 8

#     top_corner_square_x_center = (board_x_center - (board_w / 2)) + square_w / 2
#     top_corner_square_y_center = (board_y_center - (board_h / 2)) + square_h / 2

#     for row_index in range(0,8):
#         row = []
#         current_square_y_center = top_corner_square_y_center + (float(row_index) * square_h)
        
#         for col_index in range(0, 8):
#             square_x_y = []
#             current_square_x_center = top_corner_square_x_center + (float(col_index) * square_w)
#             square_x_y.append(current_square_x_center)
#             square_x_y.append(current_square_y_center)
#             row.append(square_x_y)
#         square_locations.append(row)
#     return square_locations

# square_locations = locate_squares(0.109766, 0.560417, 0.559375, 0.988889)
# # print(square_locations[0])

# convert(0.457812, 0.0645833, square_locations)

# # # for row in square_locations:
# # #     print(row)