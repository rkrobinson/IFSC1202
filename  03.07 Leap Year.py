# Prompt for a 4-digit year
year = int(input("Enter a 4-digit year: "))

# Check if it's a leap year
if year % 400 == 0:
    print("LEAP YEAR")
else:
    if year % 100 == 0:
        print("COMMON YEAR")
    else:
        if year % 4 == 0:
            print("LEAP YEAR")
        else:
            print("COMMON YEAR")