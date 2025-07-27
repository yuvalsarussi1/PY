def setup_board():
    matrix = [["-" for _ in range(8)] for _ in range(8)]
    matrix[1] = ["p"] * 8
    matrix[6] = ["P"] * 8

    matrix[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]
    matrix[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]

    black_pieces = {
    "p": "Black Pawn",
    "n": "Black Knight",
    "b": "Black Bishop",
    "r": "Black Rook",
    "q": "Black Queen",
    "k": "Black King"
    }

    white_pieces = {
    "P": "White Pawn",
    "N": "White Knight",
    "B": "White Bishop",
    "R": "White Rook",
    "Q": "White Queen",
    "K": "White King"
    }

    return matrix, black_pieces , white_pieces

def print_board(matrix):
    print("======================")
    for row_index in range(8):
        print("|", 8 - row_index, "", end=" ")
        for col_index in range(8):
            print(matrix[row_index][col_index], end=" ")
        print("|")
    print("|                    |")
    print("|   ", "a", "b", "c", "d", "e", "f", "g", "h", "|")
    print("======================")

