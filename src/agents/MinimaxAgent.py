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
                value = self.minimax(new_board, 2, item, pid)
                print("value " + str(value) + "\n")
                print("best value " + str(best_val) + "\n")
                print("position " + str(item) + "\n");
                if (value >= best_val):
                    best_move = item
                    best_val = value
            return best_move

    def value_state(self, board, pid):
        other_pid = 2 if pid is 1 else 1
        """capturesA = board.get_captures(pid)  
        capturesB = board.get_captures(other_pid)
        if (capturesA > 4):
            return 1000
        if (capturesB > 4):
            return -1000
        state_val = [0, 0, 0] # players are 1 and 2, 0 index is 0"""
        for (r,c) in board.empty_adjacent:
            if (check_win(board, r, c, other_pid)):
                #print('win possible at ' + str(r) + ', ' + str(c) + ' with player ' + str(other_pid))
                return -1000
            """if (check_win(board, r, c, pid)):
                print('win possible at ' + str(r) + ', ' + str(c) + ' with player ' + str(pid))
                return 1000
            other_raw = heuristic_count(board, r, c, other_pid)
            curr_raw = heuristic_count(board, r, c, pid)
            for key in curr_raw.keys():
                count = curr_raw[key]
                if key in self.H_VALS.keys():
                    state_val[pid] += self.H_VALS[key] * count
                else:
                    if count in self.H_VALS.keys():
                        state_val[pid] += self.H_VALS[count]
                    else:
                        state_val[pid] = 1000 # not in dict, must be greater than 5
            for key in other_raw.keys():
                count = other_raw[key]
                if key in self.H_VALS.keys():
                    state_val[other_pid] += self.H_VALS[key] * count
                else:
                    if count in self.H_VALS.keys():
                        state_val[other_pid] += self.H_VALS[count]
                    else:
                        state_val[other_pid] = 1000 # not in dict, must be greater than 5"""
        return 0

    def minimax(self, board, bound, coord, player):
        #print('minimaxing\n')
        other_player = 1
        if (player == 1):
            other_player = 1

        if bound == 0:
            return self.value_state(board, player)
        #if check_win(board, *coord, player):
            #return 1000
        #if check_win(board, *coord, other_player):
            #return -1000
        
        CURR_MAX = -100
        for (r,c) in board.empty_adjacent:
            #print('checking ' + str(r) + ', ' + str(c))
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
        #if check_win(board, *coord, player):
            #return 1000
        #if check_win(board, *coord, other_player):
            #return -1000

        CURR_MIN = 100
        for (r,c) in board.empty_adjacent:
            new_board = deepcopy(board)
            new_board.play(other_player, r, c)
            curr_val = self.minimax(new_board, bound - 1, (r, c), player)
            if curr_val < CURR_MIN:
                CURR_MIN = curr_val
        #print("CURRMIN " + str(CURR_MIN) +"\n")
        return CURR_MIN

