class MyNums:
    def __init__(self, number=1):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.number
        self.number += 1
        return temp

mynums = MyNums()

mynums_iter = iter(mynums)

print(next(mynums_iter))
print(next(mynums_iter))
print(next(mynums_iter))
print(next(mynums_iter))
print(next(mynums_iter))
