# iterators and generators

# generators

# https://docs.python.org/3/tutorial/classes.html#generators

def our_range(start, stop):
    result = []
    while start < stop:
        result.append(start)
        start += 1
    return result
    

print(our_range(1, 10))