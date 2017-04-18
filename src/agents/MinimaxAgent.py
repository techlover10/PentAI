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
                5: float('inf'),
                'capture': 2
                }

    def get_move(self, pid, board):
        #print('get_move called')
        #move = self.minimax(board, 2, pid)[1]
        if len(board.empty_adjacent) == 0:
            move = (math.floor(random.random()*18), math.floor(random.random()*18))
            return move
        else:
            moves = {}
            for tup in (sorted([(lambda tuple: (tuple, self.value_state(deepcopy(board).play(pid, *tuple), pid)))(tuple) for tuple in board.empty_adjacent], key=(lambda tup: tup[1]), reverse=True))[0:4]:
            #for item in board.empty_adjacent:
                item = tup[0]
                new_board = deepcopy(board)
                new_board.play(pid, *item)
                value = self.alphabeta(new_board, item, pid, 2, -1, float('inf'), True)
                moves[value] = item
            return moves[max(moves.keys())]
        #print(move)

    def value_state(self, board, pid):
        #print('evaluating state')
        if (board.get_captures(pid) > 4):
            return float('inf')
        state_val = 0
        for (r,c) in board.empty_adjacent:
            #print('checking ' + str(r) + ', ' + str(c))
            curr_raw = heuristic_count(board, r, c, pid)
            #if sum(curr_raw.values()) > 0:
            #    print('Row: ' + str(r) + ', Col: ' + str(c))
            #    print(curr_raw)
            for key in curr_raw.keys():
                count = curr_raw[key]
                if key in self.H_VALS.keys():
                    state_val += self.H_VALS[key] * count
                else:
                    if count in self.H_VALS.keys():
                        state_val += self.H_VALS[count]
                    else:
                        state_val = float('inf') # not in dict, must be greater than 5
        #print('state value for player ' + str(pid) + ': ' + str(state_val))
        #return (state_val, None)
        return state_val

    def alphabeta(self, board, coord, player, depth, alpha, beta, maximizing_player):
        if depth == 0:
            return self.value_state(board, player)
        if check_win(board, *coord, player):
            if maximizing_player:
                return float('inf')
            else:
                return -(float('inf'))
        if maximizing_player:
            v = -1
            for tup in (sorted([(lambda tuple: (tuple, self.value_state(deepcopy(board).play(player, *tuple), player)))(tuple) for tuple in board.empty_adjacent], key=(lambda tup: tup[1]), reverse=True))[0:4]:
                item = tup[0]
            #for item in board.empty_adjacent:
                v = max(v, self.alphabeta(deepcopy(board).play(player, *item), item, player, depth-1, alpha, beta, False))
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
            return v
        else:
            v = float('inf')
            #for item in board.empty_adjacent:
            for tup in (sorted([(lambda tuple: (tuple, self.value_state(deepcopy(board).play(player, *tuple), player)))(tuple) for tuple in board.empty_adjacent], key=(lambda tup: tup[1]), reverse=True))[0:4]:
                item = tup[0]
                v = min(v, self.alphabeta(deepcopy(board).play(player, *item), item, player, depth-1, alpha, beta, True))
                beta = min(beta, v)
                if beta <= alpha:
                    break
            return v
                

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
        for (r,c) in board.empty_adjacent:
            #print('checking ' + str(r) + ', ' + str(c))
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

        CURR_MIN = float('inf')
        CURR_POS = (-1,-1)
        for (r,c) in board.empty_adjacent:
            #print('checking ' + str(r) + ', ' + str(c))
            new_board = deepcopy(board)
            new_board.play(player, r, c)
            curr_val = self.minimax(new_board, bound - 1, other_player)[0] 
            if curr_val < CURR_MIN:
                CURR_MIN = curr_val
                CURR_POS = (r,c)

        return (CURR_MIN, CURR_POS)

