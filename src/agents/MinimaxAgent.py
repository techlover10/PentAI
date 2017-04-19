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
                5: 100,
                'capture': 2
                }

    def get_move(self, pid, board):
        if len(board.empty_adjacent) == 0:
            move = (math.floor(random.random()*18), math.floor(random.random()*18))
            return move
        else:
            moves = {}
            print(board.empty_adjacent)
            for tup in (sorted([(lambda tuple: (tuple, self.value_state(deepcopy(board).play(pid, *tuple), pid)))(tuple) for tuple in board.empty_adjacent], key=(lambda tup: tup[1]), reverse=True)):
                item = tup[0]
                new_board = deepcopy(board)
                new_board.play(pid, *item)
                value = self.alphabeta(new_board, item, pid, 1, -100, 100, True)
                if value not in moves:
                    moves[value] = []
                if item not in moves[value]:
                    moves[value].append(item)
            print(moves)
            return random.choice(moves[max(moves.keys())])

    def value_state(self, board, pid):
        capturesA = board.get_captures(1) # captures of player 1
        capturesB = board.get_captures(2) # captures of player 2
        if (capturesA > 4 or capturesB > 4):
            return 100
        state_val = [0, 0, 0] # players are 1 and 2, 0 index is 0
        for (r,c) in board.occupied:
            curr_pid = board.get_piece(r,c)
            if (check_win(board, r, c, curr_pid)):
                print('win possible at ' + str(r) + ', ' + str(c) + ' with player ' + str(curr_pid))
                if curr_pid == pid:
                    print('curr_player would win')
                    return 100
                else:
                    return -100
            curr_raw = heuristic_count(board, r, c, curr_pid)
            for key in curr_raw.keys():
                count = curr_raw[key]
                if key in self.H_VALS.keys():
                    state_val[curr_pid] += self.H_VALS[key] * count
                else:
                    if count in self.H_VALS.keys():
                        state_val[curr_pid] += self.H_VALS[count]
                    else:
                        state_val[curr_pid] = 100 # not in dict, must be greater than 5
        return state_val[pid] - state_val[2 if pid is 1 else 1]

    def alphabeta(self, board, coord, player, depth, alpha, beta, maximizing_player):
        if depth == 0:
            return self.value_state(board, player)
        # TODO: This technically isn't right, fix it later
        if check_win(board, *coord, player) and maximizing_player:
            return 100*depth
        elif check_win(board, *coord, player):
            return -100*depth
        if maximizing_player:
            v = -(100)
            for tup in (sorted([(lambda tuple: (tuple, self.value_state(deepcopy(board).play(player, *tuple), player)))(tuple) for tuple in board.empty_adjacent], key=(lambda tup: tup[1]), reverse=True)):
                item = tup[0]
                v = max(v, self.alphabeta(deepcopy(board).play(player, *item), item, 2 if player is 1 else 1, depth-1, alpha, beta, False))
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
            return v*depth
        else:
            v = 100
            for tup in (sorted([(lambda tuple: (tuple, self.value_state(deepcopy(board).play(player, *tuple), player)))(tuple) for tuple in board.empty_adjacent], key=(lambda tup: tup[1]), reverse=False)):
                item = tup[0]
                v = min(v, self.alphabeta(deepcopy(board).play(player, *item), item, 2 if player is 1 else 1, depth-1, alpha, beta, True))
                beta = min(beta, v)
                if beta <= alpha:
                    break
            return v*depth
                
