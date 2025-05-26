# Write a program to print the volume of a box by creating a class named 'Volume' with 
# an initialization list to initialize its length, breadth and height. (Just to make you familiar 
# with initialization lists)

class Volume:
    def __init__(self, length, breadth, height):
        # This is similar to an initialization list in C++
        self.length = length
        self.breadth = breadth
        self.height = height

    def get_volume(self):
        return self.length * self.breadth * self.height

# Taking input from the user
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
height = float(input("Enter height: "))

# Creating object and calculating volume
box = Volume(length, breadth, height)
print("Volume of the box:", box.get_volume())

