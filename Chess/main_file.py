# from Chess_pieces import pawn_Movement, knight_Movement, king_Movement
from board import setup_board, print_board
from utils import *
from pieces_conditions import *
from valid_move import is_valid_move
from check_targets import *
import copy
# Define piece values



def main():
    turn = True
    Wscore = 0
    Bscore = 0
    target_piece = "-"
    move_successful = False
    Tcount = 0
    Mcount = 0
    en_passant_condition = False
    en_passant_coords = None
    
    # Set up the board and print it
    matrix, black_pieces, white_pieces = setup_board()
    print_board(matrix)
    print(f"Moves:{Mcount}|Turns:{Tcount}")
    print(f"W:{Wscore}|B:{Bscore}")
    
    
    while True:
        board_copy = copy.deepcopy(matrix)
        print("White turn" if turn else "Black turn")#print whose turn
        
        target_piece = "-"
        move_successful = False

        #============== Piece selection and move ================
        x, y = select_valid_piece(matrix, turn, black_pieces, white_pieces)# Get valid piece selection
        cx, cy = select_move_destination()# Get valid piece move and move
        #========================================================
    
        #============== En Passant Detection ==============
        next_en_passant_condition, next_en_passant_coords = en_passant_detection(x,y,cx,cy,turn,matrix)        
        if next_en_passant_condition:
            en_passant_condition = next_en_passant_condition
            en_passant_coords = next_en_passant_coords
        #==================================================

        #============== Valid move ================
        valid_move = is_valid_move(cx, cy, x, y, matrix,turn)
        not_empty = is_enemy_or_empty(matrix, x, y, cx, cy,white_pieces, black_pieces)
        if valid_move and not_empty:
            target_piece, move_successful = piece_captured_move(matrix, cx, cy, x, y,turn, white_pieces, black_pieces)
        #==========================================


        #============== En Passant ==============
        if not move_successful and en_passant_condition:
            move_successful = en_passant_capture(x,y,cx,cy,turn,matrix,en_passant_coords)
            if move_successful:
                target_piece = "p" if turn else "P"
        #==========================================
        
        
        # Switch turns
        if move_successful:
        # check king safety on the UPDATED matrix
            threatens = board_threat_check(matrix)
            check_white, check_black = king_in_check(matrix, threatens, black_pieces, white_pieces)

            if (turn and check_white) or (not turn and check_black):
                matrix = board_copy
                print_board(matrix)
                print("still in check")
                continue  # no side-effects happen

            # commit side-effects ONLY now (move is legal)
            en_passant_condition = next_en_passant_condition
            en_passant_coords    = next_en_passant_coords
            Wscore, Bscore       = scoring(target_piece, Wscore, Bscore, turn)
            Mcount, Tcount       = turn_count(Mcount, Tcount)

            # finally switch turns
            turn = not turn
            print_board(matrix)
        else:
            print("Invalid move. Try again.")
            en_passant_condition = False
            en_passant_coords    = None

# Run the game
if __name__ == "__main__":
    main()

