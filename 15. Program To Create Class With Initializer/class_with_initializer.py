# Create A Program To Create Class With Initializer.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("Alice", 30)
person.display_info()
