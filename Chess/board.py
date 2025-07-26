def setup_board():
    matrix = [["-" for _ in range(8)] for _ in range(8)]
    matrix[6] = ["p"] * 8
    matrix[1] = ["P"] * 8

    matrix[7] = ["r", "n", "b", "q", "k", "b", "n", "r"]
    matrix[0] = ["R", "N", "B", "Q", "K", "B", "N", "R"]

    friendly_pieces = ["p", "r", "n", "b", "q", "k"]
    return matrix, friendly_pieces

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

