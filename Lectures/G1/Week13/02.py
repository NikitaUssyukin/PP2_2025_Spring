lst = list(map(int, input().split(' ')))

# print(lst)

with open("lst.txt", "w") as file:
    file.write(str(lst))