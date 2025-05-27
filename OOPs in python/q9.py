# Write a program that would print the information (name, year of joining, salary, 
# address) of three employees by creating a class named 'Employee'. The output should 
# be as follows:  
# Name       Year of Joining   Address 
# Shamsu        1992          chittagong
# Soleman       1994          Chittagong
# Kalam         1990            Dhaka

class Employee:
    def __init__(self, name, year_of_joining, address):
        self.name = name
        self.year_of_joining = year_of_joining
        self.address = address

# Creating employee objects
emp1 = Employee("Shamsu", 1992, "chittagong")
emp2 = Employee("Soleman", 1994, "Chittagong")
emp3 = Employee("Kalam", 1990, "Dhaka")

# Printing header
print("Name  Year of Joining  Address")

# Printing employee data
print(emp1.name, emp1.year_of_joining, emp1.address)
print(emp2.name, emp2.year_of_joining, emp2.address)
print(emp3.name, emp3.year_of_joining, emp3.address)
