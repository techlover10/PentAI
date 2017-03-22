#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Represents the game board.  Maintains game state.

from copy import copy, deepcopy

class Board:
    def __init__(self):

        # initialize the start grid
        start_row = []
        for i in range (19):
            start_row.append(0)

        self.grid = []
        for i in range (19):
            self.grid.append(deepcopy(start_row))

        self.captures = {
                1: 0,
                2: 0
                }

    def play(self, pID, xcoord, ycoord):
        self.grid[xcoord][ycoord] = pid
        self.check_capture()

    def check_capture(self):
        # TODO: Implement this
        pass

