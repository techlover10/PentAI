#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Main file for PentAI - launches the REPL to run
# whatever command is desired.

from terminal import Printer
import game.Game as game
import importlib

session = Printer.Printer()

terminal_in = 'PentAI> '
welcome = 'Welcome to PentAI'
help = 'PentAI: Help Manual'

current_game = None

# list of all commands for operating at the toplevel
possible_cmds = {
        'exit': 'Exits the program.',
        'help': 'Displays this screen.',
        'start': 'Starts a game.',
        'board': 'Prints the board if a game is active.',
        'play': 'Plays a piece.  Game will alternate between players automatically.  Game board is 1-indexed.',
        'captures': "Displays the state of captures.  Enter 'captures X' to display the captures of player X.",
        'turn': "Displays the player of the current turn",
        'state_val': "Displays the value of the current state for the current player"
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
        if current_game and current_game.session_active:
            print('Game already started!')
        else:
            agentstr = 'agents.'
            if len(cmd) >2:
                # Both players are AI
                try:
                    agent_pkg1 = importlib.import_module(agentstr + cmd[1])
                except ImportError as e:
                    print("Invalid agent name: " + cmd[1])
                try:
                    agent_pkg2 = importlib.import_module(agentstr + cmd[2])
                    agent1 = agent_pkg1.Agent()
                    agent2 = agent_pkg2.Agent()
                    current_game = game.Game(agent1, agent2)
                except ImportError as e:
                    print("Invalid agent name: " + cmd[2])
            elif len(cmd) >1:
                # Player 1 is an AI, player 2 is human
                try:
                    agent_pkg1 = importlib.import_module(agentstr + cmd[1])
                    agent1 = agent_pkg1.Agent()
                    current_game = game.Game(agent1)
                except ImportError as e:
                    print("Invalid agent name: " + cmd[1])
            else:
                # Both players are human
                current_game = game.Game()
            if current_game:
                print("Game started.  Player 1 goes first!")
                current_game.start_game()
    # Active session commands only
    elif current_game and current_game.session_active:
        if cmd[0] == 'board':
            session.board_printer(current_game.board)
        
        elif nargs >= 3 and cmd[0] == 'play':
            current_game.play(int(cmd[1])-1, int(cmd[2])-1)

        elif nargs <3 and cmd[0] == 'play':
            print("Invalid position specified.")

        elif cmd[0] == 'captures':
            if nargs > 1:
                session.print_captures(current_game.board, int(cmd[1]))
            else:
                session.print_captures(current_game.board)

        elif cmd[0] == 'turn':
            session.print_heading('Player ' + str(current_game.current_turn) + "'s turn")

        elif cmd[0] == 'value':
            new_agent = MinimaxAgent.MinimaxAgent()
            print("Heuristic value for player " + str(current_game.current_turn))
            print(new_agent.value_state(current_game.board, current_game.current_turn))

        elif cmd[0] == 'reset':
            current_game.reset()
            

    elif cmd[0] in possible_cmds:
        print('No active session!  Type "start" to start a game.')

    else:
        print("Unrecognized command.  Type 'help' for a list of commands.")
    cmd = input(terminal_in)


