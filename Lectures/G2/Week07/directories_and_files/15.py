file_name = 'test.txt'

file = open(file_name)

# print(file)
# print(type(file))

file_contents = file.read()
print(file_contents, end='')