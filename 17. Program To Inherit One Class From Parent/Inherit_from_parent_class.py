# Write A Program To Inherit One Class From Parent.

class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        print("Some generic sound")

class Cat(Animal):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name
    
    def make_sound(self):
        print(f"{self.name} says Meow!")

cat = Cat("Feline", "Whiskers")
cat.make_sound()
