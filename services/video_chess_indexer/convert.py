from cv2 import threshold
from board import Board
    
class Convert:
    def __init__(self, labels):
        self.labels = labels

    def set_top_square_corner_x_y(self):
        """
        Sets the top left center square co-ordinates
        """
        self.top_corner_square_x_center = (self.board_x_center - (self.board_w / 2)) + self.square_w / 2
        self.top_corner_square_y_center = (self.board_y_center - (self.board_h / 2)) + self.square_h / 2

    def set_square_w_h(self):
        """
        Sets square width and height
        """
        self.square_w = self.board_w/8
        self.square_h = self.board_h/8

    def set_board_boundaries(self):
        """
        Sets the boundaries of the board
        """
        self.board_top = self.board_y_center - (self.board_h / 2)
        self.board_bottom = self.board_y_center + (self.board_h / 2)
        self.board_left = self.board_x_center - (self.board_w / 2)
        self.board_right = self.board_x_center + (self.board_w / 2)

    def is_label_within_board(self, x_center, y_center):
        """
        Checks if label is within the board boundaries
        """
        if x_center < self.board_left or x_center > self.board_right:
            return False
        elif y_center < self.board_top or y_center > self.board_bottom:
            return False
        else:
            return True

    def convert_darknet_to_chess_pos(self, x_center, y_center):
        """
        Converts darknet (x, y) coordinates to chess position
        """
        x_pos = round((x_center - self.top_corner_square_x_center) / self.square_w)
        y_pos = round((y_center - self.top_corner_square_y_center) / self.square_h)
        return x_pos, y_pos

    def get_board(self):
        """
        Gets the board label in the labels list and removes it from the labels list
        If 1 board is detected it returns True otherwise it returns False
        """
        board_count = 0
        board_label_index = 0

        for index, label in enumerate(self.labels):
            if label.id == '13':
                board_count += 1
                if self.is_square_shape(label.w, label.h):
                    self.board_x_center = label.x_center
                    self.board_y_center = label.y_center
                    self.board_w = label.w
                    self.board_h = label.h
                    board_label_index = index
                else:
                    return False

        if board_count == 1:
            del self.labels[board_label_index]
            return True
        else:
            return False

    def is_square_shape(self, darknet_w, darknet_h):
        """
        Checks if detected object is in shape square
        Compares width and height and checks if there is more than threshold percentage difference.
        If difference past threshold it returns False otherwise it returns True.
        """
        aspect_ratio_w = 16
        aspect_ratio_h = 9

        threshold = 0.02

        w = aspect_ratio_w * darknet_w
        h = aspect_ratio_h * darknet_h

        dif = 0.0
        if w > h:
            dif = (w - h) / w
        else:
            dif = (h - w) / h
        if dif > threshold:
            return False
        return True
                
    def go(self):
        """
        Orchestrates conversion of labels to chess pos array
        """
        if self.get_board():
            self.set_board_boundaries()
            self.set_square_w_h()
            self.set_top_square_corner_x_y()
            self.board = Board()
            
            for label in self.labels:
                if self.is_label_within_board(label.x_center, label.y_center):
                    x_pos, y_pos = self.convert_darknet_to_chess_pos(label.x_center, label.y_center)                     
                    self.board.squares[y_pos][x_pos].set(label.id, label.conf)
            return self.board

    def temp_debug(self):
        """
        For debugging purposes (Will be deleted)
        """
        print(f"board_top - {self.board_top}")
        print(f"board_bottom - {self.board_bottom}")
        print(f"board_left - {self.board_left}")
        print(f"board_right - {self.board_right}")

# from file_handler import read_label_file
# from game import Game

# convert1 = Convert(read_label_file('./files/results/result/labels/0_1158.txt'))
# convert2 = Convert(read_label_file('./files/results/result/labels/0_1859.txt'))
# game = Game()
# game.read_position(convert1.go())
# game.board.show()
# game.read_position(convert2.go())
# game.board.show()
