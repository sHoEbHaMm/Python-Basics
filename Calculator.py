#Python calculator

operator = input("Enter an operator (+, -, *, /): ")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if operator == "+":
    print("Output:", round(number1 + number2))
elif operator == "-":
    print("Output:", round(number1 - number2))
elif operator == "/":
    print("Output:", round(number1/number2))
elif operator == "*":
    print("Output:", round(number1 * number2))
else:
    print("Invalid operation")