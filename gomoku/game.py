# -*- coding: utf-8 -*-

""" the gomoku game """

class Game():
    NO_WINNER = 0
    PLAYER_1  = 1
    PLAYER_2  = 2

    def __init___(self, player_black=None, player_white=None, game_board=None):
        self.player_black = player_black
        self.player_white = player_white
        self.game_board = game_board
        self.__is_over = False
        self.__winner = self.NO_WINNER

    def move(self, move_action=None):
        self.game_board.move(move_action)
        if self.__get_winner() == self.NO_WINNER:
            self.winner = self.__get_winner()
            self.__end_game()

    def __get_winner(self):
        return self.game_board.winner

    def __end_game(self):
        self.__is_over = True