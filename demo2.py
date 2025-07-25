import random
randomlist = []
while True:
    number = random.randint(1, 4)
    randomlist.append(number)
    print("Current list:", randomlist)
    
    num = int(input("Enter a number to check: "))
    digits = [int(d) for d in str(num)]
    print(digits)
    print(randomlist)
    if len(digits) != len(randomlist):
        randomlist = []
        break
    for i in range(len(digits)):
        if digits[i] != randomlist[i]:
            print("mistake")
            randomlist = []

        