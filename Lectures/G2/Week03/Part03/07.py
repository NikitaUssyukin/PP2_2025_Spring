# Classes and objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Student(Person):
    def __init__(self, name, age, ID):
        super().__init__(name, age)
        self.ID = ID

    def __str__(self):
        return super().__str__() + f" with ID of {self.ID}"

student = Student("Aslan", 18, "24B242024")

print(student)