# List comprehension

# The "C" way, how we are used to

ourlist = []

for i in range(5):
    ourlist.append(i)

print(ourlist)

# The Python way, using list comprehension

ourlist.clear()

ourlist = [item for item in range(5)]
# some_var = [expession for item in some_iterable condition]

print(ourlist)

anotherlist = [item * 2 for item in range(5) if item % 2 == 1]

print(anotherlist)
