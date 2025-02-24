file_name = 'test.txt'

file = open(file_name, 'r')

print('Closed:', file.closed)
file.close()
print('Closed:', file.closed)