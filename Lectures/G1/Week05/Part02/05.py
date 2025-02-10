# iterators and generators

# iterators

# https://docs.python.org/3/tutorial/classes.html#iterators

class MyNums:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.start > self.stop:
            raise StopIteration
        elif self.step < 0 and self.start < self.stop:
            raise StopIteration
        elif self.step == 0:
            raise StopIteration
        temp = self.start
        self.start += self.step
        return temp

mynums = MyNums(10, 1, -1) # [10; 1] range, inclusive

# prints from 10 to 1 on new lines
for num in mynums:
    print(num)
