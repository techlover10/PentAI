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
            print('get move called')
            a = self.pentemax(board)
            print('returning ' + str(a))
            return self.pentemax(board)

    def value_state(self, board, pid):
        other_pid = 2 if pid is 1 else 1
        state_val = 0
        for (r,c) in board.occupied:
            curr_raw = heuristic_count(board, r, c, pid)
            for key in curr_raw.keys():
                count = curr_raw[key]
                #print((r,c))
                #print(curr_raw)
                if key in self.H_VALS.keys():
                    state_val += self.H_VALS[key]
                else:
                    if count in self.H_VALS.keys():
                        state_val += self.H_VALS[count]
                    else:
                        state_val += 1000 # not in dict, must be greater than 5
        return state_val 

    def pentemax(self, board):
            val1 = self.value_state(board, 1)
            val2 = self.value_state(board, 2)
            return self.max_move(board, 1 if val1 > val2 else 2)

    def max_move(self, board, pid):
        max_val = -1
        max_move = (math.floor(random.random()*18), math.floor(random.random()*18))
        for (r, c) in board.empty_adjacent:
            new_val = self.value_state(deepcopy(board.play(pid, r, c)), pid)
            if new_val > max_val:
                max_val = new_val
                max_move = (r, c)
        return max_move


    def minimax(self, board, bound, coord, player):
        #print('minimaxing\n')
        other_player = 1
        if (player == 1):
            other_player = 2

        if bound == 0:
            return self.value_state(board, player, bound)

        if check_win(board, *coord, other_player):
            return -1000
        if check_win(board, *coord, player):
            return -1000

        CURR_MAX = 0

        for (r,c) in board.empty_adjacent:
            new_board = deepcopy(board)
            new_board.play(player, r, c)
            curr_val = self.maximin(new_board, bound - 1, (r, c), player)
            if curr_val > CURR_MAX:
                CURR_MAX = curr_val
        #print("CURRMAX " + str(CURR_MAX) +"\n")
        return CURR_MAX

    def maximin(self, board, bound, coord, player):
        #print('maximining\n')
        other_player = 1
        if (player == 1):
            other_player = 2

        if bound == 0:
            return self.value_state(board, player)

        if check_win(board, *coord, other_player):
            return 1000
        if check_win(board, *coord, player):
            return 1000

        CURR_MIN = float('inf')
        for (r,c) in board.empty_adjacent:
            new_board = deepcopy(board)
            new_board.play(other_player, r, c)
            curr_val = self.minimax(new_board, bound - 1, (r, c), player)
            if curr_val < CURR_MIN:
                CURR_MIN = curr_val
        #print("CURRMIN " + str(CURR_MIN) +"\n")
        return CURR_MIN

