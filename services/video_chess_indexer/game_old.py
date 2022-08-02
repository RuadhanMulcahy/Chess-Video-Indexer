class Game:
    def __init__(self, game_start=None):
        self.moves = []
        self.moves_ahead = []
        self.game_start = game_start
        self.on_game_start = False

    def add_move(self, move):
        if self.reverse_move_check(move):
            # print("Reverse Move")
            # print('__________________')
            # move.show()
            # self.moves.pop()
            self.moves_ahead.append(self.moves[-1])
            self.moves.pop()
            self.moves.append(move)
        elif self.reverse_move_check(move) == False and self.catch_up_check(move) == False and len(self.moves_ahead) >= 1:
            # print("New Game Branch")
            # print('__________________')
            # move.show()
            # test_game = self.get_game()
            # for i in test_game:
            #     i.show()

            self.moves = []
            self.moves_ahead = []
        elif self.catch_up_check(move):
            # print("Catch Up Move")
            # print('__________________')
            # move.show()
            # print("catch")
            # print('_______________')
            # self.moves_ahead[-1].show()
            # move.show()
            # print("______________")
            self.moves.append(move)
            self.moves_ahead.pop()
        else:
            # print("Normal Move")
            # print('__________________')
            # move.show()
            if len(self.moves) >= 1:
                # move.taken_piece = 'test'
                move.taken_piece = self.moves[-1].board.squares[move.new_square.y][move.new_square.x].piece_short
            self.moves.append(move)
        # move.show()
        
    def get_game(self):
        return self.moves[:-1] + self.moves_ahead

    def catch_up_check(self, move):
        if len(self.moves_ahead) == 0:
            return False
        if self.moves_ahead[-1].compare(move):
            return True
        return False

    def reverse_move_check(self, move):
        if len(self.moves) == 0:
            return False
        
        prev_move = self.moves[-1]
        curr_move = move
        if curr_move.board.squares[prev_move.prev_square.y][prev_move.prev_square.x].piece_short == prev_move.new_square.piece_short:
            return True
        return False
    # def reverse_move_check(self):
    #     if len(self.moves) < 2:
    #         return False
    #     prev_move = self.moves[-2]
    #     curr_move = self.moves[-1]
    #     if curr_move.board.squares[prev_move.prev_square.y][prev_move.prev_square.x].piece_short == prev_move.new_square.piece_short:
    #         return True
    #     return False
































    # def add_move(self, move):
    #     catch_up_check = False
    #     reverse_check = False
    #     self.moves.append(move)
    #     # move.show()
    #     if self.reverse_move_check():
    #         # print("reverse move")
    #         self.moves.pop(-2)
    #         self.moves_ahead.appedef catch_up_check(self):
    #     if len(self.moves) < 2 or len(self.moves_ahead) < 2:
    #         return False
    #     if self.moves[-1].compare(self.moves_ahead[-1]):
    #         return True

    # def reverse_move_check(self):
    #     if len(self.moves) < 2:
    #         return False
    #     prev_move = self.moves[-2]
    #     curr_move = self.moves[-1]
    #     if curr_move.board.squares[prev_move.prev_square.y][prev_move.prev_square.x].piece_short == prev_move.new_square.piece_short:
    #         return True
    #     return Falsend(move)       
    #         self.reverse_move_count += 1     
    #         reverse_check = True
    #         # move.show()
    #     elif self.catch_up_check():
    #         # print("________________________")
    #         # print("catch up")
    #         # self.moves_ahead[-1].show()
    #         # self.moves[-1].show()
    #         # print("______________")
    #         self.moves_ahead.pop()     
    #         catch_up_check = True 

    #     if catch_up_check == False and reverse_check == False and len(self.moves_ahead) >= 1:
    #         # print(f"{str(catch_up_check)} {str(reverse_check)} {str(len(self.moves_ahead))}")
    #         # # self.moves.append(self.moves_ahead)
    #         # # self.moves_ahead = []
    #         print("__________________________")
    #         for move in self.moves:
    #             move.show()
    #         for move in self.moves_ahead:
    #             move.show()
    #         print("__________________________")
    #         self.moves_ahead = []

    def show_game(self):
        print("Moves")
        for move in self.moves:
            move.show()

        print("Moves ahead")
        for move in self.moves_ahead:
            move.show()

    # def catch_up_check(self):
    #     if len(self.moves) < 2 or len(self.moves_ahead) < 2:
    #         return False
    #     if self.moves[-1].compare(self.moves_ahead[-1]):
    #         return True

    # def reverse_move_check(self):
    #     if len(self.moves) < 2:
    #         return False
    #     prev_move = self.moves[-2]
    #     curr_move = self.moves[-1]
    #     if curr_move.board.squares[prev_move.prev_square.y][prev_move.prev_square.x].piece_short == prev_move.new_square.piece_short:
    #         return True
    #     return False