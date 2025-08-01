

# === Coordinate & Board Helpers ===
def is_empty(#true if the new position is empty
        matrix,new_piece_x, new_piece_y): 
    return matrix[new_piece_x][new_piece_y] == "-"
   
def is_enemy(#true if the new position is occupied by an enemy piece
        matrix, choose_piece_x, choose_piece_y, new_piece_x, new_piece_y, white_pieces, black_pieces):
    return (
        (matrix[new_piece_x][new_piece_y] in white_pieces and matrix[choose_piece_x][choose_piece_y] in black_pieces) or
        (matrix[new_piece_x][new_piece_y] in black_pieces and matrix[choose_piece_x][choose_piece_y] in white_pieces)
    )

def is_same_side(#true if the new position is occupied by a friendly piece
        matrix, choose_piece_x, choose_piece_y, new_piece_x, new_piece_y,white_pieces, black_pieces): 
    return (
        (matrix[new_piece_x][new_piece_y] in white_pieces and matrix[choose_piece_x][choose_piece_y] in white_pieces) or
        (matrix[new_piece_x][new_piece_y] in black_pieces and matrix[choose_piece_x][choose_piece_y] in black_pieces)
    )

def clear_path(#true if the path is clear for sliding pieces
        matrix, choose_piece_x, choose_piece_y, new_piece_x, new_piece_y): 
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    distance = max(dx, dy) #

    # Direction of movement: -1, 0, or +1
    x_step = (new_piece_x - choose_piece_x) // distance if new_piece_x != choose_piece_x else 0
    y_step = (new_piece_y - choose_piece_y) // distance if new_piece_y != choose_piece_y else 0

    for i in range(1, distance):
        check_x = choose_piece_x + i * x_step
        check_y = choose_piece_y + i * y_step
        if matrix[check_x][check_y] != "-":
            return False
    return True
    
def parse_coord(#Convert input like 'a2' into matrix indices.
            coord):
    """Convert input like 'a2' into matrix indices."""
    if len(coord) < 2 or not coord[0].isalpha() or not coord[1:].isdigit():
        return None, None
    x = int(coord[1:])
    y = ord(coord[0].lower()) - ord('a')
    return 8 - x, y  # Matrix indexing (row from top, col from left

# === valid selection ===
def get_valid_piece_selection(#check coord is valid and choose the piece
                        matrix, turn, black_pieces, white_pieces,choose_piece):
    while True:
        coord = input("Choose piece (e.g. a2): ")
        choose_piece_x, choose_piece_y = parse_coord(coord)

        if choose_piece_x is None or choose_piece_y is None:
            print("Invalid format. Use coordinates like a2, e4, etc.")
            continue

        if not (0 <= choose_piece_x < 8 and 0 <= choose_piece_y < 8):
            print("Out of board range. Try again.")
            continue

        if choose_piece(choose_piece_x, choose_piece_y, matrix, turn, black_pieces, white_pieces):
            return choose_piece_x, choose_piece_y
        else:
            print("Invalid selection. Try again.")

def get_valid_piece_move(#check new coord is valid
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

def choose_piece(#true if the piece is valid
        choose_piece_x, choose_piece_y, matrix, turn, black_pieces, white_pieces):
    
    piece = matrix[choose_piece_x][choose_piece_y]

    if piece == "-":
        print("This square is empty.")
        return False

    if turn and piece in white_pieces:
        print(f"You have chosen a {white_pieces[piece]}.")
        return True
    
    elif not turn and piece in black_pieces:
        print(f"You have chosen a {black_pieces[piece]}.")
        return True
     
    else:
        print(f"You have chosen an enemy piece ({piece}).")
        return False

# === Piece Selection Conditions ===
def pawn_Movement_condition(#true if the move is valid
        new_piece_x, new_piece_y, choose_piece_x, choose_piece_y,turn): #true if the move is valid 
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    if dx == 1 and dy == 1:
        if turn and new_piece_x < choose_piece_x:  # white pawn (moves down)
            return True
        elif not turn and new_piece_x > choose_piece_x:  # black pawn (moves up)
            return True
        
    if dx == 1 and dy == 0:
        if turn and new_piece_x < choose_piece_x:
            return True
        elif not turn and new_piece_x > choose_piece_x:
            return True
        
    if dx == 2 and dy == 0:
        if turn and choose_piece_x == 6 and new_piece_x == 4:  # white pawn from row 6 to 4
            return True
        elif not turn and choose_piece_x == 1 and new_piece_x == 3:  # black pawn from row 1 to 3
            return True

def knight_Movement_condition(#true if the move is valid
        new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):#true if the move is valid
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    return ((dx == 2 and dy == 1) or (dx == 1 and dy == 2))
   
def bishop_Movement_condition(#true if the move is valid
        new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):#true if the move is valid
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    return dx == dy

def rook_Movement_condition(#true if the move is valid
        new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):#true if the move is valid
    return new_piece_x == choose_piece_x or new_piece_y == choose_piece_y

def queen_Movement_condition(#true if the move is valid
    new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):#true if the move is valid
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    return (dx == dy or new_piece_x == choose_piece_x or new_piece_y == choose_piece_y)

def king_Movement_condition(#true if the move is valid
        new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):#true if the move is valid
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    return max(dx, dy) == 1


# === Piece Actions ===
def piece_captured_move(#move the piece and capture the enemy piece
matrix, new_piece_x, new_piece_y, choose_piece_x, choose_piece_y,turn,white_pieces, black_pieces, white_score, black_score,piece_values): #move the piece and capture the enemy piece
    moving_piece = matrix[choose_piece_x][choose_piece_y] #choosen piece 
    target_piece = matrix[new_piece_x][new_piece_y]       #where moving piece is going
    captured = target_piece != "-"
    
    if captured:
        captured_name = black_pieces[target_piece] if turn else white_pieces[target_piece] #captured piece name
        print(f"{captured_name} captured successfully.") 
        score = piece_values.get(target_piece, 0)
        if turn:
            white_score += score
        else:
            black_score += score
    else:
        moved_name = white_pieces[moving_piece] if turn else black_pieces[moving_piece] #moving piece name
        print(f"{moved_name} moved successfully.")
    print(f"White score: {white_score} | Black score: {black_score}")
    matrix[new_piece_x][new_piece_y] = matrix[choose_piece_x][choose_piece_y] #moving piece to new position
    matrix[choose_piece_x][choose_piece_y] = "-" #clearing old position

    return black_score, white_score

    
    
    
     
    
    
    
