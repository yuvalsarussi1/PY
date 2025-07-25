def pawn_Movement(new_piece_x, new_piece_y,choose_piece_x,choose_piece_y,matrix):
            if new_piece_x == choose_piece_x - 1 and new_piece_y == choose_piece_y:
                matrix[new_piece_x][new_piece_y] = 1
                matrix[choose_piece_x][choose_piece_y] = 0
                print("Pawn moved successfully.")
            elif new_piece_x == choose_piece_x - 1 and abs(new_piece_y - choose_piece_y) == 1:
                    if matrix[new_piece_x][new_piece_y] != 0:
                        matrix[new_piece_x][new_piece_y] = 1
                        matrix[choose_piece_x][choose_piece_y] = 0
                        print("Pawn captured successfully.")
                    else:
                        print("No piece to capture.")
            else:
                print("Invalid move. A pawn can only move one square forward.")

def knight_Movement(new_piece_x, new_piece_y,dx,dy,choose_piece_x,choose_piece_y,matrix):
    if 0 <= new_piece_x < 8 and 0 <= new_piece_y < 8:     
        dx = abs(new_piece_x - choose_piece_x)# abs stgands for absolute value of a number 
        dy = abs(new_piece_y - choose_piece_y)
        if dx == 2 and dy == 1 or dx == 1 and dy == 2:
            if matrix[new_piece_x][new_piece_y] !=0:
                print("Knight captured successfully.") 
            else:
                print("Knight moved successfully.")
            matrix[new_piece_x][new_piece_y] = 3
            matrix[choose_piece_x][choose_piece_y] = 0
        else:
            print("Invalid knight move.")
    else:
        print("Move out of bounds.")

def king_Movement(new_piece_x, new_piece_y,choose_piece_x,choose_piece_y,matrix,dx,dy):
    if 0 <= new_piece_x < 8 and 0 <= new_piece_y < 8:    
        dx = abs(new_piece_x - choose_piece_x)
        dy = abs(new_piece_y - choose_piece_y)
        if max(dx, dy) == 1:#largest value among the inputs
            if matrix[new_piece_x][new_piece_y] !=0:
                print("King captured successfully.") 
            else:
                print("King moved successfully.")
            matrix[new_piece_x][new_piece_y] = 9
            matrix[choose_piece_x][choose_piece_y] = 0
        else:
            print("Invalid  King move.")
    else:
        print("Move out of bounds.")

