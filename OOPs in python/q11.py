#  Create a class named 'Rectangle' with two data members 'length' and 'breadth' and two 
# functions to print the area and perimeter of the rectangle respectively. Its constructor 
# having parameters for length and breadth is used to initialize the length and breadth of 
# the rectangle. Let class 'Square' inherit the 'Rectangle' class with its constructor 
# having a parameter for its side (suppose s) calling the constructor of its parent class. 
# Print the area and perimeter of a rectangle and a square. 

# Define the Rectangle class
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def print_area(self):
        area = self.length * self.breadth
        print("Rectangle Area:", area)

    def print_perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        print("Rectangle Perimeter:", perimeter)

# Define the Square class that inherits from Rectangle
class Square(Rectangle):
    def __init__(self, side):
        # super() is used to call the constructor of the parent class.
        super().__init__(side, side)  # Call parent constructor with same side for length and breadth

# Create a Rectangle object
rect = Rectangle(10, 5)
rect.print_area()
rect.print_perimeter()

# Create a Square object
sq = Square(6)
sq.print_area()
sq.print_perimeter()
