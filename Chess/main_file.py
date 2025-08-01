# from Chess_pieces import pawn_Movement, knight_Movement, king_Movement
from board import setup_board, print_board
from utils import *
from pieces import Total_Movement


# Define piece values
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
    "q": 9,  # Black Queen
    # "K": float('inf'),  # White King (invaluable)
    # "k": float('inf')   # Black King
}


def main():
    # Set up the board and print it
    matrix, black_pieces, white_pieces = setup_board()
    print_board(matrix)
    
    #True for white's turn, False for black
    turn = True
    # Initialize scores
    white_score = 0
    black_score = 0

    # Game loop
    while True:
        print("White turn" if turn else "Black turn")#print whose turn
        
        #input choose_piece
        choose_piece_x, choose_piece_y = get_valid_piece_selection(matrix, turn, black_pieces, white_pieces, choose_piece)# Get valid piece selection
        #input new_piece
        new_piece_x, new_piece_y = get_valid_piece_move()# Get valid piece move and move
        #check if move is valid and make it
        move, black_score, white_score = Total_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces, turn, black_score, white_score, piece_values)
        
        print_board(matrix)#print board
        
        # Switch turns
        if move:
            turn = not turn
        else:
            print("Invalid move. Try again.")

# Run the game
if __name__ == "__main__":
    main()

