# classes

# https://docs.python.org/3/tutorial/classes.html

# inheritance

# https://docs.python.org/3/tutorial/classes.html#inheritance

class Cat:
    kind = 'feline'

    def __init__(self, fur, age):
        self.fur = fur
        self.age = age

    def make_sound(self):
        print("Meow")

class HouseCat(Cat):
    def __init__(self, fur, age, name, breed):
        super().__init__(fur, age)
        self.name = name
        self.breed = breed

class WildCat(Cat):
    def __init__(self, fur, age, species):
        super().__init__(fur, age)
        self.species = species

    def make_sound(self):
        print("ROAR!")

garfield = HouseCat('ginger, fluffy', 5, 'Garfield','persian cat')
tiger = WildCat('ginger with black stripes', 3, 'Tiger')

garfield.make_sound()
tiger.make_sound()

    



