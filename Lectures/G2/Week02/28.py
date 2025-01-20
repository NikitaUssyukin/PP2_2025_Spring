# Lists (like 1D arrays in C++)

# Unlike in C++, python lists can be heterogenous
# i.e. lists in python can contain values of different data typec
a = [1, 3.14, True, "Parrot"]

a[0] += 1
a[1] /= 2
a[2] *= 3
a[3] *= 4

print(a)

for item in a:
    print(item)

for i in range(len(a)):
    print(a[i])