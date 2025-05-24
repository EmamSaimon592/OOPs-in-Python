#  Assign and print the roll number, phone number and address of two students having 
# names "Shofi" and "Jamshed" respectively by creating two objects of the class 'Student'.

class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.phone = ""
        self.address = ""

# Creating two student objects
student1 = Student()
student2 = Student()

# Assigning values to student1 (Shofi)
student1.name = "Shofi"
student1.roll_no = 1
student1.phone = "1234567890"
student1.address = "Dhaka"

# Assigning values to student2 (Jamshed)
student2.name = "Jamshed"
student2.roll_no = 2
student2.phone = "0987654321"
student2.address = "Chittagong"

# Printing details of student1
print("Student 1:")
print("Name:", student1.name)
print("Roll No:", student1.roll_no)
print("Phone:", student1.phone)
print("Address:", student1.address)

print("\nStudent 2:")
# Printing details of student2
print("Name:", student2.name)
print("Roll No:", student2.roll_no)
print("Phone:", student2.phone)
print("Address:", student2.address)
