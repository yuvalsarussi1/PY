import random
import sys

def clear_screen():
    # Works on Windows and Unix
    from os import system, name
    system('cls' if name == 'nt' else 'clear')

def get_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            return val
        except ValueError:
            print("  ▶ Please enter a valid integer.")

# 1) Setup
SIZE = get_int("Enter board size (N x N): ")
NUM_MINES = get_int("Enter number of mines: ")
if NUM_MINES >= SIZE * SIZE:
    print("Too many mines for that board!")
    sys.exit(1)

# Directions for 8 neighbors
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

# 2) Generate internal board
board = [[0]*SIZE for _ in range(SIZE)]
all_cells = [(r,c) for r in range(SIZE) for c in range(SIZE)]
mines = set(random.sample(all_cells, NUM_MINES))
for r,c in mines:
    board[r][c] = 'x'

# 3) Fill numbers
for r in range(SIZE):
    for c in range(SIZE):
        if board[r][c] == 'x': continue
        count = 0
        for dr,dc in dirs:
            nr, nc = r+dr, c+dc
            if 0<=nr<SIZE and 0<=nc<SIZE and board[nr][nc]=='x':
                count += 1
        board[r][c] = count

# 4) Game state
visible = [[False]*SIZE for _ in range(SIZE)]
flags   = [[False]*SIZE for _ in range(SIZE)]
game_over = False
victory   = False

def count_flags():
    return sum(flags[r][c] for r in range(SIZE) for c in range(SIZE))

def check_victory():
    # all non-mine cells revealed
    for r in range(SIZE):
        for c in range(SIZE):
            if (r,c) not in mines and not visible[r][c]:
                return False
    return True

def show_board(final=False):
    clear_screen()
    # header
    print("    " + " ".join(f"{c:2}" for c in range(SIZE)))
    print("   " + "--"*SIZE)
    for r in range(SIZE):
        row = [f"{r:2}|"]
        for c in range(SIZE):
            if final and (r,c) in mines:
                ch = " x"
            elif flags[r][c]:
                ch = " F"
            elif visible[r][c]:
                ch = f"{board[r][c]:2}"
            else:
                ch = " ■"
            row.append(ch)
        print(" ".join(row))
    if not final:
        print(f"\nFlags: {count_flags():2}/{NUM_MINES}")

def flood_fill(r, c):
    # reveal recursively all 0-cells and their border
    if not (0<=r<SIZE and 0<=c<SIZE): return
    if visible[r][c] or flags[r][c]: return
    visible[r][c] = True
    if board[r][c] != 0:
        return
    for dr,dc in dirs:
        flood_fill(r+dr, c+dc)

# 5) Main loop
show_board()
while not game_over and not victory:
    cmd = input("\nEnter move (row col), or 'flag r c', or 'exit': ").strip().lower()
    if cmd == 'exit':
        break

    parts = cmd.split()
    if len(parts)==3 and parts[0]=='flag':
        try:
            r, c = map(int, parts[1:])
        except:
            print("Invalid coordinates.")
            continue
        if not (0<=r<SIZE and 0<=c<SIZE):
            print("Out of range.")
        elif visible[r][c]:
            print("Can't flag a revealed cell.")
        elif count_flags()>=NUM_MINES and not flags[r][c]:
            print("No flags left.")
        else:
            flags[r][c] = not flags[r][c]

    elif len(parts)==2:
        try:
            r, c = map(int, parts)
        except:
            print("Invalid input.")
            continue
        if not (0<=r<SIZE and 0<=c<SIZE):
            print("Out of range.")
            continue
        if flags[r][c]:
            print("Cell is flagged. Unflag to reveal.")
            continue
        if (r,c) in mines:
            game_over = True
            print("\n💥 BOOM! You hit a mine!")
        else:
            flood_fill(r, c)
            if check_victory():
                victory = True
                print("\n🏆 Congratulations! You've cleared the board!")
    else:
        print("Unknown command.")

    if not game_over and not victory:
        show_board()

# Final reveal
show_board(final=True)
print("\nThanks for playing!")    
