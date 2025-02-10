# iterators and generators

# generators

# https://docs.python.org/3/tutorial/classes.html#generators

def our_range(start, stop):
    while start < stop:
        a = start
        start += 1
        yield a

nums = our_range(1, 10)

print(next(nums))
print(next(nums))
print(next(nums))

for num in nums:
    print(num)