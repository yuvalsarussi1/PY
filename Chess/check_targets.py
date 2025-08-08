
def board_pass(matrix, ):
    for row in range(8):
        for col in range(8):
            piece = matrix[row][col]
    return piece

def check_knight_targets(matrix,turn,row,col):

    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),(-2, -1), (-1, -2), (1, -2), (2, -1)]
    
    for dx, dy in knight_moves:
        check_x = row + dx
        check_y = col + dy
        if 0 <= check_x < 8 and 0 <= check_y < 8:
            target = matrix[check_x][check_y]
            if turn and target == "K":
                return True
            elif not turn and target == "k":
                return True

    return False

def is_in_check(matrix, turn):
    king_symbol = "K" if turn else "k"
    enemy_pieces = {
        "P": turn is False,  # black's turn → white pawns are enemy
        "p": turn is True,
        "N": turn is False,
        "n": turn is True,
        "B": turn is False,
        "b": turn is True,
        "R": turn is False,
        "r": turn is True,
        "Q": turn is False,
        "q": turn is True,
        "K": turn is False,
        "k": turn is True
    }

    # Step 1: Locate the king
    king_pos = None
    for row in range(8):
        for col in range(8):
            if matrix[row][col] == king_symbol:
                king_pos = (row, col)
                break
        if king_pos:
            break

    if not king_pos:
        return False  # No king on board

    king_x, king_y = king_pos

    # Step 2: Check for knight threats
    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                    (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for dx, dy in knight_moves:
        x, y = king_x + dx, king_y + dy
        if 0 <= x < 8 and 0 <= y < 8:
            piece = matrix[x][y]
            if piece in enemy_pieces and piece.lower() == 'n':
                return True

    # Step 3: Check straight lines (rook/queen)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in directions:
        x, y = king_x, king_y
        while True:
            x += dx
            y += dy
            if not (0 <= x < 8 and 0 <= y < 8):
                break
            piece = matrix[x][y]
            if piece == "-":
                continue
            if piece in enemy_pieces and (piece.lower() == 'r' or piece.lower() == 'q'):
                return True
            break  # blocked by any piece

    # Step 4: Check diagonals (bishop/queen/pawn)
    diagonals = [(1,1), (1,-1), (-1,1), (-1,-1)]
    for dx, dy in diagonals:
        x, y = king_x, king_y
        while True:
            x += dx
            y += dy
            if not (0 <= x < 8 and 0 <= y < 8):
                break
            piece = matrix[x][y]
            if piece == "-":
                continue
            if piece in enemy_pieces:
                if piece.lower() == 'b' or piece.lower() == 'q':
                    return True
                # check pawn diagonals
                if piece.lower() == 'p':
                    if turn and dx == -1:  # white king, black pawn
                        return True
                    elif not turn and dx == 1:  # black king, white pawn
                        return True
            break

    # Step 5: Check adjacent king
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            x = king_x + dx
            y = king_y + dy
            if 0 <= x < 8 and 0 <= y < 8:
                piece = matrix[x][y]
                if piece in enemy_pieces and piece.lower() == 'k':
                    return True

    return False