import random
randomlist = []

while True:
    number = random.randint(1, 4)
    randomlist.append(number)
    print("Current list:", randomlist)

    for i in range(len(randomlist)):
        num1 = int(input(f"Guess number at position {i}: "))
        if num1 == randomlist[i]:
            print("You guessed it right!")
        else:
            print(f"Wrong! The correct number was {randomlist[i]}")
            break











