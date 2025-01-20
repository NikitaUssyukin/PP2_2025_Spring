# Python Strings

a = "cat"
b = a
c = a

# this will give an error - strings are immutable
# b[0] = c[2] = "r"

b = "car"
b = "rat"

print(b)
print(c)