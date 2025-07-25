import random

SIZE = int(input("Enter board size (N x N): "))
NUM_X = int(input("Enter number of hidden 'x' cells: "))

if NUM_X >= SIZE * SIZE:
    print("Too many x cells!")
    exit()

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

matrix = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
all_positions = [(i, j) for i in range(SIZE) for j in range(SIZE)]
x_positions = set(random.sample(all_positions, NUM_X))

for i, j in x_positions:
    matrix[i][j] = "x"

for i in range(SIZE):
    for j in range(SIZE):
        if matrix[i][j] == "x":
            continue
        count = sum(
            1 for dx, dy in directions
            if 0 <= i + dx < SIZE and 0 <= j + dy < SIZE and matrix[i + dx][j + dy] == "x"
        )
        matrix[i][j] = count

visible = [[False for _ in range(SIZE)] for _ in range(SIZE)]
flags = [[False for _ in range(SIZE)] for _ in range(SIZE)]
game_over = False
victory = False

# Count remaining flags


def count_flags():
    return sum(flags[i][j] for i in range(SIZE) for j in range(SIZE))

# Show full board (x's included) at end


def show_full_board():
    header = "   " + " ".join(f"{j:2}" for j in range(SIZE))
    print(header)
    for i in range(SIZE):
        row_display = [f"{i:2}"]
        for j in range(SIZE):
            if (i, j) in x_positions:
                row_display.append(" x")
            elif visible[i][j]:
                row_display.append(f"{matrix[i][j]:2}")
            elif flags[i][j]:
                row_display.append(" F")
            else:
                row_display.append(" ■")
        print(" ".join(row_display))

# Show current board (hidden x's)


def show_board():
    header = f"\n   " + " ".join(f"{j:2}" for j in range(SIZE))
    print(header)
    for i in range(SIZE):
        row_display = [f"{i:2}"]
        for j in range(SIZE):
            if flags[i][j]:
                row_display.append(" F")
            elif visible[i][j]:
                row_display.append(f"{matrix[i][j]:2}")
            else:
                row_display.append(" ■")
        print(" ".join(row_display))
    print(f"\nFlags used: {count_flags()} / {NUM_X}")

# Reveal area (3x3 around)


def reveal_safe_area(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            ni, nj = x + dx, y + dy
            if 0 <= ni < SIZE and 0 <= nj < SIZE:
                if not flags[ni][nj] and matrix[ni][nj] != "x":
                    visible[ni][nj] = True

# Toggle flag


def toggle_flag(x, y):
    if visible[x][y]:
        print("You can't flag a revealed cell.")
        return
    if not flags[x][y] and count_flags() >= NUM_X:
        print("You have no flags left.")
        return
    flags[x][y] = not flags[x][y]

# Victory check: all safe cells revealed


def check_victory():
    for i in range(SIZE):
        for j in range(SIZE):
            if (i, j) not in x_positions and not visible[i][j]:
                return False
    return True


# Game start
print("\nGame started! Type: row col OR 'flag row col' OR 'exit'")
show_board()

while not game_over and not victory:
    user_input = input("\nYour move: ").strip().lower()
    if user_input == "exit":
        print("Goodbye!")
        break

    parts = user_input.split()
    try:
        if parts[0] == "flag" and len(parts) == 3:
            x, y = int(parts[1]), int(parts[2])
            if 0 <= x < SIZE and 0 <= y < SIZE:
                toggle_flag(x, y)
            else:
                print("Invalid coordinates.")
        elif len(parts) == 2:
            x, y = int(parts[0]), int(parts[1])
            if not (0 <= x < SIZE and 0 <= y < SIZE):
                print("Invalid coordinates.")
                continue
            if flags[x][y]:
                print("Cell is flagged. Unflag it first to reveal.")
                continue
            if (x, y) in x_positions:
                game_over = True
                print("\n💥 BOOM! You hit a mine.\n")
            else:
                reveal_safe_area(x, y)
                if check_victory():
                    victory = True
                    print("\n🎉 Congratulations! You cleared all safe cells.\n")
        else:
            print("Invalid command. Use: row col OR flag row col OR exit")
    except ValueError:
        print("Invalid input format.")

    if not game_over and not victory:
        show_board()

# Game ended: show full board
print("\nFinal Board:")
show_full_board()
