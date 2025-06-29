# Write a program to print the area of a rectangle by creating a class named 'Area' having 
# two functions. First function named as 'setDim' takes the length and breadth of the 
# rectangle as parameters and the second function named as 'getArea' returns the area of 
# the rectangle. Length and breadth of the rectangle are entered through keyboard. --------

class Area:
    def __init__(self):
        self.length = 0
        self.breadth = 0

    def setDim(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        return self.length * self.breadth

# Taking input from the user
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

# Creating an object of Area
rect = Area()

# Setting dimensions and printing area
rect.setDim(length, breadth)
print("Area of the rectangle:", rect.getArea())
