""" move of the gomoku game """

class MoveAction():

    def __init__(self, player=1, point=None):
        self.point = point
        self.player = player
