# Function to check if a number is special
def is_special_number(num):
    temp = num
    num_of_digits = 0
    sum_of_powers = 0
    
    # Determine the number of digits
    while temp > 0:
        num_of_digits += 1
        temp //= 10
    
    temp = num
    
    # Calculate sum of digits raised to the power of the number of digits
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_of_digits
        temp //= 10
    
    return sum_of_powers == num

# Function to find special numbers in a given range
def special_numbers_in_range(start, end):
    return [num for num in range(start, end + 1) if is_special_number(num)]

# Accepting user input for the range
start_range = int(input("Enter Start of Range: "))
end_range = int(input("Enter End of Range: "))

# Finding and displaying special numbers
special_list = special_numbers_in_range(start_range, end_range)

# Output formatting
print(f"Special Numbers between {start_range} and {end_range}:")
for special_num in special_list:
    print(special_num)
