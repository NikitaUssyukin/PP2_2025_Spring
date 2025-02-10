# iterators and generators

# generators

# https://docs.python.org/3/tutorial/classes.html#generators

a = 1

def func():
    global a
    b = a
    a += 1
    return b

print(func())
print(func())
print(func())
