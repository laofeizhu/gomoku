""" game board """
from gomoku.move_action import MoveAction
from gomoku.point import Point
class GameBoard():
    DIRS = [[0,1],[1,1],]
    def __init__(self, size=19):
        self.size = size
        self.grid = [[0 for x in range(size)] for y in range(size)]
        self.last_move = MoveAction(0, Point(0,0))
        self.current_player = 1
        self.winner = 0

    def move(self, move_action):
        move_player = move_action.player
        move_point = move_action.point

        # if the move is from the wrong player, raise error
        if move_player!=self.current_player:
            raise ValueError('not player_%d\'s turn to play' % move_player)
        
        # if the target point is already occupied, raise error
        if self.grid[move_point.x][move_player.y]!=0:
            raise ValueError('grid %s already has a stone' % move_point)
        
        self.last_move = move_action
        self.grid[move_point.x][move_player.y] = move_player
        self.current_player = 3 - self.current_player

        self.__update_winner()

    def __update_winner(self):
        return 0

