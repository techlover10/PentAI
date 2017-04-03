#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Superclass defining a game agent, inherited by human
# player and AI player

import game.Agent as Agent

class DumbAgent(Agent.Agent):
    def __init__(self):
        Agent.__init__(self)
        self.xcounter = 0
        self.ycounter = 0
        pass

    def get_move(self):
        self.xcounter+=1
        self.ycounter+=1
        return (self.xcounter, self.ycounter)
