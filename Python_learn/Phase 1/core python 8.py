
people = [#Stores a list of people (each as a dictionary)

    {"name": "yuval", "age": 22, "hobby": "coding"},
    {"name": "amit", "age": 18, "hobby": "gaming"},
    {"name": "shachar", "age": 10, "hobby": "minecraft"}
]
while True: 
    name = input("enter name")# Asks the user to type a name

    if name == "q": # Repeats until the user types 'q' to quit

        break
    name_found = False
    for i in people:
        if i["name"] == name:
            print(i["age"],i["hobby"]) # If the name exists, it prints that person’s age and hobby

            name_found = True
    if name_found == False:
        print("name not found") # Otherwise, it says "Name not found"

    


