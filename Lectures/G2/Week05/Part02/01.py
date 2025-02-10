# iterators and generators

# iterators

# https://docs.python.org/3/tutorial/classes.html#iterators

a = [1, 2, 3] # a list, an example of an iterable

a_iter = iter(a) # iterator of the list a

print(next(a_iter)) # 1
print(next(a_iter)) # 2
print(next(a_iter)) # 3

print(next(a_iter)) # error: StopIteration
