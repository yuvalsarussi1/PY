import os
def menu():
    while True:
        try:
            menu = int(input(
            "----------------------\n"
            "1 - show all people\n"
            "2 - add a person\n"
            "3 - quit\n"
            "choose option(1/2/3):"))
        except ValueError:
            continue
        if menu not in [1,2,3]:
            print("only 1/2/3")
            continue
        else:
            break
    return menu
def show_people():
    with open("Python_learn/Phase 1/people.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, age, hobby = line.strip().split(",")
                print(name, age, hobby)
            print("----------------------")
            print("total:",len(lines),"people")

def add_person():
    while True:
        new_person = input("Enter a new person (name,age,hobby): ")
        parts = new_person.split(",")

        if len(parts) != 3:
            print("Input must have 3 parts: name,age,hobby")
            continue

        name, age_str, hobby = parts

        if not age_str.isdigit():
            print("Age must be a number")
            continue

        age = int(age_str)
        if not (1 <= age <= 100):
            print("Age must be between 1 and 100")
            continue

        with open("Python_learn/Phase 1/people.txt", "a") as file:
            file.write(f"{name},{age},{hobby}\n")
        break
def create_file_if_missing():
    if not os.path.exists("Python_learn/Phase 1/people.txt"):
        with open("Python_learn/Phase 1/people.txt", "w") as file:
            file.write("yuval,22,coding\n")
            file.write("amit,18,gaming\n")
            file.write("shachar,10,minecraft\n")

#========================================
create_file_if_missing()

while True:

    choice = menu()
    if choice == 1:
        show_people()
    elif choice == 2:
        add_person()
    elif choice ==3: 
         break
    else:
         print("invalid choice")