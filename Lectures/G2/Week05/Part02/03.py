# iterators and generators

# iterators

# https://docs.python.org/3/tutorial/classes.html#iterators

class MyNums:
    def __init__(self, start=1):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.start
        self.start += 1
        return temp

nums = MyNums()

nums_iter = iter(nums)

print(next(nums_iter))
print(next(nums_iter))
print(next(nums_iter))
