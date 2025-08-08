import os
if not os.path.exists("Python_learn/Phase 1/people.txt"):
    with open("Python_learn/Phase 1/people.txt", "w") as file:
        file.write("yuval,22,coding\n")
        file.write("amit,18,gaming\n")
        file.write("shachar,10,minecraft\n")
while True:
    menu = int(input(
    "----------------------\n"
    "1 - show all people\n"
    "2 - add a person\n"
    "3 - quit\n"
    "choose option(1/2/3):"))

    if menu == 1:
        with open("Python_learn/Phase 1/people.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, age, hobby = line.strip().split(",")
                print(name, age, hobby)
    elif menu == 2:
        new_person = input("enter a new person(name,age,hooby)")
        if len(new_person.split(",")) == 3:
            with open("Python_learn/Phase 1/people.txt", "a") as file:
                file.write(new_person + "\n")
        else:
            print("too many args")
            continue

    elif menu == 3:
        break

#name, age, hobby = line.strip().split(",") same as 3 lines above
