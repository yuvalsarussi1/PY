# from Chess_pieces import pawn_Movement, knight_Movement, king_Movement
from board import setup_board, print_board
from pieces import *



def parse_coord(coord):
    """Convert input like 'a2' into matrix indices."""
    if len(coord) < 2 or not coord[0].isalpha() or not coord[1:].isdigit():
        return None, None
    x = int(coord[1:])
    y = ord(coord[0].lower()) - ord('a')
    return 8 - x, y  # Matrix indexing (row from top, col from left

def main():
    
    matrix, black_pieces, white_pieces = setup_board()
    print_board(matrix)
    turn = True  # True for white's turn, False for black

    while True:

        print("White turn" if turn else "Black turn")
        while True:
                coord = input("Choose piece (e.g. a2): ")
                choose_piece_x, choose_piece_y = parse_coord(coord)

                if not (0 <= choose_piece_x < 8 and 0 <= choose_piece_y < 8):
                    print("Invalid input. Try again.")
                    continue

                if choose_piece(choose_piece_x, choose_piece_y, matrix, turn, black_pieces, white_pieces):
                    break  # valid selection, exit inner loop
                else:
                    print("Invalid selection. Try again.")

        coord = input("Enter move (e.g. a2): ")
        new_piece_x, new_piece_y = parse_coord(coord)
        if not (0 <= new_piece_x < 8 and 0 <= new_piece_y < 8):
            print("Invalid move. Try again.")
            continue

        Total_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces)
        print_board(matrix)
        
        turn = not turn  # Switch turns

if __name__ == "__main__":
    main()

    # print("======================")
    # for row_index in range(8):
    #     print("|",8 - row_index,"" ,end=" ")  # Print row label (8 to 1)
    #     for col_index in range(8):
    #         print(matrix[row_index][col_index], end=" ")
    #     print("|")
    # print("|                    |")
    # print("|  "," a", "b" , "c", "d", "e", "f", "g", "h", "|")
    # print("======================")

