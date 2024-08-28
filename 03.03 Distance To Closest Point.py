# Input coordinates
A = int(input("Enter coordinate of point A: "))
B = int(input("Enter coordinate of point B: "))
C = int(input("Enter coordinate of point C: "))

# Calculate distances
distance_AB = abs(B - A)
distance_AC = abs(C - A)

# Compare distances and determine the smallest
if distance_AB < distance_AC:
    smallest_distance = distance_AB
else:
    smallest_distance = distance_AC

# Print the result
print(f"The distance from A to the closest point is: {smallest_distance}")