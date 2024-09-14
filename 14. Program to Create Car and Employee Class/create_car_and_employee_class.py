# Write A Program To Create Car And Employee Class

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def display_info(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: ${self.salary:.2f}")

# Create instances
car = Car("Toyota", "Camry", 2021)
employee = Employee("John Doe", "Software Engineer", 75000)

# Display information
car.display_info()
employee.display_info()
