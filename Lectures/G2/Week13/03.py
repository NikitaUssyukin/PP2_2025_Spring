lst = []

filename = 'lst.txt'

with open(filename, 'r') as file:
    contents = file.read()[1:-1] # slicing out the square brackets
    # print(contents)
    lst = list(map(int, contents.split(', ')))

print(lst)