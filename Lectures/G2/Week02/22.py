# Strings

# Using indexes []

a = "caterpillar"

print(a[0]) # first letter

# ways to get the last element
print(a[len(a) - 1]) 
print(a[-1])

# Slicing [::]

# str_name[start_idx:end_idx:step]

# start_index is inclusive
# if start_index is not specified, it is 0
# end_index is exclusive
# if end_index is not specified, it will be the index after the last (the length of a string)
# step sets how the index increments
# if step is not specified, it is 1 by default

# examples:

a = "pineapple"

print(a[:])
print(a[::])

print(a[0:4])
print(a[:4]) # same as above
# if your start_idx is 0, you can omit it

# another example, these 3 achieve the same result
print(a[4:9])
print(a[4:len(a)])
print(a[4:])

# changing the step
print(a[::2])

# step can also be in reverse
print(a[::-1])