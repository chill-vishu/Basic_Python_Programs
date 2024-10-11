# Write A Program That Demonstrates Polymorphism.

class Bird:
    def make_sound(self):
        print("Chirp")

class Dog:
    def make_sound(self):
        print("Bark")

def make_animal_sound(animal):
    animal.make_sound()

bird = Bird()
dog = Dog()

make_animal_sound(bird)
make_animal_sound(dog)
