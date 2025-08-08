# === Piece Selection Conditions ===
def pawn_Movement_condition(x, y, cx, cy, turn, matrix):
    dx = abs(cx - x)
    dy = abs(cy - y)

    # Diagonal capture
    if dx == 1 and dy == 1:
        if turn and x > cx and matrix[cx][cy] != "-":
            return True
        elif not turn and x < cx and matrix[cx][cy] != "-":
            return True
        
    # Single forward move
    if dx == 1 and dy == 0:
        if turn and x > cx and matrix[cx][cy] == "-":  # white forward
            return True
        elif not turn and x < cx and matrix[cx][cy] == "-":  # black forward
            return True

    # Double forward move from starting row
    if dx == 2 and dy == 0:
        if turn and x == 6 and cx == 4 and matrix[5][cy] == "-" and matrix[4][cy] == "-":  # white
            return True
        elif not turn and x == 1 and cx == 3 and matrix[2][cy] == "-" and matrix[3][cy] == "-":  # black
            return True

    return False
        
def knight_Movement_condition(cx, cy, x, y):#true if the move is valid
    dx = abs(cx - x)
    dy = abs(cy - y)
    return ((dx == 2 and dy == 1) or (dx == 1 and dy == 2))
   
def bishop_Movement_condition(cx, cy, x, y):#true if the move is valid
    dx = abs(cx - x)
    dy = abs(cy - y)
    return dx == dy

def rook_Movement_condition(cx, cy, x, y):#true if the move is valid
    return cx == x or cy == y

def queen_Movement_condition(cx, cy, x, y):#true if the move is valid
    dx = abs(cx - x)
    dy = abs(cy - y)
    return (dx == dy or cx == x or cy == y)

def king_Movement_condition(cx, cy, x, y):#true if the move is valid
    dx = abs(cx - x)
    dy = abs(cy - y)
    return max(dx, dy) == 1