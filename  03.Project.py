while True:
    try:
        # Get input from the user
        user_input = input("Enter the first number (or type 'quit' to exit): ").lower()
        if user_input == "quit" or user_input == "exit":
            print("Exiting the calculator.")
            break
        num1 = float(user_input)

        operator = input("Enter the operator (+, -, *, /): ")
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator. Please use one of (+, -, *, /).")
            continue

        user_input = input("Enter the second number (or type 'quit' to exit): ").lower()
        if user_input == "quit" or user_input == "exit":
            print("Exiting the calculator.")
            break
        num2 = float(user_input)

        # Perform the appropriate calculation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero")
                continue
            result = num1 / num2

        # Output the result
        print(f"{num1} {operator} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
