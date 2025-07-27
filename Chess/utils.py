def is_empty(matrix,new_piece_x, new_piece_y): #true if the new position is empty
    return matrix[new_piece_x][new_piece_y] == "-"
   
def is_enemy(matrix, choose_piece_x, choose_piece_y, new_piece_x, new_piece_y, white_pieces, black_pieces): #true if the new position is occupied by an enemy piece
    return (
        (matrix[new_piece_x][new_piece_y] in white_pieces and matrix[choose_piece_x][choose_piece_y] in black_pieces) or
        (matrix[new_piece_x][new_piece_y] in black_pieces and matrix[choose_piece_x][choose_piece_y] in white_pieces)
    )

def is_same_side(matrix, choose_piece_x, choose_piece_y, new_piece_x, new_piece_y,white_pieces, black_pieces): #true if the new position is occupied by a friendly piece
    return (
        (matrix[new_piece_x][new_piece_y] in white_pieces and matrix[choose_piece_x][choose_piece_y] in white_pieces) or
        (matrix[new_piece_x][new_piece_y] in black_pieces and matrix[choose_piece_x][choose_piece_y] in black_pieces)
    )

def piece_captured_move(matrix, new_piece_x, new_piece_y, choose_piece_x, choose_piece_y,turn,white_pieces, black_pieces): #move the piece and capture the enemy piece
    moving_piece = matrix[choose_piece_x][choose_piece_y] #choosen piece 
    target_piece = matrix[new_piece_x][new_piece_y]       #where moving piece is going

    captured = target_piece != "-"
    
    if captured:
        captured_name = black_pieces[target_piece] if turn else white_pieces[target_piece] #captured piece name
        print(f"{captured_name} captured successfully.") 
    else:
        moved_name = white_pieces[moving_piece] if turn else black_pieces[moving_piece] #moving piece name
        print(f"{moved_name} moved successfully.")

    matrix[new_piece_x][new_piece_y] = matrix[choose_piece_x][choose_piece_y] #moving piece to new position
    matrix[choose_piece_x][choose_piece_y] = "-" #clearing old position

def clear_path(matrix, choose_piece_x, choose_piece_y, new_piece_x, new_piece_y): #true if the path is clear for sliding pieces
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
            print("Invalid move: piece in the way")
            return False
    return True


def pawn_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y): #true if the move is valid 
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    if dx == 1 and dy == 1:
        return True
    elif dx == 1 and dy == 0:
        return True
    
def knight_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):#true if the move is valid
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    return ((dx == 2 and dy == 1) or (dx == 1 and dy == 2))
   
def bishop_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):#true if the move is valid
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    return dx == dy

def rook_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):#true if the move is valid
    return new_piece_x == choose_piece_x or new_piece_y == choose_piece_y

def queen_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):#true if the move is valid
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    return (dx == dy or new_piece_x == choose_piece_x or new_piece_y == choose_piece_y)

def king_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):#true if the move is valid
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    return max(dx, dy) == 1