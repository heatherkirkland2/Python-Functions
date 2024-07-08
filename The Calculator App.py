# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

# Task 1: Functions for each arithmetic operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Task 2: User inputs for operation and numbers
def main():
    print("Welcome to the basic calculator!")
    operation = input("Choose the operation (add, subtract, multiply, divide): ").lower()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Task 3: Handling division by zero and other potential errors
    if operation == 'add':
        print(f"The result is: {add(num1, num2)}")
    elif operation == 'subtract':
        print(f"The result is: {subtract(num1, num2)}")
    elif operation == 'multiply':
        print(f"The result is: {multiply(num1, num2)}")
    elif operation == 'divide':
        result = divide(num1, num2)
        print(f"The result is: {result}" if isinstance(result, float) else result)
    else:
        print("Error: Invalid operation.")

if __name__ == "__main__":
    main()
