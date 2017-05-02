#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Agent must implement one function, get_move

from logic.Logic import heuristic_count, check_win
from copy import copy, deepcopy
import random, math, json, os

class Agent:
    def __init__(self):
        self.ALPHA_VAL = 1
        self.prev_state = None
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
        else:
            move = self.pentemax(board, 2)[0]

        if self.prev_state:
            self.update_heuristic_vals(board)
        self.prev_state = deepcopy(board)


        return move

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

    def update_heuristic_vals(self, board):
        curr_state = deepcopy(board)
        prev_state = deepcopy(self.prev_state)

        curr_val = self.value_state(curr_state)
        prev_val = self.value_state(prev_state)

        if curr_val > prev_val:
            counts = heuristic_count(curr_state)
        elif prev_val > curr_val:
            counts = heuristic_count(prev_state)

        # find out which feature led that move to be picked
        max_val = 0
        max_key = None
        for k, v in counts.items():
            curr_count = 0
            if k in self.H_VALS:
                curr_count = v * self.H_VALS[k]
            else:
                curr_count = v * self.H_VALS[v]
            if curr_count > max_val:
                max_val = curr_count
                max_key = k

        # update max key with alpha
        for k in self.H_VALS.keys():
            self.H_VALS[k] -= self.ALPHA_VAL

        self.H_VALS[max_key] += self.ALPHA_VAL * (len(self.H_VALS.keys()) + 1)


    def load_heuristic_vals(self):
        if os.path.isfile('heuristic.json'):
            self.H_VALS = json.load(open('heuristic.json').read())

    def write_heuristic_vals(self):
        open('heuristic.json', 'w').write(json.dump(self.H_VALS))

