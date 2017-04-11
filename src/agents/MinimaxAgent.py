#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Agent must implement one function, get_move

from logic.Logic import heuristic_count

class MinimaxAgent:
    def __init__(self, pid):
        self.H_VALS = {
                1: 1,
                2: 2,
                3: 3,
                4: 4,
                5: 5
                }
        self.xcounter = 0
        self.ycounter = 0
        self.pid = pid
        pass

    def get_move(self, board):
        self.xcounter+=1
        self.ycounter+=1
        return (self.xcounter, self.ycounter)

    def value_state(self, board):
        state_val = 0
        for r in range(0, 19):
            for c in range(0,19):
                curr_raw = heuristic_count(board, r, c, self.pid)
                for line_count in curr_raw.values():
                    if line_count in self.H_VALS.keys():
                        state_val += self.H_VALS[line_count]
                    else:
                        state_val += line_count
        return state_val


