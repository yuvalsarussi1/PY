



def knight_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces):
    dx = abs(new_piece_x - choose_piece_x)# abs stgands
    dy = abs(new_piece_y - choose_piece_y)
    if ((dx == 2 and dy == 1) or (dx == 1 and dy == 2)) and matrix[new_piece_x][new_piece_y] not in friendly_pieces:
        if matrix[new_piece_x][new_piece_y] !="-":
            print("Knight captured successfully.") 
        else:
            print("Knight moved successfully.")
        matrix[new_piece_x][new_piece_y] = "n"
        matrix[choose_piece_x][choose_piece_y] = "-"
    else:
        print("Invalid knight move.")

def Pawn_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces):
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    path_clear = True
    if dx == 1 and dy == 0 and new_piece_x < choose_piece_x and matrix[new_piece_x][new_piece_y] == "-":
        print("Pawn moved successfully.")
    elif dx == 1 and dy == 1 and new_piece_x < choose_piece_x and matrix[new_piece_x][new_piece_y] != "-" and matrix[new_piece_x][new_piece_y] not in friendly_pieces: 
        print("Pawn captured successfully.")
    elif (
        dx == 2 and
        dy == 0 and
        choose_piece_x == 6 and
        new_piece_x == 4 and 
        new_piece_x < choose_piece_x and
        matrix[new_piece_x][new_piece_y] == "-" and
        matrix[new_piece_x][new_piece_y] not in friendly_pieces and
        matrix[choose_piece_x - 1][choose_piece_y] not in friendly_pieces and
        matrix[choose_piece_x][choose_piece_y] == "p"
        ):

        print("Pawn moved successfully.")
    else:
        print("Invalid pawn move.")
        path_clear = False
    
    if path_clear:
        matrix[new_piece_x][new_piece_y] = "p"
        matrix[choose_piece_x][choose_piece_y] = "-"

def king_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces):
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    if max(dx, dy) == 1 and matrix[new_piece_x][new_piece_y] not in friendly_pieces:
        if matrix[new_piece_x][new_piece_y] !="-":
            print("King captured successfully.") 
        else:
            print("King moved successfully.")


        matrix[new_piece_x][new_piece_y] = "k"
        matrix[choose_piece_x][choose_piece_y] = "-"
    else:
        print("Invalid king move.")

def Rook_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces):
#check if there is a piece in the way
    if new_piece_x == choose_piece_x or new_piece_y == choose_piece_y and matrix[new_piece_x][new_piece_y] not in friendly_pieces:
        distance = max(abs(new_piece_x - choose_piece_x), abs(new_piece_y - choose_piece_y))
        path_clear  = True
        # Direction of movement: -1, 0, or +1
        x_step = (new_piece_x - choose_piece_x) // distance if new_piece_x != choose_piece_x else 0
        y_step = (new_piece_y - choose_piece_y) // distance if new_piece_y != choose_piece_y else 0

        for i in range(1, distance):
            check_x = choose_piece_x + i * x_step
            check_y = choose_piece_y + i * y_step
            if matrix[check_x][check_y] != "-":
                print("Invalid move: piece in the way")
                path_clear  = False
                break
        if path_clear :
            if matrix[new_piece_x][new_piece_y] != "-" :
                print("Rook captured successfully.") 
            else:
                print("Rook moved successfully.")
            matrix[new_piece_x][new_piece_y] = "r"
            matrix[choose_piece_x][choose_piece_y] = "-"       
                
    else:
        print("Invalid move: rook can only move in straight lines")

def bishop_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces):
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    path_clear  = True
    if dx == dy and matrix[new_piece_x][new_piece_y] not in friendly_pieces:
        distance = dx #or dy. no need for max(dx, dy)
        x_step = (new_piece_x - choose_piece_x) // distance if new_piece_x != choose_piece_x else 0
        y_step = (new_piece_y - choose_piece_y) // distance if new_piece_y != choose_piece_y else 0
        
        for i in range(1, distance):
            check_x = choose_piece_x + i * x_step
            check_y = choose_piece_y + i * y_step
            if matrix[check_x][check_y] != "-":
                print("Invalid move: piece in the way")
                path_clear  = False
                break
        if path_clear :
            if matrix[new_piece_x][new_piece_y] != "-":
                print("bishop captured successfully.") 
            else:
                print("bishop moved successfully.")
            matrix[new_piece_x][new_piece_y] = "b"
            matrix[choose_piece_x][choose_piece_y] = "-"
                             
    else:
        print("Invalid move:bishop can only move in diagonal  lines")      

def Queen_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces):
    dx = abs(new_piece_x - choose_piece_x)
    dy = abs(new_piece_y - choose_piece_y)
    path_clear  = True
    if (dx == dy or new_piece_x == choose_piece_x or new_piece_y == choose_piece_y) and matrix[new_piece_x][new_piece_y] not in friendly_pieces:
        distance = max(dx, dy)
        x_step = (new_piece_x - choose_piece_x) // distance if new_piece_x != choose_piece_x else 0
        y_step = (new_piece_y - choose_piece_y) // distance if new_piece_y != choose_piece_y else 0
        
        for i in range(1, distance):
            check_x = choose_piece_x + i * x_step
            check_y = choose_piece_y + i * y_step
            if matrix[check_x][check_y] != "-":
                print("Invalid move: piece in the way")
                path_clear  = False
                break
        if path_clear :
            if matrix[new_piece_x][new_piece_y] != "-":
                print("Queen captured successfully.") 
            else:
                print("Queen moved successfully.")
            matrix[new_piece_x][new_piece_y] = "q"
            matrix[choose_piece_x][choose_piece_y] = "-"
                             
    else:
        print("Invalid move:Queen")    


def castling(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces):
    from_p = matrix[choose_piece_x][choose_piece_y]
    to_p = matrix[new_piece_x][new_piece_y]
    path_clear  = True

    if (from_p in ("k", "r")) and (to_p in ("k", "r")) and (from_p != to_p):
        dx = abs(new_piece_x - choose_piece_x)
        x_step = (new_piece_x - choose_piece_x) // dx if new_piece_x != choose_piece_x else 0
        for i in range(1, dx):
                check_x = choose_piece_x + i * x_step
                if matrix[check_x][choose_piece_y] != "-":
                    print("Invalid move: piece in the way")
                    path_clear  = False
                    break
                if path_clear :
                        if from_p == "k" and to_p == "r" and to_p == matrix[7][7]:
                            matrix[choose_piece_x + 2][choose_piece_y] == "k"
                            matrix[choose_piece_x][choose_piece_y] == "-" 
                            matrix[choose_piece_x + 2][choose_piece_y] == "k" 
                            matrix[new_piece_x-2][new_piece_y] == "r"
                            matrix[new_piece_x][new_piece_y] == "-"
                        
                           
                        elif to_p == "k" and from_p == "r":
                            print("y is 1")
                        
                    
        
    



def choose_piece(choose_piece_x, choose_piece_y, matrix):
    piece = matrix[choose_piece_x][choose_piece_y]
    names = {
        "p": "Pawn",
        "n": "Knight",
        "k": "King",
        "r": "Rook",
        "b": "Bishop",
        "q": "Queen"
    }
    if piece in names:
        print(f"You have chosen a {names[piece]}.")
    elif piece == "-":
        print("This square is empty.")
    else:
        print(f"You have chosen an enemy piece ({piece}).")




def Total_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix,friendly_pieces):
    if matrix[choose_piece_x][choose_piece_y] == "p":
        Pawn_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces)
    if matrix[choose_piece_x][choose_piece_y] == "n":
        knight_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces)
    if matrix[choose_piece_x][choose_piece_y] == "k":
        king_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces)
    if matrix[choose_piece_x][choose_piece_y] == "r":
        Rook_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces)
    if matrix[choose_piece_x][choose_piece_y] == "b":
        bishop_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces)
    if matrix[choose_piece_x][choose_piece_y] == "q":
        Queen_Movement(new_piece_x, new_piece_y, choose_piece_x, choose_piece_y, matrix, friendly_pieces)
