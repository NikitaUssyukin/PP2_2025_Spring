import os 

file_name = 'test.txt'

path = os.getcwd()

files_and_folders = os.scandir(path)

for element in files_and_folders:
    print(element) # DirEntry