file_name = 'test.txt'

file = open(file_name)

# print(file)
# print(type(file))

lines_list = list(file)

print(lines_list)
print('Length:', len(lines_list))