# Solutions to Object Oriented Programming Questions

# 1. Basic Class and Object
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Create an instance
my_car = Car("Toyota", "Corolla")
print(f"1. Created a car: {my_car.brand} {my_car.model}")

# 2. Class Method and Self
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(f"2. Full name of the car: {my_car.full_name()}")

# 3. Inheritance
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", 100)
print(f"3. Created an electric car: {my_tesla.full_name()} with {my_tesla.battery_size}kWh battery")

# 4. Encapsulation
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model
    
    def get_brand(self):
        return self.__brand
    
    def full_name(self):
        return f"{self.__brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(f"4. Encapsulated brand access: {my_car.get_brand()}")

# 5. Polymorphism
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fuel_type(self):
        return "Gasoline"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electricity"

my_car = Car("Toyota", "Corolla")
my_tesla = ElectricCar("Tesla", "Model S", 100)
print(f"5. Polymorphism: {my_car.brand} uses {my_car.fuel_type()}, while {my_tesla.brand} uses {my_tesla.fuel_type()}")

# 6. Class Variables
class Car:
    # Class variable
    total_cars = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")
print(f"6. Total cars created: {Car.total_cars}")

# 7. Static Method
class Car:
    total_cars = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1
    
    @staticmethod
    def general_description():
        return "A car is a wheeled motor vehicle used for transportation."

print(f"7. Static method: {Car.general_description()}")

# 8. Property Decorators
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model  # Convention for protected attribute
    
    @property
    def model(self):
        return self._model

my_car = Car("Toyota", "Corolla")
print(f"8. Read-only model: {my_car.model}")
# Attempting to set model will raise an AttributeError
# my_car.model = "Camry"  # This would raise an error

# 9. Class Inheritance and isinstance() Function
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", 100)
print(f"9. isinstance() checks: Is my_tesla a Car? {isinstance(my_tesla, Car)}")
print(f"   Is my_tesla an ElectricCar? {isinstance(my_tesla, ElectricCar)}")

# 10. Multiple Inheritance
class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
    
    def describe_battery(self):
        return f"{self.capacity}kWh battery"

class Engine:
    def __init__(self, power):
        self.power = power
    
    def describe_engine(self):
        return f"{self.power}kW motor"

class ElectricCar(Battery, Engine):
    def __init__(self, brand, model, capacity, power):
        Battery.__init__(self, capacity)
        Engine.__init__(self, power)
        self.brand = brand
        self.model = model
    
    def describe_car(self):
        return f"{self.brand} {self.model} with {self.describe_battery()} and {self.describe_engine()}"

my_tesla = ElectricCar("Tesla", "Model S", 100, 250)
print(f"10. Multiple inheritance: {my_tesla.describe_car()}")
