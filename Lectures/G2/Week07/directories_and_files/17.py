file_name = 'test.txt'

file = open(file_name)

# print(file)
# print(type(file))

for line in file:
    print(line, end='')