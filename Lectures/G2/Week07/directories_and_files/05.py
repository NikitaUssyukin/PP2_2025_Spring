import os

path = os.getcwd()
# get cwd - current working directory

for entry in os.listdir():
    print('Name:', entry)
    print('Is file:', os.path.isfile(entry))
    print('Is folder:', os.path.isdir(entry))
    print('-----------------')