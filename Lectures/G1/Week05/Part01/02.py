class Cat:
    kind = 'feline'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Meow")

class HouseCat(Cat):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

class Tiger(Cat):
    def make_sound(self):
        print("ROAR!")


garfield = HouseCat('Garfield', 5, 'Persian cat')
tiger = Tiger('Amurskiy', 3)

garfield.make_sound()
tiger.make_sound()

print(garfield.kind)
print(tiger.kind)

print(Cat.kind)
print(HouseCat.kind)
print(Tiger.kind)