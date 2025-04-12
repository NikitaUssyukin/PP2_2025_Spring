lst = list(map(int, input().split(' ')))

# print(lst)

filename = 'lst.txt'

with open(filename, 'w') as file:
    file.write(str(lst))