from board import Board
    
class Convert:
    def __init__(self, labels):
        self.labels = labels
        self.get_board()
        self.set_square_w_h()
        self.set_top_square_corner_x_y()
        self.board = Board()

    def set_top_square_corner_x_y(self):
        self.top_corner_square_x_center = (self.board_x_center - (self.board_w / 2)) + self.square_w / 2
        self.top_corner_square_y_center = (self.board_y_center - (self.board_h / 2)) + self.square_h / 2

    def set_square_w_h(self):
        self.square_w = self.board_w/8
        self.square_h = self.board_h/8

    def convert_darknet_to_chess_pos(self, x_center, y_center):
        x_pos = round((x_center - self.top_corner_square_x_center) / self.square_w)
        y_pos = round((y_center - self.top_corner_square_y_center) / self.square_h)
        return x_pos, y_pos

    def get_board(self):
        for index, label in enumerate(self.labels):
            if label[0] == '13':
                self.board_x_center = float(label[1])
                self.board_y_center = float(label[2])
                self.board_w = float(label[3])
                self.board_h = float(label[4])
                del self.labels[index]
                
    def go(self):
        for label in self.labels:
            x_pos, y_pos = self.convert_darknet_to_chess_pos(float(label[1]), float(label[2]))
            self.board.squares[y_pos][x_pos].set(label[0])