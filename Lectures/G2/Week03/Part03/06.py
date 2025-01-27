# Classes and objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def greeting1(person):
        print(f"Hello, {person.name}!")

    def greeting2(self):
        print(f"Hello, {self.name}!")

person1 = Person("Mark", 27)
person2 = Person("Ramazan", 70)

Person.greeting1(person1)
person2.greeting2()

person1.greeting1()