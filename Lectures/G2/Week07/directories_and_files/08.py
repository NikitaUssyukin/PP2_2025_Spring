import os

path = os.getcwd()
# get cwd - current working directory

entries = os.scandir(path)

print(entries)
print(type(entries))

for entry in entries:
    print('Name:', entry.name)
    print('Full path (including the file):', entry.path)
    print('Full path (excluding the file):', entry.path.removesuffix(entry.name))
    print('-----------------')