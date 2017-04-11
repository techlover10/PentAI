#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Agent must implement one function, get_move

from logic.Logic import heuristic_count
from copy import copy, deepcopy

class MinimaxAgent:
    def __init__(self):
        self.H_VALS = {
                1: 0,
                2: 1,
                3: 2,
                4: 3,
                5: 4
                }

    def get_move(self, pid, board):
        #print('get_move called')
        move = self.minimax(board, 1, pid)[1]
        print(move)
        return (move[0]+1,move[1]+1)

    def value_state(self, board, pid):
        #print('evaluating state')
        state_val = 0
        for r in range(0, 19):
            for c in range(0,19):
                #print('checking ' + str(r) + ', ' + str(c))
                if not board.spot_empty(r,c):
                    continue
                curr_raw = heuristic_count(board, r, c, pid)
                #if sum(curr_raw.values()) > 0:
                #    print('Row: ' + str(r) + ', Col: ' + str(c))
                #    print(curr_raw)
                for line_count in curr_raw.values():
                    if line_count in self.H_VALS.keys():
                        state_val += self.H_VALS[line_count]
                    else:
                        state_val += line_count
        return (state_val, None)

    def minimax(self, board, bound, player):
        #print('minimaxing')
        other_player = 0
        if (player == 1):
            other_player = 2
        else:
            other_player = 1

        if bound == 0:
            return self.value_state(board, player)

        CURR_MAX = -1
        CURR_POS = (-1,-1)
        for r in range(0, 19):
            for c in range(0, 19):
                #print('checking ' + str(r) + ', ' + str(c))
                if board.spot_empty(r, c):
                    new_board = deepcopy(board)
                    new_board.play(player, r, c)
                    curr_val = self.maximin(new_board, bound - 1, other_player)[0]
                    if curr_val > CURR_MAX:
                        CURR_MAX = curr_val
                        CURR_POS = (r,c)

        return (CURR_MAX, CURR_POS)

    def maximin(self, board, bound, player):
        #print('maximining')
        other_player = 0
        if (player == 1):
            other_player = 2
        else:
            other_player = 1

        if bound == 0:
            return self.value_state(board, player)

        CURR_MIN = -1
        CURR_POS = (-1,-1)
        for r in range(0, 19):
            for c in range(0, 19):
                #print('checking ' + str(r) + ', ' + str(c))
                if board.spot_empty(r, c):
                    new_board = deepcopy(board)
                    new_board.play(player, r, c)
                    curr_val = self.minimax(new_board, bound - 1, other_player)[0] 
                    if curr_val < CURR_MIN:
                        CURR_MIN = curr_val
                        CURR_POS = (r,c)

        return (CURR_MIN, CURR_POS)

