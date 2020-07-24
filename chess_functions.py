import pandas as pd
import numpy as np

def parse_move(move_num, move):
    '''
    Parse attributes of algebraic chess notation.
    Board positions are transformed into 0-based indexing with row, column format.
    '''

    # Create dictionary mapping board rank to row and file to column
    row_dict = {'1':7, '2':6, '3':5, '4':4, '5':3, '6':2, '7':1, '8':0, 'nan':float('nan')}
    col_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'nan':float('nan')}

    # Create empty list to contain move list dictionaries
    move_dicts = []

    # List of special characters
    chars = ['+', '#']

    # Specify whether special characters exist in move
    chars_exist = True if any([i in chars for i in move]) else False

    # Parse attributes based on special characters
    #piece_type = None
    capture = True if 'x' in move else False
    castle = True if 'O' in move else False
    check = True if '+' in move else False
    mate = True if '#' in move else False
    promote = True if '=' in move else False
    if promote == True:
        promote_type = move[-1] if mate==False and check==False else move[-2]
    else:
        promote_type = float('nan')

    # Set color based on move number parity; even = white, odd = black
    color = 'w' if move_num % 2 == 0 else 'b'


    # Parse attributes for a move notation with 2 characters
    if len(move) == 2:
        piece_type = color+'P'
        origin_row = 'nan'
        origin_col = 'nan'
        dest_row = move[1]
        dest_col = move[0]


    # Parse attributes for a move notation with 3 characters
    if len(move) == 3:
        # Check for castling
        if castle:
            # rook move
            piece_type = color+'R'
            origin_row = 0 if color=='b' else 7
            origin_col = 7
            dest_row = 0 if color=='b' else 7
            dest_col = 5
            move_dicts.append({'move':move, 'piece':piece_type, 'origin_row':origin_row,'origin_col':origin_col,
                               'dest_row':dest_row, 'dest_col':dest_col, 'capture':capture,'promote':promote,
                               'promote_type':promote_type,'castle':castle,'check':check, 'mate':mate})
            # king move
            piece_type = color+'K'
            origin_row = 0 if color=='b' else 7
            origin_col = 4
            dest_row = 0 if color=='b' else 7
            dest_col = 6
            move_dicts.append({'move':move, 'piece':piece_type, 'origin_row':origin_row,'origin_col':origin_col,
                               'dest_row':dest_row, 'dest_col':dest_col, 'capture':capture,'promote':promote,
                               'promote_type':promote_type,'castle':castle,'check':check, 'mate':mate})
            return move_dicts
        elif chars_exist:
            piece_type = color+'P'
            origin_row = 'nan'
            origin_col = 'nan'
            dest_row = move[1]
            dest_col = move[0]
        else:
            piece_type = color+'P' if move[0].islower() else color+move[0]
            origin_row = 'nan'
            origin_col = move[0] if move[0].islower() else 'nan'
            dest_row = move[2]
            dest_col = move[1]


    # Parse attributes for a move notation with 4 characters
    if len(move) == 4:
        # Check for castling
        if castle:
            # rook move
            piece_type = color+'R'
            origin_row = 0 if color=='b' else 7
            origin_col = 7
            dest_row = 0 if color=='b' else 7
            dest_col = 5
            move_dicts.append({'move':move, 'piece':piece_type, 'origin_row':origin_row,'origin_col':origin_col,
                               'dest_row':dest_row, 'dest_col':dest_col, 'capture':capture,'promote':promote,
                               'promote_type':promote_type,'castle':castle,'check':check, 'mate':mate})
            # king move
            piece_type = color+'K'
            origin_row = 0 if color=='b' else 7
            origin_col = 4
            dest_row = 0 if color=='b' else 7
            dest_col = 6
            move_dicts.append({'move':move, 'piece':piece_type, 'origin_row':origin_row,'origin_col':origin_col,
                               'dest_row':dest_row, 'dest_col':dest_col, 'capture':capture,'promote':promote,
                               'promote_type':promote_type,'castle':castle,'check':check, 'mate':mate})
            return move_dicts
        else:
            if move[0].islower():
                piece_type = color+'P'
                origin_row = 'nan'
                origin_col = move[0] if not capture and not promote else 'nan'
                if promote:
                    dest_row = move[1]
                    dest_col = move[0]
                elif capture:
                    dest_row = move[3]
                    dest_col = move[2]
                else:
                    dest_row = move[2]
                    dest_col = move[1]
            else:
                piece_type = color+move[0]
                origin_row = move[1] if move[1].isdigit() else 'nan'
                origin_col = move[1] if not move[1].isdigit() and not capture and not chars_exist else 'nan'
                dest_row = move[2] if chars_exist else move[3]
                dest_col = move[1] if chars_exist else move[2]


    # Parse attributes for a move notation with 5 characters
    if len(move) == 5:
        # Check for castling
        if castle:
            # rook move
            piece_type = color+'R'
            origin_row = 0 if color=='b' else 7
            origin_col = 0
            dest_row = 0 if color=='b' else 7
            dest_col = 3
            move_dicts.append({'move':move, 'piece':piece_type, 'origin_row':origin_row,'origin_col':origin_col,
                               'dest_row':dest_row, 'dest_col':dest_col, 'capture':capture,'promote':promote,
                               'promote_type':promote_type,'castle':castle,'check':check, 'mate':mate})
            # king move
            piece_type = color+'K'
            origin_row = 0 if color=='b' else 7
            origin_col = 4
            dest_row = 0 if color=='b' else 7
            dest_col = 2
            move_dicts.append({'move':move, 'piece':piece_type, 'origin_row':origin_row,'origin_col':origin_col,
                               'dest_row':dest_row, 'dest_col':dest_col, 'capture':capture,'promote':promote,
                               'promote_type':promote_type,'castle':castle,'check':check, 'mate':mate})
            return move_dicts
        else:
            if move[0].islower():
                piece_type = color+'P'
                if capture:
                    origin_row = move[1] if not promote and not chars_exist else 'nan'
                    origin_col = move[0]
                    dest_row = move[4] if not chars_exist else move[3]
                    dest_col = move[3] if not chars_exist else move[2]
                elif promote:
                    origin_row = 'nan'
                    origin_col = move[0] if not chars_exist else 'nan'
                    dest_row = move[2] if not chars_exist else move[1]
                    dest_col = move[1] if not chars_exist else move[0]
            else:
                piece_type = color+move[0]
                if chars_exist:
                    origin_row = move[1] if move[1].isdigit() else 'nan'
                    origin_col = move[1] if not capture and not move[1].isdigit() else 'nan'
                    dest_row = move[3]
                    dest_col = move[2]
                elif capture:
                    origin_row = move[1] if move[1].isdigit() else 'nan'
                    origin_col = move[1] if not move[1].isdigit() else 'nan'
                    dest_row = move[4]
                    dest_col = move[3]
                else:
                    origin_row = move[2]
                    origin_col = move[1]
                    dest_row = move[4]
                    dest_col = move[3]


    # Parse attributes for a move notation with 6 characters
    if len(move)==6:
        # Check for castling
        if castle:
            # rook move
            piece_type = color+'R'
            origin_row = 0 if color=='b' else 7
            origin_col = 0
            dest_row = 0 if color=='b' else 7
            dest_col = 3
            move_dicts.append({'move':move, 'piece':piece_type, 'origin_row':origin_row,'origin_col':origin_col,
                               'dest_row':dest_row, 'dest_col':dest_col, 'capture':capture,'promote':promote,
                               'promote_type':promote_type,'castle':castle,'check':check, 'mate':mate})
            # king move
            piece_type = color+'K'
            origin_row = 0 if color=='b' else 7
            origin_col = 4
            dest_row = 0 if color=='b' else 7
            dest_col = 2
            move_dicts.append({'move':move, 'piece':piece_type, 'origin_row':origin_row,'origin_col':origin_col,
                               'dest_row':dest_row, 'dest_col':dest_col, 'capture':capture,'promote':promote,
                               'promote_type':promote_type,'castle':castle,'check':check, 'mate':mate})
            return move_dicts
        else:
            if move[0].islower():
                piece_type = color+'P'
                origin_row = 'nan'
                origin_col = move[0]
                dest_row = move[3] if capture else move[2]
                dest_col = move[2] if capture else move[1]
            else:
                piece_type = color+move[0]
                if chars_exist and capture:
                    origin_row = move[1] if move[1].isdigit() else 'nan'
                    origin_col = move[1] if not move[1].isdigit() else 'nan'
                    dest_row = move[4]
                    dest_col = move[3]
                elif chars_exist:
                    origin_row = move[2]
                    origin_col = move[1]
                    dest_row = move[4]
                    dest_col = move[3]
                else:
                    origin_row = move[2]
                    origin_col = move[1]
                    dest_row = move[5]
                    dest_col = move[4]


    # Parse attributes for a move notation with 7 characters
    if len(move)==7:
        if move[0].islower():
            piece_type = color+'P'
            origin_row = 'nan'
            origin_col = move[0]
            dest_row = move[3]
            dest_col = move[2]
        else:
            piece_type = color+move[0]
            origin_row = move[2]
            origin_col = move[1]
            dest_row = move[5]
            dest_col = move[4]


    # Return transformed move

    try:
        move_dicts.append({'move':move, 'piece':piece_type, 'origin_row':row_dict[origin_row],'origin_col':col_dict[origin_col],
                           'dest_row':row_dict[dest_row], 'dest_col':col_dict[dest_col],
                           'capture':capture,'promote':promote, 'promote_type':promote_type,
                           'castle':castle,'check':check, 'mate':mate})
        if promote:
            piece_type = color+'Q'
            move_dicts.append({'move':move, 'piece':piece_type, 'origin_row':row_dict[dest_row],'origin_col':col_dict[dest_col],
                           'dest_row':row_dict[dest_row], 'dest_col':col_dict[dest_col],
                           'capture':capture,'promote':promote, 'promote_type':promote_type,
                           'castle':castle,'check':check, 'mate':mate})
    except:
        print('Assignment error:', move_num, move)

    return(move_dicts)


def get_locs(piece):
    locs = []
    for col in board.columns:
        row_idx = list(board.loc[board[col]==piece,col].index)
        locs.extend([(i, col) for i in row_idx]) if len(row_idx)>0 else None
    return(locs)


def print_move(piece, origin_row, origin_col, dest_row, dest_col, capture, update_board = True):
    if piece[1] == 'P':
        return (piece, origin_row, origin_col, dest_row, dest_col, capture, update_board)
    elif piece[1] == 'N':
        return (piece, origin_row, origin_col, dest_row, dest_col, capture, update_board)
    elif piece[1] == 'B':
        return (piece, origin_row, origin_col, dest_row, dest_col, capture, update_board)
    elif piece[1] == 'R':
        return (piece, origin_row, origin_col, dest_row, dest_col, capture, update_board)
    elif piece[1] == 'Q':
        return (piece, origin_row, origin_col, dest_row, dest_col, capture, update_board)
    elif piece[1] == 'K':
        return (piece, origin_row, origin_col, dest_row, dest_col, capture, update_board)
    else:
        raise RuntimeError('Error in move selector')


def move_selector(piece, origin_row, origin_col, dest_row, dest_col, capture, update_board = True):
    if piece[1] == 'P':
        return pawn_move(piece=piece, origin_row=origin_row, origin_col=origin_col,
                         dest_row=dest_row, dest_col=dest_col, capture=capture, update_board = update_board)
    elif piece[1] == 'N':
        return knight_move(piece=piece, origin_row=origin_row, origin_col=origin_col,
                         dest_row=dest_row, dest_col=dest_col, capture=capture, update_board = update_board)
    elif piece[1] == 'B':
        return bishop_move(piece=piece, origin_row=origin_row, origin_col=origin_col,
                         dest_row=dest_row, dest_col=dest_col, capture=capture, update_board = update_board)
    elif piece[1] == 'R':
        return rook_move(piece=piece, origin_row=origin_row, origin_col=origin_col,
                         dest_row=dest_row, dest_col=dest_col, capture=capture, update_board = update_board)
    elif piece[1] == 'Q':
        return queen_move(piece=piece, origin_row=origin_row, origin_col=origin_col,
                         dest_row=dest_row, dest_col=dest_col, capture=capture, update_board = update_board)
    elif piece[1] == 'K':
        return king_move(piece=piece, origin_row=origin_row, origin_col=origin_col,
                         dest_row=dest_row, dest_col=dest_col, capture=capture, update_board = update_board)
    else:
        raise RuntimeError('Error in move selector')


def pawn_move(piece, origin_row, origin_col, dest_row, dest_col, capture, update_board = True):
    print(piece, (origin_row, origin_col), (dest_row, dest_col))
    sign = -1 if piece[0] == 'w' else 1
    if capture:
        o_row = dest_row-(1*sign) if pd.isna(origin_row) else origin_row
        if not pd.isna(origin_col):
            o_col = origin_col
        elif board.iloc[o_row, (dest_col-1)]==piece:
            o_col = dest_col-1
        elif board.iloc[o_row, (dest_col+1)]==piece:
            o_col = dest_col+1
        else:
            raise RuntimeError(f'Origin not found for {piece} moving to ({dest_row}, {dest_col})')
    else:
        if board.iloc[(dest_row-(1*sign)),dest_col] == piece and pd.isna(board.iloc[dest_row, dest_col]):
            o_row = dest_row-(1*sign)
            o_col = dest_col
        elif board.iloc[(dest_row-(2*sign)),dest_col] == piece and pd.isna(board.iloc[dest_row, dest_col]):
            o_row = dest_row-(2*sign)
            o_col = dest_col
        else:
            raise RuntimeError(f'Origin not found for {piece} moving to ({dest_row}, {dest_col})')
    if update_board:
        board.iloc[o_row, o_col] = float('nan')
        board.iloc[dest_row, dest_col] = piece
    return (o_row, o_col)


def knight_move(piece, origin_row, origin_col, dest_row, dest_col, capture, update_board = True):
    locs = get_locs(piece)
    o_row, o_col = (float('nan'), float('nan'))
    if not pd.isna(origin_row) and not pd.isna(origin_col):
        o_row, o_col = (origin_row, origin_col)
    elif not pd.isna(origin_row):
        o_row, o_col = [i for i in locs if i[0] == origin_row][0]
    elif not pd.isna(origin_col):
        o_row, o_col = [i for i in locs if i[1] == origin_col][0]
    else:
        for i in locs:
            if (abs(dest_row-i[0])==2 and abs(dest_col-i[1])==1) or (abs(dest_row-i[0])==1 and abs(dest_col-i[1])==2):
                o_row, o_col = i
            else:
                continue
    if not pd.isna(o_row) and not pd.isna(o_col):
        if update_board:
            board.iloc[o_row, o_col] = float('nan')
            board.iloc[dest_row, dest_col] = piece
        return (o_row, o_col)
    else:
        raise RuntimeError(f'Origin not found for {piece} moving to ({dest_row}, {dest_col})')


def bishop_move(piece, origin_row, origin_col, dest_row, dest_col, capture, update_board = True):
    locs = get_locs(piece)
    o_row, o_col = (float('nan'), float('nan'))
    if not pd.isna(origin_row) and not pd.isna(origin_col):
        o_row, o_col = (origin_row, origin_col)
    elif not pd.isna(origin_row):
        o_row, o_col = [i for i in locs if i[0] == origin_row][0]
    elif not pd.isna(origin_col):
        o_row, o_col = [i for i in locs if i[1] == origin_col][0]
    else:
        for i in locs:
            curr_row, curr_col = i
            row_dist = dest_row - curr_row
            row_sign = 1 if curr_row < dest_row else -1
            col_dist = dest_col - curr_col
            col_sign = 1 if curr_col < dest_col else -1
            if abs(row_dist) != abs(col_dist):
                continue
            else:
                check_list = []
                while (curr_row*row_sign) <= (dest_row*row_sign):
                    check_list.append(0) if pd.isna(board.iloc[curr_row, curr_col]) else check_list.append(1)
                    curr_row += (1*row_sign)
                    curr_col += (1*col_sign)
                check_list.pop if capture == True else None
                if sum(check_list) == 0:
                    o_row, o_col = i
    if not pd.isna(o_row) and not pd.isna(o_col):
        if update_board:
            board.iloc[o_row, o_col] = float('nan')
            board.iloc[dest_row, dest_col] = piece
        return (o_row, o_col)
    else:
        raise RuntimeError(f'Origin not found for {piece} moving to ({dest_row}, {dest_col})')


def rook_move(piece, origin_row, origin_col, dest_row, dest_col, capture, update_board = True):
    locs = get_locs(piece)
    o_row, o_col = (float('nan'), float('nan'))
    if not pd.isna(origin_row) and not pd.isna(origin_col):
        o_row, o_col = (origin_row, origin_col)
    elif not pd.isna(origin_row):
        o_row, o_col = [i for i in locs if i[0] == origin_row][0]
    elif not pd.isna(origin_col):
        o_row, o_col = [i for i in locs if i[1] == origin_col][0]
    else:
        for i in locs:
            curr_row, curr_col = i
            if dest_row != curr_row and dest_col != curr_col:
                continue
            else:
                if curr_row == dest_row:
                    col_sign = 1 if curr_col < dest_col else -1
                    check_list = []
                    while (curr_col*col_sign) <= (dest_col*col_sign):
                        check_list.append(0) if pd.isna(board.iloc[dest_row, curr_col]) else check_list.append(1)
                        curr_col += (1*col_sign)
                    check_list.pop if capture == True else None
                    if sum(check_list) == 0:
                        o_row, o_col = i
                if curr_col == dest_col:
                    row_sign = 1 if curr_row < dest_row else -1
                    check_list = []
                    while (curr_row*row_sign) <= (dest_row*row_sign):
                        check_list.append(0) if pd.isna(board.iloc[curr_row, dest_col]) else check_list.append(1)
                        curr_row += (1*row_sign)
                    check_list.pop if capture == True else None
                    if sum(check_list) == 0:
                        o_row, o_col = i
    if not pd.isna(o_row) and not pd.isna(o_col):
        if update_board:
            board.iloc[o_row, o_col] = float('nan')
            board.iloc[dest_row, dest_col] = piece
        return (o_row, o_col)
    else:
        raise RuntimeError(f'Origin not found for {piece} moving to ({dest_row}, {dest_col})')


def queen_move(piece, origin_row, origin_col, dest_row, dest_col, capture, update_board = True):
    try:
        return bishop_move(piece=piece, origin_row=origin_row, origin_col=origin_col,
                           dest_row=dest_row, dest_col=dest_col, capture=capture)
    except:
        return rook_move(piece=piece, origin_row=origin_row, origin_col=origin_col,
                         dest_row=dest_row, dest_col=dest_col, capture=capture)


def king_move(piece, origin_row, origin_col, dest_row, dest_col, capture, update_board = True):
    locs = get_locs(piece)
    o_row, o_col = locs
    if update_board:
        board.iloc[o_row, o_col] = float('nan')
        board.iloc[dest_row, dest_col] = piece
    return (o_row, o_col)