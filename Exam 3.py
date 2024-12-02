import math

# Triangle class definition
class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = float(s1)
        self.s2 = float(s2)
        self.s3 = float(s3)

    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s2 == self.s3 or self.s1 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def area(self):
        # Using Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))

    def angles(self):
        # Using the Law of Cosines to calculate angles
        angle1 = math.degrees(math.acos((self.s2**2 + self.s3**2 - self.s1**2) / (2 * self.s2 * self.s3)))
        angle2 = math.degrees(math.acos((self.s1**2 + self.s3**2 - self.s2**2) / (2 * self.s1 * self.s3)))
        angle3 = 180 - (angle1 + angle2)
        return [angle1, angle2, angle3]


# Read the file and process triangles
triangle_list = []

with open('Exam Three Triangles.txt', 'r') as file:
    for line in file:
        sides = line.strip().split(',')
        triangle = Triangle(*sides)
        triangle_list.append(triangle)

# Print the information for each triangle
print(f"{'Type':<12}{'Side 1':<10}{'Side 2':<10}{'Side 3':<10}{'Perimeter':<12}{'Area':<12}{'Angle 1':<10}{'Angle 2':<10}{'Angle 3':<10}")
for triangle in triangle_list:
    angles = triangle.angles()
    print(f"{triangle.type():<12}{triangle.s1:<10.2f}{triangle.s2:<10.2f}{triangle.s3:<10.2f}"
          f"{triangle.perimeter():<12.2f}{triangle.area():<12.2f}"
          f"{angles[0]:<10.2f}{angles[1]:<10.2f}{angles[2]:<10.2f}")
