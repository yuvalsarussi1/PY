from utils import *

def Total_Movement(
                new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces,turn,black_score,white_score,piece_values):
    
    
    piece = matrix[choose_piece_x][choose_piece_y]
    path_clear  = False
    
    # ========== PICK NONE SLIDING PIECES  ==========
    if piece in ("P", "p"):
        if pawn_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y,turn):
            path_clear  = True
    elif piece in ("N", "n"):
        if knight_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):
            path_clear  = True
    elif piece in ("K", "k"):
        if king_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):
            path_clear  = True


    # ========== PICK SLIDING PIECES  ==========        
    elif piece in ("R", "r"):
       if(
        rook_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y) and
        clear_path(matrix, choose_piece_x, choose_piece_y, new_piece_x, new_piece_y)):
                path_clear  = True
    elif piece in ("B", "b"):
       if( 
        bishop_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y) and 
        clear_path(matrix, choose_piece_x, choose_piece_y, new_piece_x, new_piece_y)):
            path_clear  = True
    elif piece in ("Q", "q"):
        if(
        queen_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y) and 
        clear_path(matrix, choose_piece_x, choose_piece_y, new_piece_x, new_piece_y)):
            path_clear  = True


    # ========== PREFORMING MOVEMENT  ==========#
    if path_clear and not is_same_side(matrix, choose_piece_x, choose_piece_y, new_piece_x, new_piece_y,white_pieces, black_pieces):
            
            black_score, white_score = piece_captured_move(matrix, new_piece_x, new_piece_y, choose_piece_x, choose_piece_y,turn, white_pieces, black_pieces, white_score, black_score, piece_values)
            
            return True,black_score,white_score
    
    return False,black_score,white_score