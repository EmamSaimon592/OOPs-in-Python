# ----Create a class named 'Student' with a string variable 'name' and an integer variable 
# 'roll_no'. Assign the value of roll_no as '2' and that of name as "Jamshed" by creating 
# an object of the class Student. 

class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = 0

# Creating an object of the class
student1 = Student()

# Assigning values
student1.name = "Jamshed"
student1.roll_no = 2

# Printing the values
print("Name:", student1.name)
print("Roll No:", student1.roll_no)
