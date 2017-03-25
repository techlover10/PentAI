#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Helper functions for printing nicely

import os, math

class Printer:
    def __init__(self):
        x = os.popen('stty size', 'r').read().split()
        if (len(x) > 0):
            self.print_enabled = True 
            self.rows = x[0]
            self.columns = x[1]
        else:
            self.print_enabled = False 
            self.rows = 1
            self.columns = 50
        self.columns = min([int(self.columns), 50])

    def printable_title(self, text):
        text = ' ' + text.strip(' ') + ' '
        border_float = (self.columns - len(text))/2
        left_border = int(math.ceil(border_float))
        right_border = int(math.floor(border_float))
        return (('-'*left_border) + text + ('-'* right_border))

    def printable_option(self, text):
        return (' '*5 + text)

    def print_heading(self, text):
        if not self.print_enabled:
            return
        print() # print an empty line before all prints
        print_text = self.printable_title(text)
        print(print_text)

    def print_sep(self):
        if not self.print_enabled:
            return
        print('-' * self.columns)
        print()

    def print_option(self, text):
        if not self.print_enabled:
            return
        print_text = self.printable_option(text)
        print(print_text)

    def board_printer(self, game_board):
        self.print_heading('Game Board')
        self.print_sep()
        print(' ____'*19)
        topstr = ('|    '*19) + '|'
        botstr = ('|____'*19) + '|'
        for row in game_board.grid:
            curr_str = '|'
            for column in row:
                curr_str += ' '
                curr_str = curr_str + ('  ' if column is 0 else 'P' + str(column)) + ' |'
            print(topstr)
            print(curr_str)
            print(botstr)

    def print_captures(self, game_board, player=None):
        if player:
            print('Player ' + str(player) + ' has ' + str(game_board.captures[player]) + '.')
        else:
            for i in game_board.captures:
                print('Player ' + str(i) + ' has ' + str(game_board.captures[i]) + '.')

    def print_occupied(self, game_board):
        print("Currently occupied positions")
        for i in game_board.occupied:
            print(str(i))


