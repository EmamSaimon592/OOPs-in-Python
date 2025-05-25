# Write a program to print the area of two rectangles having sides (4, 5) and (5, 8) 
# respectively by creating a class named 'Rectangle' with a function named 'Area' which 
# returns the area. Length and breadth are passed as parameters to its constructor. 

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Creating two Rectangle objects
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(5, 8)

# Printing the area of both rectangles
print("Area of Rectangle 1:", rectangle1.area())
print("Area of Rectangle 2:", rectangle2.area())
