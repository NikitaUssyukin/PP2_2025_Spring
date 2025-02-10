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

print(next(nums_iter)) # 1
print(next(nums_iter)) # 2
print(next(nums_iter)) # 3

for _ in range(5): # 4 5 6 7 8
    print(next(nums_iter), end=' ')
