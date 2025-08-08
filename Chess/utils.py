

# === Coordinate & Board Helpers ===

def is_enemy_or_empty(matrix, x, y, cx, cy, white_pieces, black_pieces): 
    return not (
        (matrix[cx][cy] in white_pieces and matrix[x][y] in white_pieces) or
        (matrix[cx][cy] in black_pieces and matrix[x][y] in black_pieces)
    )

def clear_path(matrix, x, y, cx, cy): #true if the path is clear for sliding pieces
    dx = abs(cx - x)
    dy = abs(cy - y)
    distance = max(dx, dy) #

    # Direction of movement: -1, 0, or +1
    x_step = (cx - x) // distance if cx != x else 0
    y_step = (cy - y) // distance if cy != y else 0

    for i in range(1, distance):
        check_x = x + i * x_step
        check_y = y + i * y_step
        if matrix[check_x][check_y] != "-":
            return False
    return True
    
def parse_coord(coord):#Convert input like 'a2' into matrix indices.
    """Convert input like 'a2' into matrix indices."""
    if len(coord) < 2 or not coord[0].isalpha() or not coord[1:].isdigit():
        return None, None
    x = int(coord[1:])
    y = ord(coord[0].lower()) - ord('a')
    return 8 - x, y  # Matrix indexing (row from top, col from left

def scoring(target_piece,Wscore,Bscore,turn):
    piece_values = {
    "P": 1,  # White Pawn
    "p": 1,  # Black Pawn
    "N": 3,  # White Knight
    "n": 3,  # Black Knight
    "B": 3,  # White Bishop
    "b": 3,  # Black Bishop
    "R": 5,  # White Rook
    "r": 5,  # Black Rook
    "Q": 9,  # White Queen
    "q": 9,}  # Black Queen
    Cscore = piece_values.get(target_piece, 0)
    if turn:
        Wscore += Cscore
    else:
        Bscore += Cscore

    return Wscore,Bscore

def turn_count(Mcount,Tcount):
    Mcount += 1
    if Mcount % 2 == 0:
        Tcount += 1
    return Mcount,Tcount

# === valid selection ===
def select_valid_piece(matrix, turn, black_pieces, white_pieces):
    while True:
        coord = input("Choose piece (e.g. a2): ")
        choose_piece_x, choose_piece_y = parse_coord(coord)

        if choose_piece_x is None or choose_piece_y is None:
            print("Invalid format: a2, e4")
            continue

        elif not (0 <= choose_piece_x < 8 and 0 <= choose_piece_y < 8):
            print("Out of board range. Try again.")
            continue

        piece = matrix[choose_piece_x][choose_piece_y]

        if piece == "-":
            print("This square is empty.")
            continue

        if turn and piece in white_pieces:
            print(f"You have chosen a {white_pieces[piece]}.")
            return choose_piece_x, choose_piece_y

        elif not turn and piece in black_pieces:
            print(f"You have chosen a {black_pieces[piece]}.")
            return choose_piece_x, choose_piece_y

        else:
            print(f"You have chosen an enemy piece ({piece}). Try again.")

def select_move_destination(#check new coord is valid
                        ):
     while True:
        coord = input("Enter move (e.g. a4): ")
        new_piece_x, new_piece_y = parse_coord(coord)

        if new_piece_x is None or new_piece_y is None:
            print("Invalid format. Use coordinates like a2, e4, etc.")
            continue

        if not (0 <= new_piece_x < 8 and 0 <= new_piece_y < 8):
            print("Out of board range. Try again.")
            continue

        return new_piece_x, new_piece_y

# === Piece Actions ===
def piece_captured_move(matrix, cx, cy, x, y, turn, white_pieces, black_pieces):
    moving_piece = matrix[x][y]
    target_piece = matrix[cx][cy]
    captured = target_piece != "-"

    if target_piece != "-":
        captured_name = black_pieces[target_piece] if turn else white_pieces[target_piece]
        print(f"{captured_name} captured successfully.")
    else:
        moved_name = white_pieces[moving_piece] if turn else black_pieces[moving_piece]
        print(f"{moved_name} moved successfully.")

    matrix[cx][cy] = moving_piece
    matrix[x][y] = "-"

    return target_piece, True
        
def en_passant_detection(x, y, cx, cy, matrix):
    if matrix[x][y] not in ("p", "P"):
        return False, None

    if abs(cx - x) == 2:
        en_passant_target = (cx, cy)  # <- the pawn that moved 2 steps
        return True, en_passant_target

    return False, None

def en_passant_capture(x, y, cx, cy, turn, matrix, en_passant_coords):
    dx = abs(cx - x)
    dy = abs(cy - y)

    if en_passant_coords is None:
        return False

    if (
        turn and
        matrix[x][y] == "P" and
        x == 3 and
        dx == 1 and dy == 1 and
        cy == en_passant_coords[1] and
        (
            (y < 7 and matrix[x][y + 1] == "p") or
            (y > 0 and matrix[x][y - 1] == "p")
        )
    ) or (
        not turn and
        matrix[x][y] == "p" and
        x == 3 and
        dx == 1 and dy == 1 and
        cy == en_passant_coords[1] and
        (
            (y < 7 and matrix[x][y + 1] == "P") or
            (y > 0 and matrix[x][y - 1] == "P")
        )
    ):
        matrix[cx][cy] = matrix[x][y]
        matrix[x][y] = "-"
        matrix[en_passant_coords[0]][en_passant_coords[1]] = "-"
        return True

    return False
        





    
    
    
