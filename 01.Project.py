# Input the total number of days
total_days = int(input("Enter the number of days: "))

# Calculate years
years = total_days // 365

# Calculate remaining days after years
remaining_days_after_years = total_days % 365

# Calculate weeks
weeks = remaining_days_after_years // 7

# Calculate remaining days
days = remaining_days_after_years % 7

# Print the results
print(f"{total_days} days is equivalent to:")
print(f"{years} years")
print(f"{weeks} weeks")
print(f"{days} days")