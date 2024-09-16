# Function to check if a number is prime
def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, (num // 2) + 1))

# Function to get prime numbers in a range
def prime_numbers_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

# Accepting user input for the range
start_range = int(input("Enter Start of Range: "))
end_range = int(input("Enter End of Range: "))

# Finding and displaying prime numbers
prime_list = prime_numbers_in_range(start_range, end_range)

# Output formatting
print(f"Prime Numbers between {start_range} and {end_range}:")
for prime in prime_list:
    print(prime)
