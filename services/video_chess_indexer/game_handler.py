from game import Game
from game_start import GameStart
from validate import Validate
from move import Move
from board import Board

class GameHandler:
    def __init__(self):
        self.start = GameStart()
        self.validate = Validate()
        self.game = None
        self.games = []

    def read_board(self, board, time_stamp): 
        if self.start.check(board):
            print(f"GameStart: {str(time_stamp)}")
            if self.game is None:
                self.game = Game()
            else:
                self.games.append(self.game)
                self.game = Game()
    
        if self.validate.position(board):
            if self.game.add_move(Move(board, time_stamp, self.start.flipped)) == False:
                """
                SOMETHING LOGIGS
                """
                return False
                

            
       

        
            