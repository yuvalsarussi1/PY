from pieces_conditions import *
from utils import clear_path
movement_rules = {
    "P": lambda x, y, cx, cy, turn, matrix: pawn_Movement_condition(x, y, cx, cy, turn, matrix),
    "p": lambda x, y, cx, cy, turn, matrix: pawn_Movement_condition(x, y, cx, cy, turn, matrix),
    "N": lambda x, y, cx, cy, turn, matrix: knight_Movement_condition(x, y, cx, cy),
    "n": lambda x, y, cx, cy, turn, matrix: knight_Movement_condition(x, y, cx, cy),
    "K": lambda x, y, cx, cy, turn, matrix: king_Movement_condition(x, y, cx, cy),
    "k": lambda x, y, cx, cy, turn, matrix: king_Movement_condition(x, y, cx, cy),
    "R": lambda x, y, cx, cy, turn, matrix: rook_Movement_condition(x, y, cx, cy) and clear_path(matrix, x, y, cx, cy),
    "r": lambda x, y, cx, cy, turn, matrix: rook_Movement_condition(x, y, cx, cy) and clear_path(matrix, x, y, cx, cy),
    "B": lambda x, y, cx, cy, turn, matrix: bishop_Movement_condition(x, y, cx, cy) and clear_path(matrix, x, y, cx, cy),
    "b": lambda x, y, cx, cy, turn, matrix: bishop_Movement_condition(x, y, cx, cy) and clear_path(matrix, x, y, cx, cy),
    "Q": lambda x, y, cx, cy, turn, matrix: queen_Movement_condition(x, y, cx, cy) and clear_path(matrix, x, y, cx, cy),
    "q": lambda x, y, cx, cy, turn, matrix: queen_Movement_condition(x, y, cx, cy) and clear_path(matrix, x, y, cx, cy),
}

def is_valid_move(cx, cy, x, y, matrix, turn):
    piece = matrix[x][y]  # ← the piece you're moving (from current position)
    if piece in movement_rules:
        return movement_rules[piece](x, y, cx, cy, turn, matrix)
    return False


