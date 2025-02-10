# iterators and generators

# iterators

# https://docs.python.org/3/tutorial/classes.html#iterators

class MyNums:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self): # has StopIteration
        if self.start > self.stop:
            raise StopIteration
        temp = self.start
        self.start += 1
        return temp

nums = MyNums(1, 10)

nums_iter = iter(nums)

# an infinite loop - we don't encounter StopIteration
for num in nums:
    print(num, end=' ')
