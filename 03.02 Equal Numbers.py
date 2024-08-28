# Input three numbers
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

# Initialize a variable to count equal numbers
equal_count = 0

# Check equality using if-else statements
if num1 == num2 == num3:
    equal_count = 3
else:
    if num1 == num2 or num1 == num3 or num2 == num3:
        equal_count = 2
    else:
        equal_count = 0

# Print the result
print(equal_count)