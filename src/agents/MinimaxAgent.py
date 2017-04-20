#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Agent must implement one function, get_move

from logic.Logic import heuristic_count, check_win
from copy import copy, deepcopy
import random, math

class MinimaxAgent:
    def __init__(self):
        self.H_VALS = {
                1: 0,
                2: 1,
                3: 2,
                4: 3,
                5: 1000,
                'capture': 2
                }

    def get_move(self, pid, board):
        if len(board.empty_adjacent) == 0:
            move = (math.floor(random.random()*18), math.floor(random.random()*18))
            return move
        else:
            best_move = (-1, -1)
            best_val = -1000
            for item in board.empty_adjacent:
                new_board = deepcopy(board)
                new_board.play(pid, *item)
                value = self.maximin(new_board, 2, item, pid)
                if (value >= best_val):
                    best_move = item
                    best_val = value
            return best_move

    def value_state(self, board, pid):
        other_pid = 2 if pid is 1 else 1
        for (r,c) in board.empty_adjacent:
            if (check_win(board, r, c, other_pid)):
                return -1000
        return 0

    def minimax(self, board, bound, coord, player):
        other_player = 1 if player is 2 else 2

        if bound == 0:
            return self.value_state(board, player)
        
        CURR_MAX = -100
        for (r,c) in board.empty_adjacent:
            new_board = deepcopy(board)
            new_board.play(player, r, c)
            curr_val = self.maximin(new_board, bound - 1, (r, c), player)
            if curr_val > CURR_MAX:
                CURR_MAX = curr_val
        return CURR_MAX

    def maximin(self, board, bound, coord, player):
        other_player = 1 if player is 2 else 2

        if bound == 0:
            return self.value_state(board, player)

        CURR_MIN = 100
        for (r,c) in board.empty_adjacent:
            new_board = deepcopy(board)
            new_board.play(other_player, r, c)
            curr_val = self.minimax(new_board, bound - 1, (r, c), player)
            if curr_val < CURR_MIN:
                CURR_MIN = curr_val
        return CURR_MIN

