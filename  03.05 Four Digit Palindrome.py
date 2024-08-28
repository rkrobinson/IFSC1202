# Input a four-digit integer
number = int(input("Enter a four-digit integer: "))

# Extract individual digits
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
units = number % 10

# Check if it's a palindrome
if thousands == units and hundreds == tens:
    print("YES")
else:
    print("NO")