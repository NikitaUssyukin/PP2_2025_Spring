# iterators and generators

# generators

# https://docs.python.org/3/tutorial/classes.html#iterators

def our_range(start, stop, step=1):
    while(start < stop):
        yield start
        start += step

for num in our_range(1, 10):
    print(num)