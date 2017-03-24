#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Main file for PentAI - launches the REPL to run
# whatever command is desired.

from terminal import Printer
import game

session = Printer.Printer()

terminal_in = 'PentAI> '
welcome = 'Welcome to PentAI'
help = 'PentAI: Help Manual'

# list of all commands for operating at the toplevel
possible_cmds = {
        'exit': 'Exits the program.',
        'help': 'Displays this screen.'
        }

session.print_heading(welcome)
cmd = input(terminal_in)

# REPL loop
while cmd != 'exit':
    if cmd == 'help':
        session.print_heading(help)
        for i in possible_cmds:
            cmd = ' ' + i + ': ' + possible_cmds[i] + ' '
            session.print_option(cmd)
        session.print_sep()
    else:
        print("Unrecognized command.  Type 'help' for a list of commands.")
    cmd = input(terminal_in)


