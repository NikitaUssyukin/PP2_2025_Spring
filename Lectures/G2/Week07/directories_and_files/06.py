import os

path = os.getcwd()
# get cwd - current working directory

entries = os.scandir(path)

print(entries)
print(type(entries))