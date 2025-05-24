# Write a program to print the area and perimeter of a triangle having sides of 3, 4 and 5 
# units by creating a class named 'Triangle' with a function to print the area and perimeter.

import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a  # side 1
        self.b = b  # side 2
        self.c = c  # side 3

    def print_perimeter(self):
        perimeter = self.a + self.b + self.c
        print("Perimeter:", perimeter)

    def print_area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2  # semi-perimeter
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print("Area:", area)

# Creating an object of Triangle with sides 3, 4, 5
triangle = Triangle(3, 4, 5)

# Printing perimeter and area
triangle.print_perimeter()
triangle.print_area()
