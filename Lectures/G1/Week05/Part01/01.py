class MyClass:
    a = 5

    def __init__(self, b):
        self.b = b

    def print_a():
        print(MyClass.a)

    def print_b(self):
        print(self.b)

print(MyClass.a)

myclass = MyClass(10)
print(myclass.b)
print(myclass.a)

MyClass.print_a()
myclass.print_b()

MyClass.a = 123

print(MyClass.a)
print(myclass.b)
print(myclass.a)

myclass.b *= 2

print(myclass.b)
