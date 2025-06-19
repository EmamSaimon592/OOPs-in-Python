# Print the average of three numbers entered by the user by creating a class named 
# 'Average' having a function to calculate and print the average without creating any 
# object of the Average class. 

class Average:
    @staticmethod    # static method = which allows you to call the method without creating an object of the class.
    def calculate_average(a, b, c):
        avg = (a + b + c) / 3
        print("Average:", avg)

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Calling the static method without creating an object
Average.calculate_average(num1, num2, num3)

# End code
