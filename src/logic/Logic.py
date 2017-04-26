#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Logic for checking a board for a win state

# Checks for a win given a pair of coordinates
# board is a game board to check
# r and c denote the coordinates of the piece
# direction denotes the direction for counting
# player indicates the player we are checking
# direction can be one of 'l', 'r', 'u', 'd', 'ul',
# 'ur', 'dl', 'dr'
def line_count(board, r, c, direction, player):

    # base cases
    if r < 0 or r >= 19 or c < 0 or c >= 19:
        return 0
    if board.get_piece(r, c) != player:
        return 0

    # Note: board is indexed with origin being the top left corner 
    # with coordinates (0,0), toplevel gameplay is 1-adjusted
    if direction == 'l':
        return 1 + line_count(board, r, c-1, direction, player)
    if direction == 'r':
        return 1 + line_count(board, r, c+1, direction, player)
    if direction == 'u':
        return 1 + line_count(board, r-1, c, direction, player)
    if direction == 'd':
        return 1 + line_count(board, r+1, c, direction, player)
    if direction == 'ul':
        return 1 + line_count(board, r-1, c-1, direction, player)
    if direction == 'ur':
        return 1 + line_count(board, r-1, c+1, direction, player)
    if direction == 'dl':
        return 1 + line_count(board, r+1, c-1, direction, player)
    if direction == 'dr':
        return 1 + line_count(board, r+1, c+1, direction, player)

# Main function for checking for win
def check_win(board, r, c, player):
    #print("checking win: " + str(r) + ',' + str(c))
    if line_count(board, r, c-1, 'l', player) + line_count(board, r, c+1, 'r', player) + 1 >= 5:
        #print("left")
        return True
    if line_count(board, r+1, c-1, 'dl', player) + line_count(board, r-1, c+1, 'ur', player) + 1 >= 5:
        #print("bottom left")
        return True
    if line_count(board, r-1, c-1, 'ul', player) + line_count(board, r+1, c+1, 'dr', player) + 1 >= 5:
        #print("top left")
        return True
    if line_count(board, r-1, c, 'u', player) + line_count(board, r+1, c, 'd', player) + 1 >= 5:
        #print("up")
        return True
    result = check_capture(board, r, c, player)
    board.captures[player] = board.captures[player] + result
    if (board.get_captures(player)) >= 5:
        #print("captures")
        return True

    return False

def heuristic_count(board, r, c, player):
    counts = {
        'horizontal': line_count(board, r, c-1, 'l', player) + line_count(board, r, c+1, 'r', player) + 1,
        'top_right': line_count(board, r+1, c-1, 'dl', player) + line_count(board, r-1, c+1, 'ur', player) + 1,
        'top_left': line_count(board, r-1, c-1, 'ul', player) + line_count(board, r+1, c+1, 'dr', player) + 1,
        'vertical': line_count(board, r-1, c, 'u', player) + line_count(board, r+1, c, 'd', player) + 1,
        'capture': check_capture(board, r, c, player) + board.captures[player]
        }
    return counts

def check_capture(board, r, c, player):
    result = 0
    other_player = 0
    if (player == 1):
        other_player = 2
    else:
        other_player = 1
    if (board.get_piece(r, c) == other_player):
        return result
    if (board.get_piece(r + 3, c) == player):
        if (not board.spot_empty(r + 1, c) and board.get_piece(r + 1, c) == other_player 
            and not board.spot_empty(r + 2, c) and board.get_piece(r + 2, c) == other_player):
            board.piece_captured(r + 1, c)
            board.piece_captured(r + 2, c)
            result += 1 
    if (board.get_piece(r - 3, c) == player):
        if (not board.spot_empty(r - 1, c) and board.get_piece(r - 1, c) == other_player 
            and not board.spot_empty(r - 2, c) and board.get_piece(r - 2, c) == other_player):
            board.piece_captured(r - 1, c)
            board.piece_captured(r - 2, c)
            result += 1 
    if (board.get_piece(r, c + 3) == player):
        if (not board.spot_empty(r, c + 1) and board.get_piece(r, c + 1) == other_player 
            and not board.spot_empty(r, c + 2) and board.get_piece(r, c + 2) == other_player):
            board.piece_captured(r, c + 1)
            board.piece_captured(r, c + 2)
            result += 1 
    if (board.get_piece(r, c - 3) == player):
        if (not board.spot_empty(r, c - 1) and board.get_piece(r, c -1) == other_player 
            and not board.spot_empty(r, c - 2) and board.get_piece(r, c - 2) == other_player):
            board.piece_captured(r, c - 1)
            board.piece_captured(r, c - 2)
            result += 1 
    if (board.get_piece(r + 3, c + 3) == player):
        if (not board.spot_empty(r + 1, c + 1) and board.get_piece(r + 1, c + 1) == other_player 
            and not board.spot_empty(r + 2, c +2) and board.get_piece(r + 2, c + 2) == other_player):
            board.piece_captured(r + 1, c + 1)
            board.piece_captured(r + 2, c + 2)
            result += 1 
    if (board.get_piece(r - 3, c - 3) == player):
        if (not board.spot_empty(r - 1, c - 1) and board.get_piece(r - 1, c - 1) == other_player 
            and not board.spot_empty(r - 2, c - 2) and board.get_piece(r - 2, c - 2) == other_player):
            board.piece_captured(r - 1, c - 1)
            board.piece_captured(r - 2, c - 2)
            result += 1
    if (board.get_piece(r + 3, c - 3) == player):
        if (not board.spot_empty(r + 1, c - 1) and board.get_piece(r + 1, c - 1) == other_player 
            and not board.spot_empty(r + 2, c - 2) and board.get_piece(r + 2, c - 2) == other_player):
            board.piece_captured(r + 1, c - 1)
            board.piece_captured(r + 2, c - 2)
            result += 1  
    if (board.get_piece(r - 3, c + 3) == player):
        if (not board.spot_empty(r - 1, c + 1) and board.get_piece(r - 1, c + 1) == other_player 
            and not board.spot_empty(r - 2, c + 2) and board.get_piece(r - 2, c + 2) == other_player):
            board.piece_captured(r - 1, c + 1)
            board.piece_captured(r - 2, c + 2)
            result += 1 
    return result

