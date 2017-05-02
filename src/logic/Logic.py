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
    other_player = 2 if player is 1 else 1
    # base cases
    if r < 0 or r >= 19 or c < 0 or c >= 19:
        return (0, False)
    if board.get_piece(r, c) != player:
        if board.get_piece(r, c) == other_player:
            return (0, True)
        return (0, False)
    # Note: board is indexed with origin being the top left corner 
    # with coordinates (0,0), toplevel gameplay is 1-adjusted
    count = 0
    if direction == 'l':
        count = line_count(board, r, c-1, direction, player)
    if direction == 'r':
        count = line_count(board, r, c+1, direction, player)
    if direction == 'u':
        count = line_count(board, r-1, c, direction, player)
    if direction == 'd':
        count = line_count(board, r+1, c, direction, player)
    if direction == 'ul':
        count = line_count(board, r-1, c-1, direction, player)
    if direction == 'ur':
        count = line_count(board, r-1, c+1, direction, player)
    if direction == 'dl':
        count = line_count(board, r+1, c-1, direction, player)
    if direction == 'dr':
        count = line_count(board, r+1, c+1, direction, player)
    return (1 + count[0], count[1])

# Main function for checking for win
def check_win(board, r, c, player):

    #print("checking win: " + str(r) + ',' + str(c))
    if line_count(board, r, c-1, 'l', player)[0] + line_count(board, r, c+1, 'r', player)[0] + 1 >= 5:
        #print("left")
        return True
    if line_count(board, r+1, c-1, 'dl', player)[0] + line_count(board, r-1, c+1, 'ur', player)[0] + 1 >= 5:
        #print("bottom left")
        return True
    if line_count(board, r-1, c-1, 'ul', player)[0] + line_count(board, r+1, c+1, 'dr', player)[0] + 1 >= 5:
        #print("top left")
        return True
    if line_count(board, r-1, c, 'u', player)[0] + line_count(board, r+1, c, 'd', player)[0] + 1 >= 5:
        #print("up")
        return True
    result = check_capture(board, r, c, player)
    board.captures[player] = board.captures[player] + result
    if (board.get_captures(player)) >= 5:
        #print("captures")
        return True

    return False

def heuristic_count(board, r, c, player):
    other_player = 2 if player is 1 else 1
    if board.get_piece(r, c) != player:
        horizontal = 0
        top_right = 0
        top_left = 0
        vertical = 0
    else:
        left = line_count(board, r, c-1, 'l', player)
        right = line_count(board, r, c+1, 'r', player)

        horizontal = left[0] + right[0] + 1
        if left[1] and right[1]:
            horizontal = 0

        down_left = line_count(board, r+1, c-1, 'dl', player)
        up_right = line_count(board, r-1, c+1, 'ur', player)

        top_right = down_left[0] + up_right[0] + 1
        if down_left[1] and up_right[1]:
            top_right = 0

        up_left = line_count(board, r-1, c-1, 'ul', player)
        down_right = line_count(board, r+1, c+1, 'dr', player)

        top_left = up_left[0] + down_right[0] + 1
        if up_left[1] and down_right[1]:
            top_left = 0

        up = line_count(board, r-1, c, 'u', player)
        down = line_count(board, r+1, c, 'd', player)

        vertical = up[0] + down[0] + 1
        if up[1] and down[1]:
            vertical = 0

    counts = {
        'horizontal': horizontal,
        'top_right': top_right,
        'top_left': top_left,
        'vertical': vertical,
        'capture': check_capture(board, r, c, player) + board.captures[player]
        }
    return counts

def check_capture(board, r, c, player):
    result = 0
    other_player = 2 if player is 1 else 1
    if (board.get_piece(r, c) != player):
        return result
    if (board.get_piece(r + 3, c) == player):
        if (board.get_piece(r + 1, c) == other_player and board.get_piece(r + 2, c) == other_player):
            board.piece_captured(r + 1, c)
            board.piece_captured(r + 2, c)
            result += 1 
            print('1')
    if (board.get_piece(r - 3, c) == player):
        if (board.get_piece(r - 1, c) == other_player and board.get_piece(r - 2, c) == other_player):
            board.piece_captured(r - 1, c)
            board.piece_captured(r - 2, c)
            result += 1
            print('2') 
    if (board.get_piece(r, c + 3) == player):
        if (board.get_piece(r, c + 1) == other_player and board.get_piece(r, c + 2) == other_player):
            board.piece_captured(r, c + 1)
            board.piece_captured(r, c + 2)
            result += 1
            print('3') 
    if (board.get_piece(r, c - 3) == player):
        if (board.get_piece(r, c -1) == other_player and board.get_piece(r, c - 2) == other_player):
            board.piece_captured(r, c - 1)
            board.piece_captured(r, c - 2)
            result += 1
            print('4') 
    if (board.get_piece(r + 3, c + 3) == player):
        if (board.get_piece(r + 1, c + 1) == other_player and board.get_piece(r + 2, c + 2) == other_player):
            board.piece_captured(r + 1, c + 1)
            board.piece_captured(r + 2, c + 2)
            result += 1
            print('5') 
    if (board.get_piece(r - 3, c - 3) == player):
        if (board.get_piece(r - 1, c - 1) == other_player and board.get_piece(r - 2, c - 2) == other_player):
            board.piece_captured(r - 1, c - 1)
            board.piece_captured(r - 2, c - 2)
            result += 1
            print('6')
    if (board.get_piece(r + 3, c - 3) == player):
        if (board.get_piece(r + 1, c - 1) == other_player and board.get_piece(r + 2, c - 2) == other_player):
            board.piece_captured(r + 1, c - 1)
            board.piece_captured(r + 2, c - 2)
            result += 1
            print('7')  
    if (board.get_piece(r - 3, c + 3) == player):
        if (board.get_piece(r - 1, c + 1) == other_player and board.get_piece(r - 2, c + 2) == other_player):
            board.piece_captured(r - 1, c + 1)
            board.piece_captured(r - 2, c + 2)
            result += 1
            print('8') 
    return result

