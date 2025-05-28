# Suppose you have a Bank with an initial amount of $50 and you have to add some more 
# amount to it. Create a class 'AddAmount' with a data member named 'amount' with an 
# initial value of $50. Now make two constructors of this class as follows: 
# a. without any parameter - no amount will be added to the  Bank 
# b. Having a parameter which is the amount that will be added to the Bank 
# Create an object of the 'AddAmount' class and display the final amount in the 
# Bank. 

class AddAmount:
    def __init__(self, add=0):
        self.amount = 50  # Initial amount in the bank
        self.amount += add  # Add the given amount (default is 0)

    def display_amount(self):
        print("Final amount in the bank: $", self.amount)

# Case a: No amount added (default constructor)
obj1 = AddAmount()
obj1.display_amount()

# Case b: Add $100 to the bank
obj2 = AddAmount(100)
obj2.display_amount()
