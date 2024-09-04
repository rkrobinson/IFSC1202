import math

def calculate_triangle_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

# Prompt the user for the side lengths
a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
c = float(input("Enter the length of side C: "))

# Calculate the area
triangle_area = calculate_triangle_area(a, b, c)
print(f"The area of the triangle is: {triangle_area:.2f} square units")