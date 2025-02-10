# classes

# https://docs.python.org/3/tutorial/classes.html

class MyClass:
    a = 5 # attribute of the class MyClass

    def __init__(self, b):
        self.b = b # attribute of the instance of the class (of the object)

    def print_a(): # function of the class
        print(MyClass.a)

    def print_b(self): # function of the instance of the class
        print(self.b)

myclass = MyClass(10)

MyClass.print_a() # calling a function of the class
# myclass.print_a() # error, because self gets passed as the first argument
myclass.print_b() # calling a function of the instance of the class

