#Prompting the user for a mathematical operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input(" Choose the operation (+, -, *, /): ").lower()

# Perform the operation using match case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result of is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of is {result}.")
        else:
            print("Cannot divide by zero.")