# iterators and generators

# iterators

# https://docs.python.org/3/tutorial/classes.html#iterators

class MyNums:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        temp = self.start
        self.start += 1
        return temp

mynums = MyNums(1, 10) # [1; 10] range, inclusive

# prints from 1 to 10 on new lines
for num in mynums:
    print(num)
