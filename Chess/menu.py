from main_file import main

def menu():
    while True:
        print("\n♟️  CHESS GAME MENU ♟️")
        print("1. Start New Game")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            main()  # Start the game loop
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    menu()