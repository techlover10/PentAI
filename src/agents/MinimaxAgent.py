#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Agent must implement one function, get_move

from logic.Logic import heuristic_count, check_win
from copy import copy, deepcopy
import random, math

class Agent:
    def __init__(self):
        self.is_learning = False
        self.H_VALS = {
                1: 0,
                2: 5,
                3: 20,
                4: 50,
                5: 1000,
                'capture': 10
                }

    def get_move(self, pid, board):
        if len(board.empty_adjacent) == 0:
            move = (math.floor(random.random()*18), math.floor(random.random()*18))
            return move
        else:
            #a= (math.floor(random.random()*18), math.floor(random.random()*18))
            a = self.pentemax(board, 2)[0]
            #print('returning ' + str(a))
            return a

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

    def pentemax(self, board, recursion):
        val1 = self.value_state(deepcopy(board), 1)
        val2 = self.value_state(deepcopy(board), 2)
        pid = 1 if val1 > val2 else 2
        max_val = -1
        best_move = (-1, -1)
        if recursion == 0:
            for (r, c) in board.empty_adjacent:
                new_val = self.value_state(deepcopy(board).play(pid, r, c), pid)
                if new_val > max_val:
                    max_val = new_val
                    best_move = (r, c)
                return (best_move, max_val)
        else:
            for (r, c) in board.empty_adjacent:
                new_val = self.value_state(deepcopy(board).play(pid, r, c), pid)
                pentemax_max_val = -1
                if new_val > max_val:
                    pentemax_max_val_curr = self.pentemax(deepcopy(board).play(pid, r, c), recursion-1)[1] * recursion
                    if pentemax_max_val_curr > pentemax_max_val:
                        max_val = new_val
                        best_move = (r, c)
            return (best_move, max_val)



    #def minimax(self, board, bound, coord, player):
    #    #print('minimaxing\n')
    #    other_player = 1
    #    if (player == 1):
    #        other_player = 2

    #    if bound == 0:
    #        return self.value_state(board, player, bound)

    #    if check_win(board, *coord, other_player):
    #        return -1000
    #    if check_win(board, *coord, player):
    #        return -1000

    #    CURR_MAX = 0

    #    for (r,c) in board.empty_adjacent:
    #        new_board = deepcopy(board)
    #        new_board.play(player, r, c)
    #        curr_val = self.maximin(new_board, bound - 1, (r, c), player)
    #        if curr_val > CURR_MAX:
    #            CURR_MAX = curr_val
    #    #print("CURRMAX " + str(CURR_MAX) +"\n")
    #    return CURR_MAX

    #def maximin(self, board, bound, coord, player):
    #    #print('maximining\n')
    #    other_player = 1
    #    if (player == 1):
    #        other_player = 2

    #    if bound == 0:
    #        return self.value_state(board, player)

    #    if check_win(board, *coord, other_player):
    #        return 1000
    #    if check_win(board, *coord, player):
    #        return 1000

    #    CURR_MIN = float('inf')
    #    for (r,c) in board.empty_adjacent:
    #        new_board = deepcopy(board)
    #        new_board.play(other_player, r, c)
    #        curr_val = self.minimax(new_board, bound - 1, (r, c), player)
    #        if curr_val < CURR_MIN:
    #            CURR_MIN = curr_val
    #    #print("CURRMIN " + str(CURR_MIN) +"\n")
    #    return CURR_MIN

