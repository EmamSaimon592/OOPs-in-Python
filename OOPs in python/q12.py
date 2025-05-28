# Create a class named 'Shape' with a function to print "This is a shape". Then create 
# two other classes named 'Rectangle' and 'Circle' inheriting the Shape class, both 
# having a function to print "This is rectangular shape" and "This is circular shape" 
# respectively. Create a subclass 'Square' of 'Rectangle' having a function to print 
# "Square is a rectangle". Now call the function of the 'Shape' and the 'Rectangle' class 
# by the object of the 'Square' class.

# Base class
class Shape:
    def print_shape(self):
        print("This is a shape")

# Derived class from Shape
class Rectangle(Shape):
    def print_rectangle(self):
        print("This is rectangular shape")

# Another derived class from Shape
class Circle(Shape):
    def print_circle(self):
        print("This is circular shape")

# Subclass of Rectangle
class Square(Rectangle):
    def print_square(self):
        print("Square is a rectangle")

# Create an object of Square
sq = Square()

# Call function of Shape using Square object
sq.print_shape()

# Call function of Rectangle using Square object
sq.print_rectangle()
