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
        time_stamp = self.time_format(time_stamp)
        if self.start.check(board):
            print(f"GameStart: {str(time_stamp)}")
            if self.game is None:
                self.game = Game(game_start=time_stamp)
            else:
                self.games.append(self.game)
                self.game = Game(game_start=time_stamp)
                self.game.moves = []
                print(len(self.game.moves))
    
        if self.validate.position(board):
            if self.game.add_move(Move(board, time_stamp, self.start.flipped)) == False:
                self.games.append(self.game)
                base_game_moves = self.game.get_moves_for_next_game()
                base_game_start = self.game.game_start
                self.game = Game(moves=base_game_moves, game_start=base_game_start)

    def time_format(self, timestamp):
        return str(timestamp)[2:-4]
            
    def show_games(self):
        for index, game in enumerate(self.games):
            print(f"____________________________Game {str(index)} Start: {str(game.game_start)}___________________________")
            game.show()

    def test_show(self):
        game = self.games[0]
        game.moves[0].show()

        
            