#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# A game is an instance of an actual game

import game.Board as Board
import logic.Logic as Logic
import game.DumbAgent

class Game:
    def __init__(self, agent1=None, agent2=None):
        self.board = Board.Board()
        self.session_active = False
        self.current_turn = 1 # start with player 1
        self.agents[0] = None
        self.agents[1] = agent1
        self.agents[2] = agent2

    def start_game(self):
        self.session_active = True
        self.run_game()

    def reset(self):
        self.board = Board.Board()
        self.session_active = False
        self.current_turn = 1

    # Game will run until it is a human's turn
    def run_game(self):
        while self.agents[self.current_turn]:
            play(self.agents[self.current_turn].get_move(self.board))

    def play(self, xcoord, ycoord):
        if xcoord < 1 or xcoord > 19 or ycoord < 1 or ycoord > 19:
            print("Invalid position specified!")
            print("Player " + str(self.current_turn) + "'s turn!")
            return

        xcoord -= 1 # adjust for 0 index
        ycoord -= 1 # adjust for 0 index

        if not self.board.spot_empty(xcoord, ycoord):
            print ("Position is occupied!")
            print("Player " + str(self.current_turn) + "'s turn!")
            return

        self.board.play(self.current_turn, xcoord, ycoord)

        if Logic.check_win(self.board, xcoord, ycoord, self.current_turn):
            print("Player " + str(self.current_turn) + ' wins!')
            print("Game ended.")
            self.reset()
            return

        self.current_turn = 2 if self.current_turn is 1 else 1
        print("Player " + str(self.current_turn) + "'s turn!")


