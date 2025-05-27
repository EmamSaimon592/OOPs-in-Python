#  Write a program by creating an 'Employee' class having the following functions and 
# print the final salary. 
# 1 - ‘getInfo ()' which takes the salary, number of hours of work per day of employee 
# as parameters 
# 2 - 'AddSal()' which adds $10 to the salary of the employee if it is less than $500. 
# 3 - ‘AddWork ()' which adds $5 to the salary of the employee if the number of hours 
# of work per day is more than 6 hours. 

class Employee:
    def __init__(self):
        self.salary = 0
        self.hours_per_day = 0

    def getInfo(self, salary, hours_per_day):
        self.salary = salary
        self.hours_per_day = hours_per_day

    def AddSal(self):
        if self.salary < 500:
            self.salary += 10

    def AddWork(self):
        if self.hours_per_day > 6:
            self.salary += 5

    def printSalary(self):
        print("Final Salary:", self.salary)

# Create an employee object
emp = Employee()

# Get input from user
salary = int(input("Enter salary: "))
hours = int(input("Enter number of working hours per day: "))

# Set employee info and apply rules
emp.getInfo(salary, hours)
emp.AddSal()
emp.AddWork()
emp.printSalary()
