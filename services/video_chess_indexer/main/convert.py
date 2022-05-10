from board import Board
    
class Convert:
    def __init__(self, labels):
        self.labels = labels
        self.get_board()
        self.set_board_boundaries()
        self.set_square_w_h()
        self.set_top_square_corner_x_y()
        self.board = Board()

    def set_top_square_corner_x_y(self):
        """
        Sets the top left center square co ordinates
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
        Chcks if label is within the board boundaries
        """
        if x_center < self.board_left or x_center > self.board_right:
            return False
        elif y_center < self.board_top or y_center > self.board_bottom:
            return False
        else:
            return True

    def convert_darknet_to_chess_pos(self, x_center, y_center):
        """
        Converts darknet x y coordinates to chess position
        """
        x_pos = round((x_center - self.top_corner_square_x_center) / self.square_w)
        y_pos = round((y_center - self.top_corner_square_y_center) / self.square_h)
        return x_pos, y_pos

    def get_board(self):
        """
        Gets the board label in the labels list and removes it from the labels list
        """
        for index, label in enumerate(self.labels):
            if label[0] == '13':
                self.board_x_center = float(label[1])
                self.board_y_center = float(label[2])
                self.board_w = float(label[3])
                self.board_h = float(label[4])
                del self.labels[index]
                
    def go(self):
        """
        Loops through each element in the labels file 
        """
        for label in self.labels:
            if self.is_label_within_board(float(label[1]), float(label[2])):
                x_pos, y_pos = self.convert_darknet_to_chess_pos(float(label[1]), float(label[2]))
                self.board.squares[y_pos][x_pos].set(label[0])

    def temp_debug(self):
        """
        For debugging purposes (Will be deleted)
        """
        print(f"board_top - {self.board_top}")
        print(f"board_bottom - {self.board_bottom}")
        print(f"board_left - {self.board_left}")
        print(f"baord_right - {self.board_right}")