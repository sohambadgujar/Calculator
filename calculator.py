# CALCULATOR

while True:
    
    # Input from the user
    num1 = float(input("Enter the first number  : "))
    num2 = float(input("Enter the second number : "))

    
    print("Choose an operation:")
    print("Addition (+)")
    print("Subtraction (-)")
    print("Multiplication (*)")
    print("Division (/)")
    operation = input("Enter your operation (+, -, *, /): ")

    # Calculations 
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed")
    else:
        print("Invalid operation. Please enter only +, -, *, or /")

    # If user wants to perform more calculation 
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != 'yes':
        print("Thank you for using the calculator!")
        break