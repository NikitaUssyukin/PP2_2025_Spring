a = [[0] * 3] * 3
b = [[0] * 3 for i in range(3)]

print(a)
print(b)

print(type(a))
print(type(b))

c = []
c += [[0] * 3]
c += [[0] * 3]
c += [[0] * 3]

print(c)
c[0][0] = 1

print(c)

d = [1, 2, 3]
e = d

e[0] = 5
print(d, e)