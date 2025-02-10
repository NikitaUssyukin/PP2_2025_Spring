# iterators and generators

# iterators

# https://docs.python.org/3/tutorial/classes.html#iterators

class MyNums:
    def __init__(self, start, stop, step=1):
        self.numbers = list(range(start, stop+1, step))

    def __iter__(self):
        return iter(self.numbers)

mynums = MyNums(10, 1, -1) # [10; 1] range, inclusive

mynums_iter = iter(mynums)

print(next(mynums_iter)) # 10
print(next(mynums_iter)) # 9
print(next(mynums_iter)) # 8
print(next(mynums_iter)) # 7
print(next(mynums_iter)) # 6

# prints from 10 to 1 on new lines
for num in mynums:
    print(num)
