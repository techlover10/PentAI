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

    def play(self, player, r, c):
        self.grid[r][c] = player

    def get_piece(self, r, c):
        if (r > 18 or c > 18 or r < 0 or c < 0):
            return -1
        return self.grid[r][c]
    
    def piece_captured(self, r, c):
        self.grid[r][c] = 0

    def spot_empty(self, r, c):
        return self.get_piece(r, c) == 0

    def get_captures(self, pid):
        return self.captures[pid]
