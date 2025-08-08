import random
secret_number = random.randint(1, 100)
num_guess = 0
while True:
    num1 = int(input("guess the number"))
    
    if num1 < 1 or num1 > 100:
        print("number between 1 - 100")
        continue    
    
    num_guess = num_guess + 1
    print("number of tries =", num_guess)

    if num1 == secret_number:
        print("currect")
        break
    if num1 < secret_number:
        print("too low")
    elif num1 > secret_number:
        print("too high")
    

   
    

