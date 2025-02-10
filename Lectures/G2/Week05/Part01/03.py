# classes

# https://docs.python.org/3/tutorial/classes.html

class MyClass:
    a = 5 # attribute of the class MyClass

    def __init__(self, b):
        self.b = b # attribute of the instance of the class (of the object)

myclass1 = MyClass(10) # objects of the class MyClass
myclass2 = MyClass(15) 
myclass3 = MyClass(1)

print(myclass1.a, myclass1.b)
print(myclass2.a, myclass2.b)
print(myclass3.a, myclass3.b)

myclass2.b = 123

print('-----------------')
print(myclass1.a, myclass1.b)
print(myclass2.a, myclass2.b)
print(myclass3.a, myclass3.b)

myclass2.a = 789 # a becomes an attribute of the instance

print('-----------------')
print(myclass1.a, myclass1.b)
print(myclass2.a, myclass2.b)
print(myclass3.a, myclass3.b)

MyClass.a = 456

print('-----------------')
print(myclass1.a, myclass1.b)
print(myclass2.a, myclass2.b)
print(myclass3.a, myclass3.b)
