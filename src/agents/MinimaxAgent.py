#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Agent must implement one function, get_move

from logic.Logic import heuristic_count

class MinimaxAgent:
    def __init__(self, pid):
        self.H_VALS = {
                1: 0,
                2: 1,
                3: 2,
                4: 3,
                5: 4
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
                if not board.spot_empty(r,c):
                    continue
                curr_raw = heuristic_count(board, r, c, self.pid)
                if sum(curr_raw.values()) > 0:
                    print('Row: ' + str(r) + ', Col: ' + str(c))
                    print(curr_raw)
                for line_count in curr_raw.values():
                    if line_count in self.H_VALS.keys():
                        state_val += self.H_VALS[line_count]
                    else:
                        state_val += line_count
        return state_val


