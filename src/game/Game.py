#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# A game is an instance of an actual game

import game.Board as Board

class Game:
    def __init__(self):
        self.board = Board.Board()
        self.session_active = False
        self.current_turn = 1 # start with player 1

    def start_game(self):
        self.session_active = True

    def play(self, xcoord, ycoord):
        if xcoord < 0 or xcoord > 19 or ycoord < 0 or ycoord > 19:
            print("Invalid position specified!")
            print("Player " + str(self.current_turn) + "'s turn!")
            return

        if not self.board.spot_empty(xcoord, ycoord):
            print ("Position is occupied!")
            print("Player " + str(self.current_turn) + "'s turn!")
            return

        self.board.play(self.current_turn, xcoord, ycoord)
        self.current_turn = 2 if self.current_turn is 1 else 1
        print("Player " + str(self.current_turn) + "'s turn!")


