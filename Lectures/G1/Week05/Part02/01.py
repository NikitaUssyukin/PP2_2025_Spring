# iterators and generators

# iterators

# https://docs.python.org/3/tutorial/classes.html#iterators

our_list = [1, 2, 3] # iterable

our_list_iter = iter(our_list) # iterator

print(next(our_list_iter)) # 1
print(next(our_list_iter)) # 2
print(next(our_list_iter)) # 3

print(next(our_list_iter)) # StopIteration