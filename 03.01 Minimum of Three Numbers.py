# Input three numbers
num1 = 3
num2 = 1
num3 = 2

# Using if and else to find the largest number
if num1 > num2 and num1 > num3:
    largest = num1
else:
    if num2 > num3:
        largest = num2
    else:
        largest = num3

print(f"{largest} is the largest number")

# Using if and else to find the smallest number
if num1 < num2 and num1 < num3:
    smallest = num1
else:
    if num2 < num3:
        smallest = num2
    else:
        smallest = num3

print(f"{smallest} is the smallest number")