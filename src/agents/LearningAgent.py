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
                0: 0,
                1: 0,
                2: 5,
                3: 20,
                4: 50,
                5: 1000,
                'capture': 10
                }
        self.load_heuristic_vals()

    def get_move(self, pid, board):

        if self.prev_state:
            self.update_heuristic_vals(board, pid)

        if len(board.empty_adjacent) == 0:
            move = (math.floor(random.random()*18), math.floor(random.random()*18))
        else:
            move = self.pentemax(board, 2)[0]

        self.prev_state = deepcopy(board).play(pid, *move)

        return move

    def heuristic_value_state(self, board, pid):
        other_pid = 2 if pid is 1 else 1
        state_val = {}
        for (r,c) in board.occupied:
            curr_raw = heuristic_count(board, r, c, pid)
            for key in curr_raw.keys():
                count = curr_raw[key]
                #print((r,c))
                #print(curr_raw)
                if key in self.H_VALS.keys():
                    if count in state_val:
                        state_val[count] += self.H_VALS[key]
                    else:
                        state_val[count] = self.H_VALS[key]
                else:
                    if count in self.H_VALS.keys():
                        if count in state_val:
                            state_val[count] += self.H_VALS[count]
                        else:
                            state_val[count] = self.H_VALS[count]
                    else:
                        if count in state_val:
                            state_val[count] += 1000 # not in dict, must be greater than 5
                        else:
                            state_val[count] = 1000
        return state_val 

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

    def update_heuristic_vals(self, board, pid):
        curr_state = deepcopy(board)
        prev_state = deepcopy(self.prev_state)

        other_pid = 2 if pid is 1 else 1
        curr_val = self.value_state(curr_state, other_pid)
        prev_val = self.value_state(prev_state, pid)

        if curr_val > prev_val:
            counts = self.heuristic_value_state(curr_state, other_pid)
        elif prev_val > curr_val:
            counts = self.heuristic_value_state(prev_state, pid)

        # find out which feature led that move to be picked
        max_val = 0
        max_key = None
        for k, v in counts.items():
            if v >= max_val:
                max_val = v
                max_key = k

        # update max key with alpha
        acc = 0
        for k in self.H_VALS.keys():
            if self.H_VALS[k] - self.ALPHA_VAL > 0:
                self.H_VALS[k] -= self.ALPHA_VAL
                acc += self.ALPHA_VAL

        self.H_VALS[max_key] += acc
        self.write_heuristic_vals()


    def load_heuristic_vals(self):
        if os.path.isfile('heuristic.json'):
            self.H_VALS = json.loads(open('agents/heuristic.json').read())

    def write_heuristic_vals(self):
        open('agents/heuristic.json', 'w').write(json.dumps(self.H_VALS))

