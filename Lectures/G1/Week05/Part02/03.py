# iterators and generators

# iterators

# https://docs.python.org/3/tutorial/classes.html#iterators

class MyNums:
    def __init__(self, number=1):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self): # Lacks StopIteration
        temp = self.number
        self.number += 1
        return temp

mynums = MyNums()

# infinite loop
for num in mynums:
    print(num)
