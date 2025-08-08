import os

def show_people():
    with open("Python_learn/Phase 1/people.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, age, hobby = line.strip().split(",")
                print(name, age, hobby)
def add_person():
    new_person = input("enter a new person(name,age,hooby)")
    if len(new_person.split(",")) == 3:
        with open("Python_learn/Phase 1/people.txt", "a") as file:
            file.write(new_person + "\n")
    else:
            print("too many args")
def create_file_if_missing():
    if not os.path.exists("Python_learn/Phase 1/people.txt"):
        with open("Python_learn/Phase 1/people.txt", "w") as file:
            file.write("yuval,22,coding\n")
            file.write("amit,18,gaming\n")
            file.write("shachar,10,minecraft\n")
def menu():
    menu = int(input(
    "----------------------\n"
    "1 - show all people\n"
    "2 - add a person\n"
    "3 - quit\n"
    "choose option(1/2/3):"))
    return menu

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