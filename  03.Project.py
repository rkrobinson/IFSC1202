# Define operations using functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

# Dictionary to map operators to functions
OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def get_number(prompt):
    """
    Prompt the user to enter a number.
    Returns the number as a float.
    If the user types 'quit' or 'exit', returns None.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ('quit', 'exit'):
            return None
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'quit' to exit.")

def get_operator():
    """
    Prompt the user to enter an operator.
    Returns the operator as a string.
    If the user types 'quit' or 'exit', returns None.
    """
    while True:
        operator = input("Enter the operator (+, -, *, /): ").strip()
        if operator.lower() in ('quit', 'exit'):
            return None
        if operator in OPERATIONS:
            return operator
        else:
            print("Invalid operator. Please choose from (+, -, *, /) or type 'quit' to exit.")

def perform_calculation(num1, operator, num2):
    """
    Perform the calculation based on the operator.
    Returns the result of the operation.
    """
    try:
        operation_func = OPERATIONS[operator]
        return operation_func(num1, num2)
    except ValueError as ve:
        return ve

def calculator():
    """
    Main function to run the calculator.
    """
    print("Welcome to the Modular Calculator!")
    print("You can type 'quit' or 'exit' at any time to stop.\n")
    
    while True:
        num1 = get_number("Enter the first number: ")
        if num1 is None:
            print("Exiting the calculator. Goodbye!")
            break

        operator = get_operator()
        if operator is None:
            print("Exiting the calculator. Goodbye!")
            break

        num2 = get_number("Enter the second number: ")
        if num2 is None:
            print("Exiting the calculator. Goodbye!")
            break

        result = perform_calculation(num1, operator, num2)
        print(f"{num1} {operator} {num2} = {result}\n")

if __name__ == "__main__":
    calculator()

