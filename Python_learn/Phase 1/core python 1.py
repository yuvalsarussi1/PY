num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /)")
if operator == "+":
    answer = num1 + num2
elif operator == "-":
    answer = num1 - num2
elif operator == "*":
    answer = num1 * num2
elif operator == "/":
    if num2 != 0:
        answer = num1 / num2
    else:
        answer = "Error: Division by zero"
else:
    answer = "Error: Invalid operator"
    
print(answer)