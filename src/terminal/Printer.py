#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Helper functions for printing nicely

import os, math

class Printer:
    def __init__(self):
        self.rows, self.columns = os.popen('stty size', 'r').read().split()
        self.columns = min([int(self.columns), 50])

    def printable_title(self, text):
        border_float = (self.columns - len(text))/2
        left_border = int(math.ceil(border_float))
        right_border = int(math.floor(border_float))
        return (('-'*left_border) + text + ('-'* right_border))

    def printable_option(self, text):
        return (' '*5 + text)

    def print_heading(self, text):
        print() # print an empty line before all prints
        print_text = self.printable_title(text)
        print(print_text)

    def print_sep(self):
        print('-' * self.columns)
        print()

    def print_option(self, text):
        print_text = self.printable_option(text)
        print(print_text)
