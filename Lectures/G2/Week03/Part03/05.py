# Classes and objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

person1 = Person("Mark", 27)
person2 = Person("Ramazan", 70)

print(person1)
print(person2)