#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Main file for PentAI - launches the REPL to run
# whatever command is desired.

import os
import game

rows, columns = os.popen('stty size', 'r').read().split()
columns = min([int(columns), 50])

terminal_in = 'PentAI> '
welcome = ' Welcome to PentAI '
help = ' PentAI: Help Manual '

# list of all commands for operating at the toplevel
possible_cmds = {
        'exit': 'Exits the program.',
        'help': 'Displays this screen.'
        }

print()
print()
print(('-'*int(((columns)-len(welcome))/2) + welcome + '-'*int(((columns)-len(welcome))/2)))
cmd = input(terminal_in)

# REPL loop
while cmd != 'exit':
    if cmd == 'help':
        print()
        print('-'*int(((columns)-len(help))/2) + help + '-'*int(((columns)-len(help))/2))
        for i in possible_cmds:
            cmd = ' ' + i + ': ' + possible_cmds[i] + ' '
            print(' '*5 + cmd)
        print('-'*columns)
        print()
    else:
        print("Unrecognized command.  Type 'help' for a list of commands.")
    cmd = input(terminal_in)


