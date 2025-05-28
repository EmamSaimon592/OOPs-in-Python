# We want to store the information of different vehicles. Create a class named Vehicle 
# with two data member named mileage and price. Create its two subclasses 
# *Car with data members to store ownership cost, warranty (by years), seating capacity 
# and fuel type (diesel or petrol). 
# *Bike with data members to store the number of cylinders, number of gears, cooling 
# type(air, liquid or oil), wheel type(alloys or spokes) and fuel tank size(in inches) 
# Make another two subclasses Audi and Ford of Car, each having a data member to store 
# the model type. Next, make two subclasses Walton and TVS, each having a data 
# member to store the make-type. 
# Now, store and print the information of an Audi and a Ford car (i.e. model type, 
# ownership cost, warranty, seating capacity, fuel type, mileage and price.) Do the same 
# for a Walton and a TVS bike

# Base class
class Vehicle:
    def __init__(self, mileage, price):
        self.mileage = mileage
        self.price = price

# Subclass of Vehicle for Car
class Car(Vehicle):
    def __init__(self, mileage, price, ownership_cost, warranty, seating_capacity, fuel_type):
        super().__init__(mileage, price)
        self.ownership_cost = ownership_cost
        self.warranty = warranty
        self.seating_capacity = seating_capacity
        self.fuel_type = fuel_type

# Subclass of Vehicle for Bike
class Bike(Vehicle):
    def __init__(self, mileage, price, cylinders, gears, cooling_type, wheel_type, fuel_tank_size):
        super().__init__(mileage, price)
        self.cylinders = cylinders
        self.gears = gears
        self.cooling_type = cooling_type
        self.wheel_type = wheel_type
        self.fuel_tank_size = fuel_tank_size

# Subclasses of Car
class Audi(Car):
    def __init__(self, model_type, mileage, price, ownership_cost, warranty, seating_capacity, fuel_type):
        super().__init__(mileage, price, ownership_cost, warranty, seating_capacity, fuel_type)
        self.model_type = model_type

    def display(self):
        print("\n--- Audi Car Information ---")
        print(f"Model Type: {self.model_type}")
        print(f"Ownership Cost: ${self.ownership_cost}")
        print(f"Warranty: {self.warranty} years")
        print(f"Seating Capacity: {self.seating_capacity}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Mileage: {self.mileage} km/l")
        print(f"Price: ${self.price}")

class Ford(Car):
    def __init__(self, model_type, mileage, price, ownership_cost, warranty, seating_capacity, fuel_type):
        super().__init__(mileage, price, ownership_cost, warranty, seating_capacity, fuel_type)
        self.model_type = model_type

    def display(self):
        print("\n--- Ford Car Information ---")
        print(f"Model Type: {self.model_type}")
        print(f"Ownership Cost: ${self.ownership_cost}")
        print(f"Warranty: {self.warranty} years")
        print(f"Seating Capacity: {self.seating_capacity}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Mileage: {self.mileage} km/l")
        print(f"Price: ${self.price}")

# Subclasses of Bike
class Walton(Bike):
    def __init__(self, make_type, mileage, price, cylinders, gears, cooling_type, wheel_type, fuel_tank_size):
        super().__init__(mileage, price, cylinders, gears, cooling_type, wheel_type, fuel_tank_size)
        self.make_type = make_type

    def display(self):
        print("\n--- Walton Bike Information ---")
        print(f"Make Type: {self.make_type}")
        print(f"Cylinders: {self.cylinders}")
        print(f"Gears: {self.gears}")
        print(f"Cooling Type: {self.cooling_type}")
        print(f"Wheel Type: {self.wheel_type}")
        print(f"Fuel Tank Size: {self.fuel_tank_size} inches")
        print(f"Mileage: {self.mileage} km/l")
        print(f"Price: ${self.price}")

class TVS(Bike):
    def __init__(self, make_type, mileage, price, cylinders, gears, cooling_type, wheel_type, fuel_tank_size):
        super().__init__(mileage, price, cylinders, gears, cooling_type, wheel_type, fuel_tank_size)
        self.make_type = make_type

    def display(self):
        print("\n--- TVS Bike Information ---")
        print(f"Make Type: {self.make_type}")
        print(f"Cylinders: {self.cylinders}")
        print(f"Gears: {self.gears}")
        print(f"Cooling Type: {self.cooling_type}")
        print(f"Wheel Type: {self.wheel_type}")
        print(f"Fuel Tank Size: {self.fuel_tank_size} inches")
        print(f"Mileage: {self.mileage} km/l")
        print(f"Price: ${self.price}")


# # Creating Audi and Ford objects
# audi_car = Audi("A6", 18, 50000, 2000, 5, 5, "Petrol")
# ford_car = Ford("Mustang", 12, 60000, 2500, 4, 4, "Diesel")

# # Creating Walton and TVS objects
# walton_bike = Walton("Walton Xplore", 45, 1500, 1, 5, "Air", "Alloys", 14)
# tvs_bike = TVS("TVS Apache", 50, 1800, 1, 5, "Oil", "Spokes", 13)

# # Displaying information
# audi_car.display()
# ford_car.display()
# walton_bike.display()
# tvs_bike.display()


#output===>

# --- Audi Car Information ---
# Model Type: A6
# Ownership Cost: $2000
# Warranty: 5 years
# Seating Capacity: 5
# Fuel Type: Petrol
# Mileage: 18 km/l
# Price: $50000

# --- Ford Car Information ---
# Model Type: Mustang
# Ownership Cost: $2500
# Warranty: 4 years
# Seating Capacity: 4
# Fuel Type: Diesel
# Mileage: 12 km/l
# Price: $60000

# --- Walton Bike Information ---
# Make Type: Walton Xplore
# Cylinders: 1
# Gears: 5
# Cooling Type: Air
# Wheel Type: Alloys
# Fuel Tank Size: 14 inches
# Mileage: 45 km/l
# Price: $1500

# --- TVS Bike Information ---
# Make Type: TVS Apache
# Cylinders: 1
# Gears: 5
# Cooling Type: Oil
# Wheel Type: Spokes
# Fuel Tank Size: 13 inches
# Mileage: 50 km/l
# Price: $1800

