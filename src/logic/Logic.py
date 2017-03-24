#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Logic for checking a board for a win state

# Checks for a win given a pair of coordinates
# board is a game board to check
# xcoord and ycoord denote the coordinates of the piece
# direction denotes the direction for counting
# player indicates the player we are checking
# direction can be one of 'l', 'r', 'u', 'd', 'ul',
# 'ur', 'dl', 'dr'
def line_count(board, xcoord, ycoord, direction, player):

    # base cases
    if xcoord < 0 or xcoord >= 19 or ycoord < 0 or ycoord >= 19:
        return 0
    if board.get_piece(xcoord, ycoord) != player:
        return 0

    if direction == 'l':
        return 1 + line_count(board, xcoord-1, ycoord, direction, player)
    if direction == 'r':
        return 1 + line_count(board, xcoord+1, ycoord, direction, player)
    if direction == 'u':
        return 1 + line_count(board, xcoord, ycoord-1, direction, player)
    if direction == 'd':
        return 1 + line_count(board, xcoord-1, ycoord+1, direction, player)
    if direction == 'ul':
        return 1 + line_count(board, xcoord-1, ycoord-1, direction, player)
    if direction == 'ur':
        return 1 + line_count(board, xcoord+1, ycoord-1, direction, player)
    if direction == 'dl':
        return 1 + line_count(board, xcoord-1, ycoord+1, direction, player)
    if direction == 'dr':
        return 1 + line_count(board, xcoord+1, ycoord+1, direction, player)

# Main function for checking for win
def check_win(board, xcoord, ycoord, player):
    #print("checking win: " + str(xcoord) + ',' + str(ycoord))
    if line_count(board, xcoord, ycoord, 'l', player) + line_count(board, xcoord, ycoord, 'r', player + 1) >= 5:
        return True
    if line_count(board, xcoord, ycoord, 'dl', player) + line_count(board, xcoord, ycoord, 'ur', player + 1) >= 5:
        return True
    if line_count(board, xcoord, ycoord, 'ul', player) + line_count(board, xcoord, ycoord, 'dr', player + 1) >= 5:
        return True
    if line_count(board, xcoord, ycoord, 'u', player) + line_count(board, xcoord, ycoord, 'd', player + 1) >= 5:
        return True

    if (board.get_captures(player)) >= 5:
        return True

    return False

def check_capture(board, xcoord, ycoord, player):
    # TODO: Implement
    return False

