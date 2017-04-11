#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# A game is an instance of an actual game

import game.Board as Board
import logic.Logic as Logic
import agents.MinimaxAgent as MinimaxAgent

class Game:
    def __init__(self, agent1=None, agent2=None):
        self.board = Board.Board()
        self.session_active = False
        self.current_turn = 1 # start with player 1
        self.agents = [None, agent1, agent2]

    def start_game(self):
        self.session_active = True
        self.run_game()

    def reset(self):
        self.board = Board.Board()
        self.session_active = False
        self.current_turn = 1

    # Game will run until it is a human's turn
    def run_game(self):
        is_run = False
        while self.agents[self.current_turn] and self.session_active:
            is_run = True
            print("agent " + str(self.current_turn) + " is playing")
            self.play(*self.agents[self.current_turn].get_move(self.current_turn, self.board))
        return is_run

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
        if not self.run_game():
            print("Player " + str(self.current_turn) + "'s turn!")


