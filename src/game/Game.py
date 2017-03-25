#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# A game is an instance of an actual game

import game.Board as Board
import logic.Logic as Logic

class Game:
    def __init__(self):
        self.board = Board.Board()
        self.session_active = False
        self.current_turn = 1 # start with player 1

    def start_game(self):
        self.session_active = True

    def reset(self):
        self.board = Board.Board()
        self.session_active = False
        self.current_turn = 1

    def play(self, r, c):
        if r < 1 or r > 19 or c < 1 or c > 19:
            print("Invalid position specified!")
            print("Player " + str(self.current_turn) + "'s turn!")
            return

        r -= 1 # adjust for 0 index
        c -= 1 # adjust for 0 index

        if not self.board.spot_empty(r, c):
            print ("Position is occupied!")
            print("Player " + str(self.current_turn) + "'s turn!")
            return

        self.board.play(self.current_turn, r, c)

        if Logic.check_win(self.board, r, c, self.current_turn):
            print("Player " + str(self.current_turn) + ' wins!')
            print("Game ended.")
            self.reset()
            return

        self.current_turn = 2 if self.current_turn is 1 else 1
        print("Player " + str(self.current_turn) + "'s turn!")


