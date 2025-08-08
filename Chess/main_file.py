# from Chess_pieces import pawn_Movement, knight_Movement, king_Movement
from board import setup_board, print_board
from utils import *
from pieces_conditions import *
from valid_move import is_valid_move


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
        print("White turn" if turn else "Black turn")#print whose turn
        
        x, y = select_valid_piece(matrix, turn, black_pieces, white_pieces)# Get valid piece selection
        cx, cy = select_move_destination()# Get valid piece move and move
        
        target_piece = "-"
        move_successful = False

        next_en_passant_condition, next_en_passant_coords = en_passant_detection(x,y,cx,cy,turn,matrix)
        
        valid_move = is_valid_move(cx, cy, x, y, matrix,turn)
        not_empty = is_enemy_or_empty(matrix, x, y, cx, cy,white_pieces, black_pieces)
        if valid_move and not_empty:
            target_piece, move_successful = piece_captured_move(matrix, cx, cy, x, y,turn, white_pieces, black_pieces)
            Mcount,Tcount = turn_count(Mcount,Tcount)
        

        #============== En Passant ==============
        if not move_successful and en_passant_condition:
            move_successful = en_passant_capture(x,y,cx,cy,turn,matrix,en_passant_coords)
            if move_successful:
                target_piece = "p" if turn else "P"
                Mcount,Tcount = turn_count(Mcount,Tcount)
        #==========================================
        
        #==============Update en passant condition ==============
        if move_successful:
            en_passant_condition = next_en_passant_condition
            en_passant_coords = next_en_passant_coords
        else:
            en_passant_condition = False
            en_passant_coords = None
        #==========================================

        Wscore,Bscore = scoring(target_piece,Wscore,Bscore,turn)
        
        print_board(matrix)#print board
        print(f"Moves:{Mcount}|Turns:{Tcount}")
        print(f"W:{Wscore}|B:{Bscore}")


        # Switch turns
        if move_successful:
            turn = not turn
        else:
            print("Invalid move. Try again.")

# Run the game
if __name__ == "__main__":
    main()

