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

    # Note: board is indexed with origin being the top left corner 
    # with coordinates (0,0), toplevel gameplay is 1-adjusted
    if direction == 'l':
        return 1 + line_count(board, xcoord, ycoord-1, direction, player)
    if direction == 'r':
        return 1 + line_count(board, xcoord, ycoord+1, direction, player)
    if direction == 'u':
        return 1 + line_count(board, xcoord-1, ycoord, direction, player)
    if direction == 'd':
        return 1 + line_count(board, xcoord+1, ycoord, direction, player)
    if direction == 'ul':
        return 1 + line_count(board, xcoord-1, ycoord-1, direction, player)
    if direction == 'ur':
        return 1 + line_count(board, xcoord-1, ycoord+1, direction, player)
    if direction == 'dl':
        return 1 + line_count(board, xcoord+1, ycoord-1, direction, player)
    if direction == 'dr':
        return 1 + line_count(board, xcoord+1, ycoord+1, direction, player)

# Main function for checking for win
def check_win(board, xcoord, ycoord, player):
    #print("checking win: " + str(xcoord) + ',' + str(ycoord))
    if line_count(board, xcoord, ycoord-1, 'l', player) + line_count(board, xcoord, ycoord+1, 'r', player) + 1 >= 5:
        return True
    if line_count(board, xcoord+1, ycoord-1, 'dl', player) + line_count(board, xcoord-1, ycoord+1, 'ur', player) + 1 >= 5:
        return True
    if line_count(board, xcoord-1, ycoord-1, 'ul', player) + line_count(board, xcoord+1, ycoord+1, 'dr', player) + 1 >= 5:
        return True
    if line_count(board, xcoord-1, ycoord, 'u', player) + line_count(board, xcoord+1, ycoord, 'd', player) + 1 >= 5:
        return True
    result = check_capture(board, xcoord, ycoord, player)
    board.captures[player] += result
    if (board.get_captures(player)) >= 5:
        return True

    return False

def check_capture(board, xcoord, ycoord, player):
    result = 0
    other_player = 0
    if (player == 1):
        other_player = 2
    else:
        other_player = 1
    if (board.get_piece(xcoord, ycoord) == other_player):
        return result
    if (board.get_piece(xcoord + 3, ycoord) == player):
        if (not board.spot_empty(xcoord + 1, ycoord) and board.get_piece(xcoord + 1, ycoord) == other_player 
            and not board.spot_empty(xcoord + 2, ycoord) and board.get_piece(xcoord + 2, ycoord) == other_player):
            board.piece_captured(xcoord + 1, ycoord)
            board.piece_captured(xcoord + 2, ycoord)
            result += 1 
    if (board.get_piece(xcoord - 3, ycoord) == player):
        if (not board.spot_empty(xcoord - 1, ycoord) and board.get_piece(xcoord - 1, ycoord) == other_player 
            and not board.spot_empty(xcoord - 2, ycoord) and board.get_piece(xcoord - 2, ycoord) == other_player):
            board.piece_captured(xcoord - 1, ycoord)
            board.piece_captured(xcoord - 2, ycoord)
            result += 1 
    if (board.get_piece(xcoord, ycoord + 3) == player):
        if (not board.spot_empty(xcoord, ycoord + 1) and board.get_piece(xcoord, ycoord + 1) == other_player 
            and not board.spot_empty(xcoord, ycoord + 2) and board.get_piece(xcoord, ycoord + 2) == other_player):
            board.piece_captured(xcoord, ycoord + 1)
            board.piece_captured(xcoord, ycoord + 2)
            result += 1 
    if (board.get_piece(xcoord, ycoord - 3) == player):
        if (not board.spot_empty(xcoord, ycoord - 1) and board.get_piece(xcoord, ycoord -1) == other_player 
            and not board.spot_empty(xcoord, ycoord - 2) and board.get_piece(xcoord, ycoord - 2) == other_player):
            board.piece_captured(xcoord, ycoord - 1)
            board.piece_captured(xcoord, ycoord - 2)
            result += 1 
    if (board.get_piece(xcoord + 3, ycoord + 3) == player):
        if (not board.spot_empty(xcoord + 1, ycoord + 1) and board.get_piece(xcoord + 1, ycoord + 1) == other_player 
            and not board.spot_empty(xcoord + 2, ycoord +2) and board.get_piece(xcoord + 2, ycoord + 2) == other_player):
            board.piece_captured(xcoord + 1, ycoord + 1)
            board.piece_captured(xcoord + 2, ycoord + 2)
            result += 1 
    if (board.get_piece(xcoord - 3, ycoord - 3) == player):
        if (not board.spot_empty(xcoord - 1, ycoord - 1) and board.get_piece(xcoord - 1, ycoord - 1) == other_player 
            and not board.spot_empty(xcoord - 2, ycoord - 2) and board.get_piece(xcoord - 2, ycoord - 2) == other_player):
            board.piece_captured(xcoord - 1, ycoord - 1)
            board.piece_captured(xcoord - 2, ycoord - 2)
            result += 1
    if (board.get_piece(xcoord + 3, ycoord - 3) == player):
        if (not board.spot_empty(xcoord + 1, ycoord - 1) and board.get_piece(xcoord + 1, ycoord - 1) == other_player 
            and not board.spot_empty(xcoord + 2, ycoord - 2) and board.get_piece(xcoord + 2, ycoord - 2) == other_player):
            board.piece_captured(xcoord + 1, ycoord - 1)
            board.piece_captured(xcoord + 2, ycoord - 2)
            result += 1  
    if (board.get_piece(xcoord - 3, ycoord + 3) == player):
        if (not board.spot_empty(xcoord - 1, ycoord + 1) and board.get_piece(xcoord - 1, ycoord + 1) == other_player 
            and not board.spot_empty(xcoord - 2, ycoord + 2) and board.get_piece(xcoord - 2, ycoord + 2) == other_player):
            board.piece_captured(xcoord - 1, ycoord + 1)
            board.piece_captured(xcoord - 2, ycoord + 2)
            result += 1 
    return result

