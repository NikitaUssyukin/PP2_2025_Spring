# iterators and generators

# iterators

# https://docs.python.org/3/tutorial/classes.html#iterators

a = [1, 2, 3] # a list, an example of an iterable

a_iter = iter(a) # iterator of the list a

print(next(a_iter)) # 1

for num in a_iter: # 2 3
    print(num, end=' ')
