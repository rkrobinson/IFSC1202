import csv

# Step 1: Create an empty two-dimensional list to store the data from the CSV file
distances = []

# Step 2: Read the CSV file and load each line into the distances list
try:
    with open('09.Project Distances.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            distances.append(row)  # Append each row to the distances list

except FileNotFoundError:
    print("The file '09.Project Distances.csv' was not found.")
    exit()

# Step 3: Print the two-dimensional list formatted as a table
print("Cities", end="    ")
for city in distances[0][1:]:  # Skip the first empty cell in the first row
    print(f"{city:<10}", end=" ")
print()

for i in range(1, len(distances)):
    print(f"{distances[i][0]:<10}", end=" ")  # Print the From City
    for distance in distances[i][1:]:
        print(f"{distance:<10}", end=" ")  # Print each distance value
    print()

# Step 4: Prompt for a From City
from_city = input("\nEnter From City: ")

# Step 5: Prompt for a To City
to_city = input("Enter To City: ")

# Step 6: Search the zeroth column for the From City
from_city_index = -1
for i in range(1, len(distances)):  # Start from 1 to skip the header row
    if distances[i][0].lower() == from_city.lower():
        from_city_index = i
        break

# Step 7: Search the zeroth row for the To City
to_city_index = -1
for j in range(1, len(distances[0])):  # Start from 1 to skip the header column
    if distances[0][j].lower() == to_city.lower():
        to_city_index = j
        break

# Step 8: Display results or handle invalid cities
if from_city_index == -1:
    print("Invalid From City")
elif to_city_index == -1:
    print("Invalid To City")
else:
    distance = distances[from_city_index][to_city_index]
    print(f"\n{from_city} to {to_city} - {distance} miles")
