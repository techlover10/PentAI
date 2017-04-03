#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Agent must implement one function, get_move


class DumbAgent:
    def __init__(self):
        self.xcounter = 0
        self.ycounter = 0
        pass

    def get_move(self, pid, board):
        self.xcounter+=1
        self.ycounter+=1
        return (self.xcounter, self.ycounter)
