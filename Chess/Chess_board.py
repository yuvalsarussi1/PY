# from Chess_pieces import pawn_Movement, knight_Movement, king_Movement


matrix = [["-" for _ in range(8)] for _ in range(8)]

#---------------------  Board building---------------
matrix[6] = ["p"] * 8
matrix[1] = ["p"] * 8

matrix[7][0] = "r"
matrix[7][7] = "r"
matrix[7][1] = "n"
matrix[7][6] = "n"
matrix[7][4] = "k"
matrix[7][2] = "b"
matrix[7][5] = "b"
matrix[7][3] = "q"

matrix[0][0] = "R"
matrix[0][7] = "R"
matrix[0][1] = "N"
matrix[0][6] = "N"
matrix[0][4] = "K"
matrix[0][2] = "B"
matrix[0][5] = "B"
matrix[0][3] = "Q"

friendly_pieces = ["r","n","k","b","q","p"]
#------------------------------------------------


# for row in matrix:
#     print(row)
print("======================")
for row_index in range(8):
    print("|",8 - row_index,"" ,end=" ")  # Print row label (8 to 1)
    for col_index in range(8):
        print(matrix[row_index][col_index], end=" ")
    print("|")
print("|                    |")
print("|  "," a", "b" , "c", "d", "e", "f", "g", "h", "|")
print("======================")

def Pawn_Movement(new_piece_x, new_piece_y):
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

def knight_Movement(new_piece_x, new_piece_y):
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

def king_Movement(new_piece_x, new_piece_y):
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
        print("Invalid King move.")
     
def Rook_Movement(new_piece_x, new_piece_y):
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
    
def bishop_Movement(new_piece_x, new_piece_y):
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
            
def Queen_Movement(new_piece_x, new_piece_y):
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



def choose_piece(choose_piece_x, choose_piece_y):
    
    if matrix[choose_piece_x][choose_piece_y] == "p":
        print("You have chosen a pawn.")
    if matrix[choose_piece_x][choose_piece_y] == "n":
        print("You have chosen a Knight.")
    if matrix[choose_piece_x][choose_piece_y] == "k":
        print("You have chosen a King.")
    if matrix[choose_piece_x][choose_piece_y] == "r":
        print("You have chosen a Rook.")
    if matrix[choose_piece_x][choose_piece_y] == "b":
        print("You have chosen a Bishop.")
    if matrix[choose_piece_x][choose_piece_y] == "q":
        print("You have chosen a Queen.")
        

def Total_Movement(new_piece_x, new_piece_y):
    if matrix[choose_piece_x][choose_piece_y] == "p":
        Pawn_Movement(new_piece_x, new_piece_y)
    if matrix[choose_piece_x][choose_piece_y] == "n":
        knight_Movement(new_piece_x, new_piece_y)
    if matrix[choose_piece_x][choose_piece_y] == "k":
        king_Movement(new_piece_x, new_piece_y)
    if matrix[choose_piece_x][choose_piece_y] == "r":
        Rook_Movement(new_piece_x, new_piece_y)
    if matrix[choose_piece_x][choose_piece_y] == "b":
        bishop_Movement(new_piece_x, new_piece_y)
    if matrix[choose_piece_x][choose_piece_y] == "q":
        Queen_Movement(new_piece_x, new_piece_y)








   
    


while True:
    #takes input and break it down to x(int) and y(letter). 
    coord = input("Choose piece: ")
    x = int(coord[1:])
    letter = coord[0]
    #change the letter to number 
    y = ord(letter.lower()) - ord('a')
    #chagne x and y to numbers for matrix list
    choose_piece_x = 8 - x 
    choose_piece_y = y

    choose_piece(choose_piece_x, choose_piece_y)

    coord = input("Enter Movement: ")
    x = int(coord[1:])
    letter = coord[0]
    #change the letter to number 
    y = ord(letter.lower()) - ord('a')
    #chagne x and y to numbers for matrix list
    new_piece_x = 8 - x 
    new_piece_y = y
    
    if (0 <= new_piece_x < 8 and 0 <= new_piece_y < 8):  
        Total_Movement(new_piece_x, new_piece_y)
    else:
        print("Invalid move: out of board boundaries")


    print("======================")
    for row_index in range(8):
        print("|",8 - row_index,"" ,end=" ")  # Print row label (8 to 1)
        for col_index in range(8):
            print(matrix[row_index][col_index], end=" ")
        print("|")
    print("|                    |")
    print("|  "," a", "b" , "c", "d", "e", "f", "g", "h", "|")
    print("======================")






# def Rook_Movement(new_piece_x, new_piece_y):
#     if new_piece_x == choose_piece_x and new_piece_y != choose_piece_y:
#         for i in range 
#         matrix[new_piece_x][new_piece_y] = 2
#         matrix[choose_piece_x][choose_piece_y] = 0
#         print("Rook moved successfully.")
#     elif new_piece_x != choose_piece_x and new_piece_y == choose_piece_y:
#         matrix[new_piece_x][new_piece_y] = 2
#         matrix[choose_piece_x][choose_piece_y] = 0
#         print("Rook moved successfully.")
#     else:
#         print("Invalid move. A rook can only move horizontally or vertically.")


# def Movement (piece_x, piece_y, new_piece_x, new_piece_y):
#     if matrix[piece_y][piece_x] == 1:
#         def pawn_move(COLUMN=new_piece_x, ROW=new_piece_y):
# def pawn_move(COLUMN,ROW):
    
#     matrix[ROW][COLUMN] = 1
#     matrix[piece_x][piece_y] = 0


#     for row in matrix:
#         print(row)

# pawn_move(1, 3)






# def Eating(new_piece_x, new_piece_y):
#     if matrix[choose_piece_x][choose_piece_y] == 1:
#         if new_piece_x == choose_piece_x - 1 and abs(new_piece_y - choose_piece_y) == 1:
#             if matrix[new_piece_x][new_piece_y] != 0:
#                 matrix[new_piece_x][new_piece_y] = 1
#                 matrix[choose_piece_x][choose_piece_y] = 0
#                 print("Pawn captured successfully.")