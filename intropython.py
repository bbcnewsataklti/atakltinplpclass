num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
else:
    print("Invalid operation.")
print(f"The result is: {result}")