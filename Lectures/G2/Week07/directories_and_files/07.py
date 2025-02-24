import os

path = os.getcwd()
# get cwd - current working directory

entries = os.scandir(path)

print(entries)
print(type(entries))

for entry in entries:
    print('Name:', entry.name)
    print('Full path:', entry.path)
    print('Is file:', entry.is_file())
    print('Is folder:', entry.is_dir())
    print('-----------------')