while True:
    a_or_b = input("You’re in a room with two doors: A and B. Which do you choose?")
    
    if a_or_b == "A" or a_or_b == "B":
        
        if a_or_b == "A":
            q1 = int(input("1+2?"))
            if q1 == 3:
                print("you win")
                break
            else:
                print("wrong start over")
                continue
            
        if a_or_b == "B":
            q2 = int(input("1+4?"))
            if q2 == 5:
                print("you win")
                break
            else:
                print("wrong start over")
                continue
    
    else:
        print("only A OR B")
        