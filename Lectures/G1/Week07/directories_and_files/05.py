import os

path = os.getcwd()
print(path)

contents = os.listdir(path)

for element in contents:
    print('Name:', element)
    print('Is a file:', os.path.isfile(element))
    print('Is a folder:', os.path.isdir(element))
    print("-------------")

