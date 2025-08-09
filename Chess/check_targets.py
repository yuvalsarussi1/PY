from board import setup_board


def _ray_cast(x, y, matrix, dx, dy, size=8):
    """Walk one direction until edge or first blocker.
    Return all squares along the ray, including the first occupied square,
    and stop there (can't threaten past a blocker)."""
    path = []
    nx, ny = x + dx, y + dy
    while 0 <= nx < size and 0 <= ny < size:
        path.append((nx, ny))
        if matrix[nx][ny] != "-":   # blocker encountered; include and stop
            break
        nx += dx
        ny += dy
    return path

# === Threats_of_piece ===
def pawn_threat(x, y, turn, threatens, size=8):
    # Determine which direction the pawn attacks
    if turn:  # White pawn → attacks upward (row index decreases)
        deltas = [(-1, -1), (-1, 1)]
    else:     # Black pawn → attacks downward (row index increases)
        deltas = [(1, -1), (1, 1)]

    targets = []
    for dx, dy in deltas:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:  # Stay within board
            targets.append((nx, ny))

    threatens.setdefault((x, y), []).extend(targets)
    return threatens

def king_threat(x, y, threatens, size=8):
    deltas = [(1, 0), (1, 1), (1, -1),
              (0, 1), (0, -1),
              (-1, 0), (-1, 1), (-1, -1)]

    targets = []
    for dx, dy in deltas:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:  # stay on board
            targets.append((nx, ny))

    threatens.setdefault((x, y), []).extend(targets)
    return threatens

def knight_threat(x, y, threatens, size=8):
    deltas = [(2, 1), (1, 2), (-1, 2), (-2, 1),
              (-2, -1), (-1, -2), (1, -2), (2, -1)]
    targets = []
    for dx, dy in deltas:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:
            targets.append((nx, ny))
    threatens.setdefault((x, y), []).extend(targets)
    return threatens
    
def bishop_threat(x, y, matrix, threatens, size=8):
    rays = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    targets = []
    for dx, dy in rays:
        targets.extend(_ray_cast(x, y, matrix, dx, dy, size))
    threatens.setdefault((x, y), []).extend(targets)
    return threatens

def rook_threat(x, y, matrix, threatens, size=8):
    rays = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    targets = []
    for dx, dy in rays:
        targets.extend(_ray_cast(x, y, matrix, dx, dy, size))
    threatens.setdefault((x, y), []).extend(targets)
    return threatens

def queen_threat(x, y, matrix, threatens, size=8):
    # queen = rook + bishop
    bishop_threat(x, y, matrix, threatens, size)
    rook_threat(x, y, matrix, threatens, size)
    return threatens

#=== Threats_Functions ===
def board_threat_check(matrix):
    threatens = {}
    for row in range(8):
        for col in range(8):
            p = matrix[row][col]
            if p == "-":
                continue
            is_white = p.isupper()

            if p in ("P", "p"):
                pawn_threat(row, col, is_white, threatens)
            elif p in ("K", "k"):
                king_threat(row, col, threatens)
            elif p in ("N", "n"):
                knight_threat(row, col, threatens)
            elif p in ("B", "b"):
                bishop_threat(row, col, matrix, threatens)
            elif p in ("R", "r"):
                rook_threat(row, col, matrix, threatens)      # <-- pass threatens
            elif p in ("Q", "q"):
                queen_threat(row, col, matrix, threatens)
    return threatens

def print_threatens(threatens):
    for piece, positions in threatens.items():
        print(f"{piece}: {positions}")

#=== King_Check ===
def king_in_check(matrix,threatens,black_pieces,white_pieces):
    check_black = False
    check_white = False
    
    for key,values in threatens.items():
        attacker = matrix[key[0]][key[1]]
        
        for value_x, value_y in values:
            target = matrix[value_x][value_y]
            
            if target == "k" and attacker in white_pieces:
                print(f"Black King in check! Attacked by {white_pieces[attacker]} from {key}")
                check_black = True

            elif target == "K" and attacker in black_pieces:
                print(f"White King in check! Attacked by {black_pieces[attacker]} from {key}")
                check_white = True

    return check_white,check_black
