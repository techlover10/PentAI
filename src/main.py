#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Main file for PentAI - launches the REPL to run
# whatever command is desired.

from terminal import Printer
import game.Game as game

session = Printer.Printer()

terminal_in = 'PentAI> '
welcome = 'Welcome to PentAI'
help = 'PentAI: Help Manual'

current_game = game.Game()

# list of all commands for operating at the toplevel
possible_cmds = {
        'exit': 'Exits the program.',
        'help': 'Displays this screen.',
        'start': 'Starts a game.',
        'board': 'Prints the board if a game is active.',
        'play': 'Plays a piece.  Game will alternate between players automatically.',
        'captures': "Displays the state of captures.  Enter 'captures X' to display the captuers of player X."
        }

session.print_heading(welcome)
cmd = input(terminal_in)

# REPL loop
while cmd != 'exit':

    cmd = cmd.split(' ')
    nargs = len(cmd)

    if cmd[0] == 'help':
        session.print_heading(help)
        for i in possible_cmds:
            cmd = ' ' + i + ': ' + possible_cmds[i] + ' '
            session.print_option(cmd)
        session.print_sep()

    elif cmd[0] == 'start':
        if current_game.session_active:
            print('Game already started!')
        else:
            current_game.start_game()
            print("Game started.  Player 1 goes first!")
    # Active session commands only
    elif current_game.session_active:
        if cmd[0] == 'board':
            session.board_printer(current_game.board)
        
        elif nargs >= 3 and cmd[0] == 'play':
            current_game.play(int(cmd[1]), int(cmd[2]))

        elif cmd[0] == 'captures':
            if nargs > 1:
                session.print_captures(current_game.board, int(cmd[1]))
            else:
                session.print_captures(current_game.board)

    elif cmd[0] in possible_cmds:
        print('No active session!  Type "start" to start a game.')

    else:
        print("Unrecognized command.  Type 'help' for a list of commands.")
    cmd = input(terminal_in)


