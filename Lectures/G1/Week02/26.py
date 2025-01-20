# Loops

a = 5

for i in range(0, a + 1):
    if i % 2 == 0:
        print(i)

print("----")

for i in range(0, a + 1, 2):
    print(i)

for i in range(0, a + 1):
    if i % 2 != 0:
        continue
    print(i)