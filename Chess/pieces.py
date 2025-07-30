from board import setup_board
from utils import *


# def knight_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces):
#     dx = abs(new_piece_x - choose_piece_x)# abs stgands
#     dy = abs(new_piece_y - choose_piece_y)
#     if ((dx == 2 and dy == 1) or (dx == 1 and dy == 2)) and (
#     matrix[new_piece_x][new_piece_y] == "-" or
#     (matrix[new_piece_x][new_piece_y] in white_pieces and matrix[choose_piece_x][choose_piece_y] in black_pieces) or
#     (matrix[new_piece_x][new_piece_y] in black_pieces and matrix[choose_piece_x][choose_piece_y] in white_pieces)
# ):
#         if matrix[new_piece_x][new_piece_y] != "-":
#             print("Knight captured successfully.") 
#         else:
#             print("Knight moved successfully.")
#         matrix[new_piece_x][new_piece_y] = matrix[choose_piece_x][choose_piece_y]
#         matrix[choose_piece_x][choose_piece_y] = "-"
#     else:
#         print("Invalid knight move.")

# def Pawn_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces):
#     dx = abs(new_piece_x - choose_piece_x)
#     dy = abs(new_piece_y - choose_piece_y)
#     path_clear = True
#     if dx == 1 and dy == 0 and new_piece_x < choose_piece_x and matrix[new_piece_x][new_piece_y] == "-":
#         print("Pawn moved successfully.")
#     elif dx == 1 and dy == 1 and new_piece_x < choose_piece_x and matrix[new_piece_x][new_piece_y] != "-" and matrix[new_piece_x][new_piece_y] not in white_pieces: 
#         print("Pawn captured successfully.")
#     elif (
#         dx == 2 and
#         dy == 0 and
#         choose_piece_x == 6 and
#         new_piece_x == 4 and 
#         new_piece_x < choose_piece_x and
#         matrix[new_piece_x][new_piece_y] == "-" and
#         matrix[new_piece_x][new_piece_y] not in white_pieces and
#         matrix[choose_piece_x - 1][choose_piece_y] not in white_pieces and
#         matrix[choose_piece_x][choose_piece_y] == "P"
#         ):

#         print("Pawn moved successfully.")
#     else:
#         print("Invalid pawn move.")
#         path_clear = False
    
#     if path_clear:
#         matrix[new_piece_x][new_piece_y] = matrix[choose_piece_x][choose_piece_y]
#         matrix[choose_piece_x][choose_piece_y] = "-"

# def king_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces):
#     dx = abs(new_piece_x - choose_piece_x)
#     dy = abs(new_piece_y - choose_piece_y)
#     if max(dx, dy) == 1 and matrix[new_piece_x][new_piece_y] not in white_pieces:
#         if matrix[new_piece_x][new_piece_y] !="-":
#             print("King captured successfully.") 
#         else:
#             print("King moved successfully.")


#         matrix[new_piece_x][new_piece_y] = matrix[choose_piece_x][choose_piece_y]
#         matrix[choose_piece_x][choose_piece_y] = "-"
#     else:
#         print("Invalid king move.")

# def Rook_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces):
# #check if there is a piece in the way
#     if new_piece_x == choose_piece_x or new_piece_y == choose_piece_y and matrix[new_piece_x][new_piece_y] not in white_pieces:
#         distance = max(abs(new_piece_x - choose_piece_x), abs(new_piece_y - choose_piece_y))
#         path_clear  = True
#         # Direction of movement: -1, 0, or +1
#         x_step = (new_piece_x - choose_piece_x) // distance if new_piece_x != choose_piece_x else 0
#         y_step = (new_piece_y - choose_piece_y) // distance if new_piece_y != choose_piece_y else 0

#         for i in range(1, distance):
#             check_x = choose_piece_x + i * x_step
#             check_y = choose_piece_y + i * y_step
#             if matrix[check_x][check_y] != "-":
#                 print("Invalid move: piece in the way")
#                 path_clear  = False
#                 break
#         if path_clear :
#             if matrix[new_piece_x][new_piece_y] != "-" :
#                 print("Rook captured successfully.") 
#             else:
#                 print("Rook moved successfully.")
#             matrix[new_piece_x][new_piece_y] = matrix[choose_piece_x][choose_piece_y]
#             matrix[choose_piece_x][choose_piece_y] = "-"       
                
#     else:
#         print("Invalid move: rook can only move in straight lines")

# def bishop_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces):
#     dx = abs(new_piece_x - choose_piece_x)
#     dy = abs(new_piece_y - choose_piece_y)
#     path_clear  = True
#     if dx == dy and matrix[new_piece_x][new_piece_y] not in white_pieces:
#         distance = dx #or dy. no need for max(dx, dy)
#         x_step = (new_piece_x - choose_piece_x) // distance if new_piece_x != choose_piece_x else 0
#         y_step = (new_piece_y - choose_piece_y) // distance if new_piece_y != choose_piece_y else 0
        
#         for i in range(1, distance):
#             check_x = choose_piece_x + i * x_step
#             check_y = choose_piece_y + i * y_step
#             if matrix[check_x][check_y] != "-":
#                 print("Invalid move: piece in the way")
#                 path_clear  = False
#                 break
#         if path_clear :
#             if matrix[new_piece_x][new_piece_y] != "-":
#                 print("bishop captured successfully.") 
#             else:
#                 print("bishop moved successfully.")
#             matrix[new_piece_x][new_piece_y] = matrix[choose_piece_x][choose_piece_y]
#             matrix[choose_piece_x][choose_piece_y] = "-"
                             
#     else:
#         print("Invalid move:bishop can only move in diagonal  lines")      

# def Queen_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces):
#     dx = abs(new_piece_x - choose_piece_x)
#     dy = abs(new_piece_y - choose_piece_y)
#     path_clear  = True
#     if (dx == dy or new_piece_x == choose_piece_x or new_piece_y == choose_piece_y) and matrix[new_piece_x][new_piece_y] not in white_pieces:
#         distance = max(dx, dy)
#         x_step = (new_piece_x - choose_piece_x) // distance if new_piece_x != choose_piece_x else 0
#         y_step = (new_piece_y - choose_piece_y) // distance if new_piece_y != choose_piece_y else 0
        
#         for i in range(1, distance):
#             check_x = choose_piece_x + i * x_step
#             check_y = choose_piece_y + i * y_step
#             if matrix[check_x][check_y] != "-":
#                 print("Invalid move: piece in the way")
#                 path_clear  = False
#                 break
#         if path_clear :
#             if matrix[new_piece_x][new_piece_y] != "-":
#                 print("Queen captured successfully.") 
#             else:
#                 print("Queen moved successfully.")
#             matrix[new_piece_x][new_piece_y] = matrix[choose_piece_x][choose_piece_y]
#             matrix[choose_piece_x][choose_piece_y] = "-"
                             
#     else:
#         print("Invalid move:Queen")    

# def castling(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces):
#     from_p = matrix[choose_piece_x][choose_piece_y]
#     to_p = matrix[new_piece_x][new_piece_y]
#     path_clear  = True

#     if (from_p in ("k", "r")) and (to_p in ("k", "r")) and (from_p != to_p):
#         dx = abs(new_piece_x - choose_piece_x)
#         x_step = (new_piece_x - choose_piece_x) // dx if new_piece_x != choose_piece_x else 0
#         for i in range(1, dx):
#                 check_x = choose_piece_x + i * x_step
#                 if matrix[check_x][choose_piece_y] != "-":
#                     print("Invalid move: piece in the way")
#                     path_clear  = False
#                     break
#                 if path_clear :
#                         if from_p == "k" and to_p == "r" and to_p == matrix[7][7]:
#                             matrix[choose_piece_x + 2][choose_piece_y] == "k"
#                             matrix[choose_piece_x][choose_piece_y] == "-" 
#                             matrix[choose_piece_x + 2][choose_piece_y] == "k" 
#                             matrix[new_piece_x-2][new_piece_y] == "r"
#                             matrix[new_piece_x][new_piece_y] == "-"
                        
                           
#                         elif to_p == "k" and from_p == "r":
#                             print("y is 1")
                        
                    
        
    



def choose_piece(choose_piece_x, choose_piece_y, matrix, turn, black_pieces, white_pieces):
    piece = matrix[choose_piece_x][choose_piece_y]

    if piece == "-":
        print("This square is empty.")
        return False

    if turn and piece in white_pieces:
        print(f"You have chosen a {white_pieces[piece]}.")
        return True
    elif not turn and piece in black_pieces:
        print(f"You have chosen a {black_pieces[piece]}.")
        return True
    else:
        print(f"You have chosen an enemy piece ({piece}).")
        return False





def Total_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces,turn):
    piece = matrix[choose_piece_x][choose_piece_y]
    path_clear  = False
    if piece in ("P", "p"):
        if pawn_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y,turn):
            path_clear  = True
    elif piece in ("N", "n"):
        if knight_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):
            path_clear  = True
    elif piece in ("K", "k"):
        if king_Movement_condition(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y):
            path_clear  = True
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
    
    if path_clear:
        if(
        not is_same_side(matrix, choose_piece_x, choose_piece_y, new_piece_x, new_piece_y,white_pieces, black_pieces)
        or  is_empty(matrix, new_piece_x, new_piece_y)):
            piece_captured_move(matrix, new_piece_x, new_piece_y, choose_piece_x, choose_piece_y,turn,white_pieces, black_pieces)
            
            return True
    
    
        
        
    # else:
    #     print("Invalid move")
    #     return False
    
    





# def Total_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces):
#     piece = matrix[choose_piece_x][choose_piece_y]

#     if piece in ("P", "p"):
#         Pawn_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces)
#     elif piece in ("N", "n"):
#         knight_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces)
#     elif piece in ("K", "k"):
#         king_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces)
#     elif piece in ("R", "r"):
#         Rook_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces)
#     elif piece in ("B", "b"):
#         bishop_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces)
#     elif piece in ("Q", "q"):
#         Queen_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, white_pieces, black_pieces)