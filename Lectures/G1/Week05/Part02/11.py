# iterators and generators

# generators

# https://docs.python.org/3/tutorial/classes.html#generators

def our_range(start, stop):
    while start < stop:
        a = start
        start += 1
        yield a

print(list(our_range(1, 10)))

