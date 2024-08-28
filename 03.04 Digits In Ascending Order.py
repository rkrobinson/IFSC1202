# Input a three-digit integer
number = int(input("Enter a three-digit integer: "))

# Extract individual digits
hundreds = number // 100
tens = (number % 100) // 10
ones = number % 10

# Check if digits are in ascending order
if hundreds < tens and tens < ones:
    print("YES")
else:
    print("NO")