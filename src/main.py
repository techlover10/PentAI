#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Main file for PentAI - launches the REPL to run
# whatever command is desired.

import game

terminal_in = 'PentAI> '

# list of all commands for operating at the toplevel
possible_cmds = {
        'exit': 'Exits the program.',
        'help': 'Displays this screen.'
        }

print('--- Welcome to PentAI ---')
cmd = input(terminal_in)

# REPL loop
while cmd != 'exit':
    if cmd == 'help':
        print('----- PentAI: Help Manual -----')
        for i in possible_cmds:
            print(' ' + i + ': ' + possible_cmds[i])
    else:
        print("Unrecognized command.  Type 'help' for a list of commands.")
    cmd = input(terminal_in)


