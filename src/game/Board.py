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
        self.occupied = []
    def play(self, player, xcoord, ycoord):
        self.grid[xcoord][ycoord] = player
        self.occupied.append((xcoord + 1, ycoord + 1))

    def get_piece(self, xcoord, ycoord):
        return self.grid[xcoord][ycoord]

    def spot_empty(self, xcoord, ycoord):
        return self.get_piece(xcoord, ycoord) == 0

    def get_captures(self, pid):
        return self.captures[pid]
