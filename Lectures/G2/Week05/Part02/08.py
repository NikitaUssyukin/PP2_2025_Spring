# iterators and generators

# iterators

# https://docs.python.org/3/tutorial/classes.html#iterators

class MyNums:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self): # has StopIteration
        if self.step > 0 and self.start > self.stop:
            raise StopIteration
        elif self.step < 0 and self.start < self.stop:
            raise StopIteration
        elif self.step == 0:
            raise StopIteration
        temp = self.start
        self.start += self.step
        return temp

nums = MyNums(1, 10, 1)
reverse_nums = MyNums(10, 1, -1)

for num in nums:
    print(num, end=' ')

print('\n-----------------')

for num in reverse_nums:
    print(num, end=' ')
