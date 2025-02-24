file_name = 'test.txt'

with open(file_name, 'r') as file:
    print('Closed:', file.closed)

print('Closed:', file.closed)