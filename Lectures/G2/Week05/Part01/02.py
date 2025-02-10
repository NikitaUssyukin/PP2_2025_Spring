# classes

# https://docs.python.org/3/tutorial/classes.html

class MyClass:
    a = 5 # attribute of the class MyClass

    def __init__(self, b):
        self.b = b # attribute of the instance of the class (of the object)

print(MyClass.a) # printing the attribute of the class
# print(MyClass.b)
# error - MyClass has no such attribute

myclass = MyClass(10) # object of the class MyClass
print(myclass.b) # printing the attribute of the object of the class
print(myclass.a) # printing the attribute of the class from the object of the class

