# Task 1
# Objection: Build a basic calulator that can perform addition, subtraction, multiplication, and division.

# Functions for the different expressions including the Zero Division error
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Task 2 

# Used convert user input into the arithmetic functions
functions = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

# This function and will make it lowercase to ensure it matches the dictionary keys
function_type = input("Enter the operation you want to perform (add, subtract, multiply, divide): ").lower()

# If the function was in the dictionary, it will ask for the two numbers and perform the operation
if function_type in functions:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Executes the function
    result = functions[function_type](num1, num2)

    print(f"Result: {result}")
else:
    print("Invalid function name.")