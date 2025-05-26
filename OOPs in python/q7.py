# Print the sum, difference and product of two complex numbers by creating a class 
# named 'Complex' with separate functions for each operation whose real and imaginary 
# parts are entered by the user

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        print("Sum: " + str(real) + " + " + str(imag) + "i")

    def subtract(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        print("Difference: " + str(real) + " + " + str(imag) + "i")

    def multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        print("Product: " + str(real) + " + " + str(imag) + "i")

# Taking input from the user
print("Enter first complex number:")
real1 = int(input("Real part: "))
imag1 = int(input("Imaginary part: "))

print("\nEnter second complex number:")
real2 = int(input("Real part: "))
imag2 = int(input("Imaginary part: "))

# Creating Complex number objects
c1 = Complex(real1, imag1)
c2 = Complex(real2, imag2)

# Performing operations
c1.add(c2)
c1.subtract(c2)
c1.multiply(c2)

