lst = []

with open("lst.txt", "r") as file:
    file_contents = file.read()[1:-1] # slicing the needed part of the string
    # print(file_contents)
    lst = list(map(int, file_contents.split(', ')))

print(lst)


